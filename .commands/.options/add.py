import sys
import json
import re

def load_json(path):
	with open(path, "r") as j:
		return json.load(j)
		
def save_json(data, path):
	with open(path, "w") as j:
		json.dump(data, j)
		
def option_to_dict(string):
	desc = re.findall('\*([^*]+)\*', string)
	if len(desc) > 0:
		desc = desc[0]
	else:
		desc = ""
	name = " ".join(string.replace('*' + desc + '*', "").split())
	d = {}
	if len(desc) > 0:
		d["desc"] = desc
	if len(name) > 0:
		d["name"] = name
	#print("name: ", name,"desc: ", desc)
	return d

def main(path, *args):
	path = '/'.join(path.split('/')[:-2]) + '/'
	args = args[0][0]
	#print(args)
	command = re.findall('([^]]+)\[', args)
	if len(command) > 0:
		command = command[0][:-1]
	else:
		command = args
		
	cargs = re.findall('\[([^]]+)\]', args)
	options = list(
		map(
			lambda x: list(
				map(
					lambda y: option_to_dict(" ".join(y.split())),
					x.split('|')
				)
			),
			cargs
		)
	)
	
	new_command = {"command": command, "options": options}
	
	data = load_json(path + "./data.json")
	data.append(new_command)
	
	save_json(data, path + "./data.json")
	
	#print(data)

if __name__ == "__main__":
	main(sys.argv[0], sys.argv[1:])
