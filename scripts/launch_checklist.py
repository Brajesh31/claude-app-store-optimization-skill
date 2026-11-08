#!/usr/bin/env python3
"""Generate a platform-aware pre-launch checklist."""
import argparse,json
from pathlib import Path
COMMON=["App identity, ownership, and contact details verified","Privacy policy and data disclosures reviewed","Production build tested on supported devices and OS versions","Crash reporting and analytics validated","Screenshots and app icon reviewed at store sizes","Support URL and user support process ready","Release notes reviewed","Rollback and incident contact documented"]
APPLE=["Title, subtitle, promotional text, description, and keywords within limits","App privacy details and tracking disclosures completed","Age rating and export compliance reviewed","In-app purchase metadata and review notes verified"]
GOOGLE=["Title, short description, and full description within limits","Data safety form and content rating completed","Target audience and ads declarations reviewed","App access instructions supplied for review"]
def build_checklist(platform):
    items=COMMON[:]
    if platform in ("apple","both"):items += ["[Apple] "+x for x in APPLE]
    if platform in ("google","both"):items += ["[Google] "+x for x in GOOGLE]
    return {"platform":platform,"checklist":[{"item":x,"complete":False} for x in items],"note":"Verify current store policies before submission."}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--platform",choices=["apple","google","both"],default="both");p.add_argument("-o","--output",type=Path);a=p.parse_args()
    result=build_checklist(a.platform)
    s=json.dumps(result,indent=2)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    else:print(s)
if __name__=="__main__":main()
