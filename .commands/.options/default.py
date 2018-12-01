import sys
import json

def load_json(path):
	with open(path, "r") as j:
		return json.load(j)
		
def save_json(data, path):
	with open(path, "w") as j:
		json.dump(data, j)
		
def dict_to_str(d):
	out = ""
	name = d.get("name")
	desc = d.get("desc")
	if name != None:
		out += name
	if name != None and desc != None:
		out += " "
	if desc != None:
		out += '*' + desc + '*'
	return out
		
def option(o):
	return " | ".join(map(dict_to_str, o))
	
def options(o):
	return ["[ " + option(x) + " ]" for x in o]
		
def radek(dct):
	return [dct["command"], *options(dct["options"])]
	
def pretty_print(data):
	widths = [0 for x in range(max(len(row) for row in data))]
	for r in range(len(data)):
		for c in range(len(data[r])):
			if len(data[r][c]) > widths[c]:
				widths[c] = len(data[r][c])
	
	for row in data:
		print("".join(row[i].ljust(widths[i] + 2) for i in range(len(row))))
			
		

def main(path, *args):
	path = '/'.join(path.split('/')[:-2]) + '/'
	args = args[0]
	
	lst = list(map(radek, load_json(path + "./data.json")))
	
	pretty_print(lst)

if __name__ == "__main__":
	main(sys.argv[0], sys.argv[1:])
