import re
import os.path

pb_filepath = os.path.dirname(os.path.abspath(
    __file__)) + '/../product_backlog.md'

is_user_story_line = re.compile(r'US\d{2}')
has_criteria_link_added = re.compile(
    r'\[→\]\(\.\/acceptance\_criteria\.md\#US\d{2}\-\-\-.*')
prefix_potential = '/potential_backlog/potential_'


def add_acc(filename, potential=False):
    text = ''

    if potential:
        filename = '/'.join(filename.split('/')
                            [:-1]) + prefix_potential + filename.split('/')[-1]

    with open(filename) as file:
        for line in file.readlines():
            found_us = is_user_story_line.findall(line)
            found_ac = has_criteria_link_added.findall(line)

            if found_us:
                requirement = line.split('|')[4].strip()
                requirement = re.sub(
                    r'\W + ', ' ', requirement).replace(' ', '-')
                user_story = found_us[0]

                link = f'[→](./acceptance_criteria.md#{user_story}---{requirement}) |'
                if found_ac:
                    text += line.replace(found_ac[0], link)
                else:
                    text += ' ' + line.strip() + link + ' |\n'
            else:
                text += line

    f = open(filename, 'w')
    f.write(text)
    f.close()

    return


for i in False, True:
    add_acc(pb_filepath, potential=i)
