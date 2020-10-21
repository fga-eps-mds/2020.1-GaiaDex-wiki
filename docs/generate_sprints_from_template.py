import json
import unicodedata

def planning(filename, list_of_us, sprint_number):
    file = open(filename, 'r').read()
    file = file.replace('Planejamento da Sprint N', f'Planejamento da Sprint {sprint_number}').replace('planejamento-da-sprint-n', f'planejamento-da-sprint-{sprint_number}')

    issues = []

    for us in list_of_us:
        us = us.lstrip('* ')
        us_as_filename = us.lower().replace(' - ', '_').replace('/', '_').replace(' ', '_').replace('(', '').replace(')', '')
        us_as_filename = unicodedata.normalize('NFKD', us_as_filename).encode('ASCII', 'ignore').decode('ASCII')
        type_of_issue = 'BackEnd' if 'backend' in us else 'FrontEnd' if 'frontend' in us else 'wiki'

        issue = f'''
1. [{us}](https://github.com/fga-eps-mds/2020.1-GaiaDex-{type_of_issue}/issues/)

    - ![pont_{us_as_filename}](img/pont_{us_as_filename}.png)
    - Resultado final - X
'''

        issues.append(issue)
    
    replace_template_issues = '''
1. [Issue N](https://github.com/fga-eps-mds/2020.1-GaiaDex-)

    - ![pont_xxx](img/pont_xxx.png)
    - Resultado final - Y

2. [Issue N](https://github.com/fga-eps-mds/2020.1-GaiaDex-)

    - ![pont_xxx](img/pont_xxx.png)
    - Resultado final - Y
'''

    result = file.replace(replace_template_issues, ''.join(issues))
    f = open(filename, 'w')
    f.write(result)
    f.close()


def results_and_meeting_minutes(filename, list_of_us, sprint_number, next_issues = []):
    file = open(filename, 'r').read()
    file = file.replace('Resultados da Sprint N', f'Resultados da Sprint {sprint_number}').replace('resultados-da-sprint-n', f'resultados-da-sprint-{sprint_number}')

    rows = []

    for us in list_of_us:
        us = us.lstrip('* ')
        type_of_row = 'BackEnd' if 'backend' in us else 'FrontEnd' if 'frontend' in us else 'wiki'
        row = f'| [{us}](https://github.com/fga-eps-mds/2020.1-GaiaDex-{type_of_row}/issues/) | 0 | Concluído/Não Concluído/Em andamento |'
        rows.append(row)

    replace_template_rows = '| [Issue N](https://github.com/fga-eps-mds/2020.1-GaiaDex-)| 0 | Concluído/Não Concluído/Em andamento |'

    result = file.replace(replace_template_rows, '\n'.join(rows))

    if next_issues != []:
        next_issues = [x.replace('*', '-') for x in next_issues]
        print(next_issues)
        result = result.replace('...', '\n'.join(next_issues))

    f = open(filename, 'w')
    f.write(result)
    f.close()

with open('roadmap/product_roadmap.md', 'r') as product_roadmap:
    product_roadmap = product_roadmap.read()
    sprints = product_roadmap.split('### Sprint ')[1:]
    sprints[-1] = sprints[-1].strip('## Release 2\n')

    us_by_sprints = { k:v for k, v in [(i.split('\n')[0], [z for z in i.split('\n') if z != '' and z[0] ==  '*']) for i in sprints] if int(k) >= 8}

    for sprint, list_of_us in us_by_sprints.items():
        base = f'sprints/sprint{sprint}'

        planning(f'{base}/planning.md', list_of_us, sprint)
        results_and_meeting_minutes(f'{base}/results.md', list_of_us, sprint)
        if int(sprint) < 14:
            results_and_meeting_minutes(f'{base}/meeting_minutes.md', list_of_us, sprint, next_issues=us_by_sprints[str(int(sprint)+1)])
        else:
            results_and_meeting_minutes(f'{base}/meeting_minutes.md', list_of_us, sprint)
