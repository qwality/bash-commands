import sys
import json

def load_json(path):
	with open(path, "r") as j:
		return json.load(j)
		
def radek(dct):
	return [dct["flag"], "something" if dct["args"] == "True" else "", dct["file"]]
	
def pretty_print(data):
	widths = [0 for x in range(max(len(row) for row in data))]
	for r in range(len(data)):
		for c in range(len(data[r])):
			if len(data[r][c]) > widths[c]:
				widths[c] = len(data[r][c])
	
	for row in data:
		print("".join(row[i].ljust(widths[i] + 2) for i in range(len(row))))

def main(p_path, path, e_path, *args):
	#print("python-help-path:   ", path)
	#print("python-help-e_path: ", e_path)
	#print("python-help-args:   ", list(args))
	
	lst = list(map(radek, load_json(path + "/.options/options.json")))
	
	pretty_print(lst)

if __name__ == "__main__":
	main(*sys.argv)
