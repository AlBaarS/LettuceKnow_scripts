import argparse
l2p = argparse.ArgumentParser(prog="Label2PASS", usage="python3 label2pass.py --input_vcf [vcf] --label [label] --filter_lowqual", description="Change an arbitrary label to PASS in VCF files. Outputs to stdout.")

l2p.add_argument("--input_vcf","-i",
		action="store",
		help="Specify the path to your input file (1 file per run!)")
l2p.add_argument("--label","-l",
		action="store",
		help="Label to change to 'PASS'")
l2p.add_argument("--filter_lowqual","-f",
		action="store_true",
		help="Filter out lines with the 'LowQual' tag")

namespace = l2p.parse_args()
vcf = str(namespace.input_vcf)
lbl = str(namespace.label)
lq = bool(namespace.filter_lowqual)

with open(vcf,"r") as file:
	for line in file:
		if "#" in line:
			print(line.strip("\n"))
		elif "#" not in line:
			if lq:
				if "LowQual" not in line:
					if lbl in line:
						newline = line.replace(lbl, "PASS")
						print(newline.strip("\n"))
			else:
				if lbl in line:
					newline = line.replace(lbl, "PASS")
					print(newline.strip("\n"))
		else:
			print(line.strip("\n"))
