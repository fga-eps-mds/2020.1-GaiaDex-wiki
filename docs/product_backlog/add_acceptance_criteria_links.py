import re
from collections import defaultdict

is_user_story_line = re.compile('US\d{2}')
has_criteria_link_added = re.compile('\[→\]\(\.\/acceptance\_criteria\.md\#US\d{2}\-\-\-.*')
text = ''

with open('product_backlog.md') as file:
    for line in file.readlines():
        found_us = is_user_story_line.findall(line)
        found_ac = has_criteria_link_added.findall(line)

        if found_us:
            requirement = line.split('|')[4].strip()
            requirement = re.sub('\W+', ' ', requirement).replace(' ', '-')
            user_story = found_us[0]

            link = f'[→](./acceptance_criteria.md#{user_story}---{requirement})'
            if found_ac:
                text += line.replace(found_ac[0], link)
            else:
                text += ' ' + line.strip() + link + ' |\n'
        else:
            text += line

f = open('product_backlog.md', 'w')
f.write(text)
f.close()