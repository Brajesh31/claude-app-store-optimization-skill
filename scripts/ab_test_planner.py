#!/usr/bin/env python3
"""Estimate per-variant sample size for a two-proportion A/B test."""
import argparse,json,math
from pathlib import Path
from statistics import NormalDist
def sample_size(baseline,relative_lift,alpha=.05,power=.8):
    p1=float(baseline);p2=min(.999999,p1*(1+float(relative_lift)))
    if not 0<p1<1 or not p1<p2<1:raise ValueError("baseline and lift must produce proportions between 0 and 1, with p2 > p1")
    z_alpha=NormalDist().inv_cdf(1-alpha/2);z_power=NormalDist().inv_cdf(power);pbar=(p1+p2)/2
    n=((z_alpha*math.sqrt(2*pbar*(1-pbar))+z_power*math.sqrt(p1*(1-p1)+p2*(1-p2)))**2)/(p2-p1)**2
    return math.ceil(n)
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("-o","--output",type=Path);a=p.parse_args()
    d=json.loads(a.input.read_text(encoding="utf-8"));n=sample_size(d["baseline_conversion"],d["relative_lift"],d.get("alpha",.05),d.get("power",.8))
    s=json.dumps({"sample_size_per_variant":n,"total_sample_size":2*n,"assumptions":"Independent two-sided comparison of proportions; normal approximation. Adjust for multiple comparisons and actual experiment design."},indent=2)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    else:print(s)
if __name__=="__main__":main()
