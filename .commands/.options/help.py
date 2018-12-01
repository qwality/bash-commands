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

def main(path, *args):
	path = '/'.join(path.split('/')[:-2]) + '/'
	args = args[0]
	
	lst = list(map(radek, load_json(path + ".options/options.json")))
	
	pretty_print(lst)

if __name__ == "__main__":
	main(sys.argv[0], sys.argv[1:])
