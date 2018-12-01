import sys
import json
import subprocess

def load_json(path):
	with open(path, "r") as j:
		return json.load(j)
		
def save_json(data, path):
	with open(path, "w") as j:
		json.dump(data, j)
		
def option_by_flag(flag, options):
	for option in options:
		if option["flag"] == '-' + flag:
			return option
	return None

def main(s_path, e_path, *args):
	path = s_path
	path = '/'.join(path.split('/')[:-1])
	args = args[0]

	print(path)	
	#print("path:\t", path, "\nargs:\t", args, "\nresults: ", end='')
	
	default, *options = load_json(path + "/.options/options.json")
	
	args2 = []
	skip = False
	
	for arg in args:
		if not skip:
			if arg[0] == '-':
				flags = arg[1:-1]
				last_flag = arg[-1]
				
				for flag in flags:
					option = option_by_flag(flag, options)
					if option != None:
						if option["args"] == "False":
							args2.append([option["program"], option["file"]])
							
				option = option_by_flag(last_flag, options)
				if option != None:
					args2.append([option["program"], option["file"]])
					if option["args"] == "False":
						break
					skip = True
		else:
			args2[-1].append(arg)
			
	if len(args2) == 0:
		args2.append([default["program"], default["file"]])
		
	#print(args2)
			
	for arg2 in args2:
		subprocess.call([arg2[0], path + "/.options/" + arg2[1], ' '.join(arg2[2:])])
		
	
	#save_json(a, path + "/options.json")
	
	
	

if __name__ == "__main__":
	main(*sys.argv)
