# based on -> https://github.com/andre-filho/ezissue
from collections import OrderedDict
import os.path

pb_file_path = os.path.dirname(
    os.path.abspath(__file__)) + '/product_backlog.md'
ac_file_path = os.path.dirname(
    os.path.abspath(__file__)) + '/acceptance_criteria.md'
ex_file_path = os.path.dirname(
    os.path.abspath(__file__)) + '/extras.md'


def gen_description(us_number):
    description = 'Eu como'
    issue_title = ''
    with open(pb_file_path) as file:
        for line in file.readlines():
            if "US{:02d}".format(us_number) in line:
                user = line.split('|')[3].strip().lower()
                want = line.split('|')[4].strip()
                so_that = line.split('|')[5].strip().lower()

                issue_title = '{:02d} - {}'.format(us_number, want)

                description = f'{description} {user} quero {want.lower()} para {so_that}.'

    return (issue_title, description)


def gen_acex_list(us_number, filename):
    acs = []
    with open(filename) as file:
        has_reached_user_story = False
        for line in file.readlines():
            if 'criterio 1' in line or 'criterio 2' in line or 'criterio1' in line or 'criterio2' in line:
                continue
            if 'US' in line and has_reached_user_story == True: #reached next US, leave
                break
            if has_reached_user_story == True and '- [ ]' in line:
                acs.append(line.split('- [ ]')[-1].strip().replace(';', '\\').replace('|', '\\'))
            if "US{:02d}".format(us_number) in line:
                has_reached_user_story = True

    return ';'.join(acs)


def remove_duplicates(filepath):
    s = OrderedDict()
    for line in open(filepath, 'r'):
        if '| title | description |' not in line and '| ----- | ----------- |' not in line:
            s[line] = None

    with open(filepath, 'w') as file:
        file.write(
            '| title | description | acceptance criteria | extras |\n| ----- | ----------- | ------------------- | ---- |\n')
        file.writelines(s.keys())

def number_of_user_stories():
    with open(pb_file_path, 'r') as f:
        f = f.read()
        return len(f.split('| US'))

with open('template_issues.md', 'w') as file:
    file.write('')

for i in range(1, number_of_user_stories()):
    issue_title, description = gen_description(i)
    ac = gen_acex_list(i, ac_file_path)
    ex = gen_acex_list(i, ex_file_path)
    issue = f'| {issue_title} | {description} | {ac} | {ex} |\n'

    with open('template_issues.md', 'a') as file:
        file.write(issue)

remove_duplicates('template_issues.md')
