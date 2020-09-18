import os.path
ac_file_path = os.path.dirname(os.path.abspath(__file__)) + '/../acceptance_criteria.md'
ex_file_path = os.path.dirname(os.path.abspath(__file__)) + '/../extras.md'
pb_file_path = os.path.dirname(os.path.abspath(__file__)) + '/../product_backlog.md'

def sort_file(filename):
    f = open(filename, 'r').read()
    
    header = f.split('###')[0]
    tokens = f.split('###')[1:]

    us_ac = {}

    for t in tokens:
        t = [x.strip() for x in t.split('- ')[1:]]
        name, criterias = t[0], ['- '+x for x in t[1:]]
        us_ac[name] = {
            'number': -1,
            'criterias': criterias,
        }

    
    f = open(pb_file_path, 'r').read()

    us_num = {}
    tokens = f.split('| US')[1:]
    for l in tokens:
        number = l.split('|')[0].strip()
        name = l.split('|')[3].strip()

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

    sorted_us_ac = {k: v for k, v in sorted(us_ac.items(), key=lambda item: int(item[1]['number']))}
    for name, value in sorted_us_ac.items():
        number, criterias = value['number'], value['criterias']
        if number != -1:
            criterias = '\n'.join(criterias)
            final_text += f'### US{number} - {name}\n\n{criterias}\n\n'        
    
    f = open(filename, 'w')
    f.write(final_text)
    f.close()

sort_file(ac_file_path)
sort_file(ex_file_path)
