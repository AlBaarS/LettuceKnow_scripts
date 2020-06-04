# files
inp = open("/hpc/uu_pmi/alejandro/InterProScan_sorted.tsv","r")
out = open("/hpc/uu_pmi/alejandro/InterProScan_filter.tsv","w")
rep = open("/hpc/uu_pmi/alejandro/InterProScan_report.txt","w")

# prepare output
out.write("# geneID" + "\t" + "type" + "\t" + "length" + "\t" + "extracellular_domain" + "\t" + "annotations" + "\n")
rep.write("Report showing some statistics regarding the selection of RLPs and RLKs\n\n")

# lists & variables

dom_names = ["LRR","Lysin Motif","L-type Lectin","B-type Lectin","C-type Lectin","Malectin","GNK2-homologous","Thaumatin","Chitinase","EGF-repeat","SERK","PAN","TNFR"]
dom_dict = {"LRR":0,"Lysin Motif":0,"L-type Lectin":0,"B-type Lectin":0,"C-type Lectin":0,"Malectin":0,"GNK2-homologous":0,"Thaumatin":0,"Chitinase":0,"EGF-repeat":0,"SERK":0,"PAN":0,"TNFR":0}
out_lst = []

# analysis
y = 0
rlp_raw = 0
rlk_raw = 0
rlp_new = 0
rlk_new = 0
for line in inp:
	y += 1
	if "RLP" in line:
		rlp_raw += 1
	elif "RLK" in line:
		rlk_raw += 1
	for x in range(0,13):
		if dom_names[x] in line:
			out_lst.append(line)
			dom_dict[str(dom_names[x])] += 1
out_lst = sorted(list(set(out_lst)))
for n in out_lst:
	if "RLP" in n:
		rlp_new += 1
	elif "RLK" in n:
		rlk_new += 1
	out.write(n)
out.close()

# create report
for key,value in dom_dict.items():
	print("There are " + str(value) + " proteins with the " + key + " extracellular domain.")
	rep.write("There are " + str(value) + " proteins with the " + key + " extracellular domain.\n")
rep.write("\nIn the raw, sorted file there are " + str(y) + " selected proteins, of which " + str(rlp_raw) + " are RLPs and " + str(rlk_raw) + " are RLKs.\n")
print("In the raw, sorted file there are " + str(y) + " selected proteins, of which " + str(rlp_raw) + " are RLPs and " + str(rlk_raw) + " are RLKs.")
rep.write("\nIn the filtered file there are " + str(len(out_lst)) + " selected proteins, of which " + str(rlp_new) + " are RLPs and " + str(rlk_new) + " are RLKs.\n")
print("In the filtered file there are " + str(len(out_lst)) + " selected proteins, of which " + str(rlp_new) + " are RLPs and " + str(rlk_new) + " are RLKs.")
