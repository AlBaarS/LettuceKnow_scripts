import argparse, re

# arguments
s2s = argparse.ArgumentParser(prog="Sample2Species", usage="python3 sample2species.py --samples [samples.csv] --input [file.txt] --outdir [path/to/output/directory] --keepSample")

s2s.add_argument('--samples', '-s',
		action='store',
		help="Specify a .csv file with sample IDs in the first column and name in the second. The second column must consist of two strings seperated by a whitespace "
		"(e.g. 'Homo sapiens' or 'H. sapiens')")
s2s.add_argument('--input','-i',
		action='store',
		help='File you want to add species names to.')
s2s.add_argument('--outdir','-o',
		action='store',
		help="Path to where you want your new file to go. It will have the same same plus 'renamed' in the title.")
s2s.add_argument('--keepSample','-k',
		action='store_true',
		help='If specified, will instead put the species name before the sample ID rather than replace it')

# store input
namespace = s2s.parse_args()
csv = str(namespace.samples)
input = str(namespace.input)
outdir = str(namespace.outdir)
keepSample = bool(namespace.keepSample)

# import data
samples_dict = {}
with open(csv, 'r') as in_csv:
	for line in in_csv:
		tmp = re.split(',|\n',line)
		tmp_sp = tmp[1].split(' ')
		species = str(tmp_sp[0] + '_' + tmp_sp[1])
		samples_dict[tmp[0]] = species

# prepare output
input_list = re.split('/', input)
filename = input_list[-1]
filename_list = filename.split('.')
filename_list.insert(-1, '_renamed.')
newfilename = ""
newfilename = newfilename.join(filename_list)

out = open(str(outdir + '/' + newfilename), 'w')

# find matches in input & adapt string
with open(input, 'r') as data:
	for line in data:
		line_new = ""
		for k, v in samples_dict.items():
			line_split = line.split(',')
			if k == line_split[0]:
				if keepSample:
					inserttxt = str(v + '_')
					idx = line.index(k)
					line_new = line[:idx] + inserttxt + line[idx:]
				else:
					line_new = line.replace(k, v)
			elif k != line_split[0]:
				if line_new == "":
					line_new = line
		out.write(line_new)
out.close()
