import os.path
ac_file_path = os.path.dirname(os.path.abspath(
    __file__)) + '/../acceptance_criteria.md'
ex_file_path = os.path.dirname(
    os.path.abspath(__file__)) + '/../extra_criterias.md'
pb_file_path = os.path.dirname(
    os.path.abspath(__file__)) + '/../product_backlog.md'
prefix_potential = '/potential_backlog/potential_'


def sort_file(filename, potential=False):
    pb_file = pb_file_path

    if potential:
        filename = '/'.join(filename.split('/')
                            [:-1]) + prefix_potential + filename.split('/')[-1]
        pb_file = '/'.join(pb_file.split('/')
                           [:-1]) + prefix_potential + pb_file.split('/')[-1]

    f = open(filename, 'r').read()

    header = f.split('###')[0]
    tokens = f.split('###')[1:]

    us_ac = {}

    for t in tokens:
        t = [x.strip() for x in t.split('- ')[1:]]
        name, criterias = t[0], ['- ' + x for x in t[1:]]
        us_ac[name] = {
            'number': -1,
            'criterias': criterias,
        }

    f = open(pb_file, 'r').read()

    tokens = f.split('| US')[1:]
    for token in tokens:
        number = token.split('|')[0].strip()
        name = token.split('|')[3].strip()

        if name in us_ac:
            us_ac[name]['number'] = number
        else:
            us_ac[name] = {
                'number': number,
                'criterias': [
                    '- [ ] criterio1',
                    '- [ ] criterio2'
                ],
            }

    final_text = header

    sorted_us_ac = {k: v for k, v in sorted(
        us_ac.items(), key=lambda item: int(item[1]['number']))}
    for name, value in sorted_us_ac.items():
        number, criterias = value['number'], value['criterias']
        if number != -1:
            criterias = '\n'.join(criterias)
            final_text += f'### US{number} - {name}\n\n{criterias}\n\n'

    f = open(filename, 'w')
    f.write(final_text)
    f.close()

    return

# --- #


for i in False, True:
    sort_file(ac_file_path, potential=i)
    sort_file(ex_file_path, potential=i)
