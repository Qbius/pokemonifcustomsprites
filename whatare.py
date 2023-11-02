import json
import os
import re

raw = [m.groups() for f in os.listdir('custom') if (m := re.match(r'(\d+)\.(\d+)(.*)\.png', f))]
res = {}
for a, b, c in raw:
    if a not in res:
        res[a] = {}
    if b not in res[a]:
        res[a][b] = []
    res[a][b] = sorted([*res[a][b], c])
json.dump(res, open('sprite_info.json', 'w'), indent=4)