#!/usr/bin/env python3
"""Validate store listing metadata against common character limits."""
import argparse,json
from pathlib import Path
LIMITS={"apple":{"title":30,"subtitle":30,"promotional_text":170,"description":4000,"keywords":100,"whats_new":4000},
        "google":{"title":50,"short_description":80,"description":4000}}
def validate(metadata,platform):
    limits=LIMITS[platform]; out={}
    for field,limit in limits.items():
        value=str(metadata.get(field,""))
        out[field]={"characters":len(value),"limit":limit,"valid":len(value)<=limit,"remaining":limit-len(value)}
    return out
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--platform",choices=LIMITS,required=True);p.add_argument("-o","--output",type=Path);a=p.parse_args()
    data=json.loads(a.input.read_text(encoding="utf-8")); result={"platform":a.platform,"fields":validate(data.get("metadata",data),a.platform)}
    s=json.dumps(result,indent=2,ensure_ascii=False)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    else:print(s)
if __name__=="__main__":main()
