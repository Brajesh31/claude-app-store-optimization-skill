#!/usr/bin/env python3
"""Validate user-supplied localized store metadata; does not translate text."""
import argparse,json
from pathlib import Path
LIMITS={"apple":{"title":30,"subtitle":30,"promotional_text":170,"description":4000,"keywords":100},
        "google":{"title":50,"short_description":80,"description":4000}}
def validate(locales,platform):
    result={}
    for locale,fields in locales.items():
        result[locale]={}
        for field,limit in LIMITS[platform].items():
            value=str(fields.get(field,""))
            result[locale][field]={"characters":len(value),"limit":limit,"valid":len(value)<=limit}
    return result
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--platform",choices=LIMITS,required=True);p.add_argument("-o","--output",type=Path);a=p.parse_args()
    d=json.loads(a.input.read_text(encoding="utf-8"));s=json.dumps(validate(d.get("locales",{}),a.platform),indent=2,ensure_ascii=False)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    else:print(s)
if __name__=="__main__":main()
