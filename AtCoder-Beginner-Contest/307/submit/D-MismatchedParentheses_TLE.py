#[TLE] 423Byte TLEms 203252KB Python3
import re

n = int(input())
s = input()

def delete_brackets(s):
    table = {
        "(": "（",
        ")": "）",
    }
    for key in table.keys():
        s = s.replace(key, table[key])
    s = re.sub('（[^（|^）]*）', "", s)
    return delete_brackets(s) if sum( [1 if re.search('（[^（|^）]*）', s) else 0] ) > 0 else s.replace("（","(").replace("）",")")

r = delete_brackets(s)
print(r)
