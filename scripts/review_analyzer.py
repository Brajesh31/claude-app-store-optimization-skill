#!/usr/bin/env python3
"""Basic lexicon-based review triage for a supplied JSON list of reviews."""
import argparse,json,re
from collections import Counter
from pathlib import Path
POS={"good","great","love","easy","useful","fast","excellent","helpful","smooth","awesome"}
NEG={"bad","poor","slow","crash","bug","broken","hard","issue","fail","terrible","annoying"}
def analyze(reviews):
    out=[];themes=Counter();counts=Counter()
    for item in reviews:
        text=str(item.get("text",""));words=set(re.findall(r"[a-z]+",text.lower()))
        pos=len(words&POS);neg=len(words&NEG);sent="positive" if pos>neg else "negative" if neg>pos else "neutral"
        counts[sent]+=1
        for theme in ("login","payment","crash","performance","notification","feature","support"):
            if theme in words:themes[theme]+=1
        out.append({"id":item.get("id"),"sentiment_heuristic":sent,"positive_hits":pos,"negative_hits":neg})
    return {"total":len(reviews),"sentiment_counts":dict(counts),"theme_counts":dict(themes),"reviews":out,
            "note":"Simple keyword heuristic, not a trained sentiment model. Human review is required."}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("-o","--output",type=Path);a=p.parse_args()
    d=json.loads(a.input.read_text(encoding="utf-8"));s=json.dumps(analyze(d.get("reviews",[])),indent=2)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    else:print(s)
if __name__=="__main__":main()
