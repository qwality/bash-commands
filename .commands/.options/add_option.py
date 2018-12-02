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
	#print("p-add_o-path:       ", path)
	#print("p-add_o-e_path:     ", e_path)
	#print("p-add_o-args:       ", list(args))
	
	if len(args) < 4:
		print("bad input")
		return 1
	
	options = load_json(path + "/.options/options.json")
	
	flag, arg, program, *file_name = args
	file_name = ' '.join(file_name)
	
	if flag[0] != '-':
		print("bad input")
		return 1
	
	for option in options[1:]:
		if option["flag"] == flag:
			print("bad input")
			return 1
			
	if arg == "True" or arg == "False":
		pass
	else:
		print("bad input", arg)
		return 1
	
	#print(flag, arg, program, file_name)
	
	new_command = {"flag": flag, "program": program, "file": file_name, "args": arg}
	options.append(new_command)
	save_json(options, path + "/.options/options.json")
	
	#print(data)

if __name__ == "__main__":
	main(*sys.argv)
