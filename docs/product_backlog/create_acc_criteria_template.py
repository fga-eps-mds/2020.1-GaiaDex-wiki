import re
from collections import defaultdict

is_user_story_line = re.compile('US\d{2}')
has_criteria_link_added = re.compile('\[→\]\(\.\/acceptance\_criteria\.md\#US\d{2}\-\-\-')

text = ''
with open('product_backlog.md') as file:
    for line in file.readlines():
        found_us = is_user_story_line.findall(line)
        
        if found_us:
            requirement = line.split('|')[4].strip()
            user_story = found_us[0]

            text += f'### {user_story} - {requirement}\n'
            text += '- [ ] criterio 1\n'
            text += '- [ ] criterio 2\n\n'

f = open('template_criteria.md', 'w')
f.write(text)
f.close()