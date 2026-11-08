#!/usr/bin/env python3
"""Calculate a transparent heuristic ASO score from supplied metrics."""
import argparse,json
from pathlib import Path
def clamp(v,lo=0,hi=1):return max(lo,min(hi,float(v)))
def score(data):
    m=data.get("metadata",{});r=data.get("ratings",{});c=data.get("conversion",{});k=data.get("keyword_rankings",{})
    parts={
      "metadata_quality":25*sum(clamp(m.get(x,0)) for x in ("title_quality","description_quality","keyword_density"))/3,
      "ratings_reviews":25*(0.7*clamp((float(r.get("average_rating",0))-1)/4)+0.3*clamp(float(r.get("total_ratings",0))/10000)),
      "conversion":25*clamp(float(c.get("impression_to_install",0))/0.2),
      "keyword_performance":25*clamp((float(k.get("top_10",0))+0.5*float(k.get("top_50",0))+0.2*float(k.get("top_100",0)))/50)
    }
    return {"overall_score":round(sum(parts.values()),1),"breakdown":{x:round(y,1) for x,y in parts.items()},
            "method":"Heuristic score using supplied inputs; not an official Apple or Google ranking metric."}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("-o","--output",type=Path);a=p.parse_args()
    s=json.dumps(score(json.loads(a.input.read_text(encoding="utf-8"))),indent=2)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    else:print(s)
if __name__=="__main__":main()
