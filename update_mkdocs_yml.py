import glob
import yaml

def has_child_object(d):
		for k,v in d.items():
				if type(v) == dict:
					return True
		return False

d = {'docs':{}}

for filepath in glob.glob('docs/**/*.md',recursive=True):
		for i, folder in enumerate(filepath.split('/')[1:-1]):
				if i == 0:
						d['docs'].setdefault(folder, {'name':''})
				else:
						d['docs'][filepath.split('/')[1]].setdefault(folder, {'name':''})

		if 'template_issues' not in filepath:
				with open(filepath, 'r') as file:
						doc_name = file.readline().strip('# ').strip('\n')
						keys = filepath.split('/')[:-1]					
						if len(keys) == 2:
								d[keys[0]][keys[1]]['name'] = doc_name
								d[keys[0]][keys[1]][doc_name] = filepath.replace('docs/', '')							
						if len(keys) == 3:
								d[keys[0]][keys[1]][keys[2]]['name'] = doc_name
								d[keys[0]][keys[1]][keys[2]][doc_name] = filepath.replace('docs/', '')							

result = {}

for k1, v1 in d['docs'].items():
		if not has_child_object(d['docs'][k1]):
				artifact_name = d['docs'][k1]['name']
				if len(d['docs'][k1]) <= 2:
						result['- '+artifact_name] = d['docs'][k1][artifact_name]
				else:
						if 'RoadMap de papéis' == artifact_name:
								artifact_name = 'Roadmap de Produto'
						if 'Guia de estilo NodeJS' == artifact_name:
								artifact_name = 'Guia de Estilo'
						result['- '+artifact_name] = {}
						for k2, v2 in d['docs'][k1].items():
								if k2 != 'name':
										result['- '+artifact_name]['- '+k2] = v2
		else:
				artifact_name = d['docs'][k1]['name']
				if 'Planejamento da Sprint N' in artifact_name or 'Resultados da Sprint N' in artifact_name:
						artifact_name = 'Sprints'
				result['- '+artifact_name] = {}
				for k2, v2 in d['docs'][k1].items():
						if type(v2) == dict:
								sec_artifact_name = d['docs'][k1][k2]['name']
								if 'Planejamento da Sprint' in sec_artifact_name or 'Resultados da Sprint' in sec_artifact_name:
										sec_artifact_name = ' '.join(sec_artifact_name.split(' ')[-2:])
								result['- '+artifact_name]['- '+sec_artifact_name] = {}
								for k3, v3 in d['docs'][k1][k2].items():
										if k3 != 'name':
												result['- '+artifact_name]['- '+sec_artifact_name]['- '+k3] = v3
						elif k2 != 'name':
								result['- '+artifact_name]['- '+k2] = v2

text_result = yaml.dump(result,allow_unicode=True,default_flow_style=False, indent=4).replace('\'', '')
text_result = '  - Inicio: index.md\n' + text_result
text_result = '\n  '.join(text_result.split('\n')) + '\n'

with open('mkdocs.yml', 'r') as file:
		file = file.read()
		nav = file.split('nav:\n')[-1].split('# Style')[0]
		result = file.replace(nav, text_result)
		
		with open('mkdocs.yml', 'w') as file:
				file.write(result)
