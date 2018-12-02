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

def main(p_path, path, e_path, *args):
	#print("p-add-path:         ", path)
	#print("p-add-e_path:       ", e_path)
	#print("p-add-args:         ", list(args))
	
	if len(args) == 0:
		print("bad input")
		return 1
		
	command = args[0]
	comment = ' '.join(args[1:])
		
	cargs = re.findall('\[([^]]+)\]', comment)
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
	#print(new_command)
	
	data = load_json(path + "/data.json")
	data.append(new_command)
	save_json(data, path + "/data.json")
	
	#print(data)

if __name__ == "__main__":
	main(*sys.argv)
