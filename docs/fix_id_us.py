import glob
import re

us_num = {}
with open('product_backlog/product_backlog.md', 'r') as file:
    file = file.read()
    tokens = file.split('| US')[1:]
    for l in tokens:
        number = l.split('|')[0].strip()
        name = l.split('|')[3].strip()
        us_num[name] = number

# print(us_num)
for path in glob.glob('**/*.md', recursive=True):
    flag = 0
    with open(path, 'r') as file:
        file = file.read()
        for name, number in us_num.items():
            name_rgx = re.escape(name)
            rgx = re.compile(r'\d{2}(?=\s\-\s'+name_rgx+r')');
            z = rgx.findall(file)
            if len(z):
                file = rgx.sub(number, file)
        f = open(path, 'w')
        f.write(file)
        f.close()