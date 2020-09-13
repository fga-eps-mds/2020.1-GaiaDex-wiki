import re
from collections import defaultdict

is_user_story_line = re.compile('US\d{2}')

text = ''

d = defaultdict(lambda: [])

with open('product_backlog.md') as file:
    for line in file.readlines():
        found = is_user_story_line.findall(line)
        if found:
            epico = line.split('|')[2].strip()
            d[epico].append(line)
        else:
            text += line

for key, value in d.items():
    for us in value:
        text += us

idx = 1
final_text = ''
for line in text.split('\n'):
    found = is_user_story_line.findall(line)
    if found:
        line = line.replace(found[0], "US{:02d}".format(idx))
        idx += 1
    final_text += line+'\n'

f = open('product_backlog.md', 'w')
f.write(final_text)
f.close()
