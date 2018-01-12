import re
st = '/root:0:x bin ama:m:a'
pat = ':'
replace = '-'
s2 = re.sub(pat, replace, st, flags=re.I, count=1)
print(s2)

counter = 0
match_count = len(re.findall(pat,st,re.I))
print(match_count)

def replace_last_tw(m):
    global counter
    counter += 1
    repstat = replace if counter > match_count -2 else m.group()
    return repstat

s3 = re.sub(pat, replace_last_tw, st, flags=re.I)
print(s3)