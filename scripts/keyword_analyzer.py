#!/usr/bin/env python3
"""Heuristic keyword triage. Does not fetch or estimate real store search volume."""
import argparse, json, re
from pathlib import Path

def analyze_keyword(keyword, features=(), category=""):
    words = re.findall(r"[a-z0-9]+", keyword.lower())
    feature_words = set(re.findall(r"[a-z0-9]+", " ".join(features).lower()))
    category_words = set(re.findall(r"[a-z0-9]+", category.lower()))
    overlap = len(set(words) & (feature_words | category_words))
    relevance = round(overlap / max(len(set(words)), 1), 2)
    return {"keyword": keyword, "word_count": len(words), "relevance_heuristic": relevance,
            "length": len(keyword), "long_tail_candidate": len(words) >= 3,
            "note": "No live search-volume or competition data was queried."}

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument("input",type=Path); p.add_argument("-o","--output",type=Path)
    a=p.parse_args(); data=json.loads(a.input.read_text(encoding="utf-8"))
    rows=[analyze_keyword(k,data.get("key_features",[]),data.get("category","")) for k in data.get("target_keywords",[])]
    result={"app_name":data.get("app_name"),"keywords":sorted(rows,key=lambda x:(-x["relevance_heuristic"],x["length"]))}
    rendered=json.dumps(result,indent=2,ensure_ascii=False)
    if a.output:a.output.write_text(rendered+"\n",encoding="utf-8")
    else:print(rendered)
if __name__=="__main__":main()
