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

                issue_title = 'US{:02d} - {}'.format(us_number, want)

                description = f'{description} {user} quero {want.lower()} para {so_that}.'

    return (issue_title, description)


def gen_acex_list(us_number, filename):
    acs = []
    with open(filename) as file:
        flag = 0
        for line in file.readlines():
            if 'US' in line and flag == 1:
                break
            if flag == 1 and '- [ ]' in line:
                acs.append(
                    line.split('- [ ]')[-1].strip().replace(';', '\\').replace('|', '\\'))
            if "US{:02d}".format(us_number) in line:
                flag = 1

    return ';'.join(acs)


def remove_duplicates(filepath):
    s = OrderedDict()
    for line in open(filepath, 'r'):
        if '| title | description |' not in line and '| ----- | ----------- |' not in line:
            s[line] = None

    with open(filepath, 'w') as file:
        file.write(
            '| title | description | acceptance criteria | tasks |\n| ----- | ----------- | ------------------- | ----- |\n')
        file.writelines(s.keys())

def number_of_user_stories():
    with open(pb_file_path, 'r') as f:
        f = f.read()
        return len(f.split('| US'))

for i in range(1, number_of_user_stories()):
    issue_title, description = gen_description(i)
    ac = gen_acex_list(i, ac_file_path)
    ex = gen_acex_list(i, ex_file_path)

    issue = f'| {issue_title} | {description} | {ac} | {ex} |\n'

    with open('template_issues.md', 'a') as file:
        file.write(issue)

remove_duplicates('template_issues.md')
