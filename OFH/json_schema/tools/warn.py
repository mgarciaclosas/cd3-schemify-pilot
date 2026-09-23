"""Warning checks for the Our Future Health package: reports findings, never rejects or changes data.

Usage:  python tools/warn.py --file DATA.json --table TABLE [--max-rows 20]
        python tools/warn.py --file DATA.csv  --table TABLE --format csv

DATA is a JSON array of row objects (or a CSV whose absent values are the literal -998). The checks live in
tools/warnings/TABLE.warnings.json. The exit code is 0 whether or not warnings are found."""
import argparse, csv, json, sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent


def int_columns(schema):
    cols = set()
    for entry in schema["items"]["allOf"]:
        for prop, sub in entry.get("then", {}).get("properties", {}).items():
            if isinstance(sub.get("const"), int):
                cols.add(prop)
        for prop, sub in entry.get("if", {}).get("properties", {}).items():
            if isinstance(sub.get("const"), int):
                cols.add(prop)
    return cols


def range_columns(schema):
    """Columns checked by a numeric range (minimum/maximum); a CSV cell for one is read as a number."""
    cols = set()
    for entry in schema["items"]["allOf"]:
        for prop, sub in entry.get("properties", {}).items():
            cols.add(prop)
    return cols


def as_number(text):
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--table", required=True)
    ap.add_argument("--format", choices=["json", "csv"], default=None)
    ap.add_argument("--max-rows", type=int, default=20)
    args = ap.parse_args()
    path = ROOT / "warnings" / (args.table + ".warnings.json")
    if not path.is_file():
        print(json.dumps({"ok": False, "error": "no warning checks for table " + args.table}))
        return 0
    schema = json.load(open(path, encoding="utf-8"))
    if not Path(args.file).is_file():
        print(json.dumps({"ok": False, "error": "data file not found: " + args.file}))
        return 0
    fmt = args.format or ("csv" if args.file.lower().endswith(".csv") else "json")
    if fmt == "csv":
        ints = int_columns(schema)
        nums = range_columns(schema)
        data = []
        with open(args.file, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                for c in ints:
                    if c in row:
                        row[c] = as_number(row[c])
                for c in nums:
                    if c in row:
                        row[c] = as_number(row[c])
                data.append(row)
    else:
        data = json.load(open(args.file, encoding="utf-8"))
    checks = schema["items"]["allOf"]
    validator = Draft202012Validator(schema["items"])
    found = {}
    for i, row in enumerate(data):
        seen = set()
        for err in validator.iter_errors(row):
            path_ = list(err.schema_path)
            idx = path_[path_.index("allOf") + 1] if "allOf" in path_ else None
            if idx is None or idx in seen:
                continue
            seen.add(idx)
            found.setdefault(idx, []).append(i)
    out = []
    for idx, rws in sorted(found.items()):
        text = checks[idx]["$comment"]
        rule = text.split(":")[0].replace("Warning ", "")
        out.append({"rule": rule, "count": len(rws), "rows": rws[: args.max_rows], "message": text.split(": ", 1)[1]})
    print(json.dumps({"ok": True, "table": args.table, "rows_checked": len(data), "warnings": len(found),
                      "findings": out, "note": "Warnings only: nothing is rejected and no data is changed."}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
