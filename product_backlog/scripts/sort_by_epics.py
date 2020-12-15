import re
from collections import defaultdict
import os.path
pb_filepath = os.path.dirname(os.path.abspath(
    __file__)) + '/../product_backlog.md'
prefix_potential = '/potential_backlog/potential_'

is_user_story_line = re.compile(r'US\d{2}')


def sort_by_epics(filename, potential=False):
    text = ''
    if potential:
        filename = '/'.join(filename.split('/')
                            [:-1]) + prefix_potential + filename.split('/')[-1]

    d = defaultdict(lambda: [])

    with open(filename) as file:
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
        final_text += line + '\n'

    f = open(filename, 'w')
    f.write(final_text)
    f.close()


for i in False, True:
    sort_by_epics(pb_filepath, potential=i)
