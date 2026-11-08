#!/usr/bin/env python3
"""Compare user-supplied competitor metadata. No store scraping is performed."""
import argparse,json,re
from pathlib import Path
def tokens(text):return set(re.findall(r"[a-z0-9]+",str(text).lower()))
def analyze(items):
    docs=[]
    for item in items:
        words=tokens(" ".join(str(item.get(k,"")) for k in ("title","subtitle","description","keywords")))
        docs.append({"name":item.get("name","Unnamed"),"token_count":len(words),"keywords":sorted(words)})
    common=set.intersection(*(set(x["keywords"]) for x in docs)) if docs else set()
    union=set.union(*(set(x["keywords"]) for x in docs)) if docs else set()
    return {"competitors":docs,"shared_terms":sorted(common),"combined_terms":sorted(union),
            "note":"Based only on supplied metadata. Rankings, downloads, and visual assets are not collected."}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("-o","--output",type=Path);a=p.parse_args()
    data=json.loads(a.input.read_text(encoding="utf-8"));s=json.dumps(analyze(data.get("competitors",[])),indent=2)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    else:print(s)
if __name__=="__main__":main()
