# Usage: python make_data.py path\to\dashboard_rows.json   -> rewrites data.json with a fresh timestamp
import json,sys,datetime
rows=json.load(open(sys.argv[1]))
json.dump({"updated":datetime.datetime.now().astimezone().isoformat(timespec="seconds"),"rows":rows},open("data.json","w"),separators=(",",":"))
print(len(rows),"reports written to data.json")
