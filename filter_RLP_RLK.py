import sys

# files
input = open("/hpc/uu_pmi/Lettuceknow_JK_hpc/Lsativa_467_v5_out.tsv","r")
IPR = input.readlines()
out = open("/hpc/uu_pmi/alejandro/InterProScan_sorted.tsv","w")
out.write("# geneID" + "\t" + "type" + "\t" + "length" + "\t" + "extracellular_domain" + "\t" + "annotations")
out.close()

# empty lists
protID = []

# annotations
LRR = ["IPR031071","IPR000372","IPR001611","IPR032675","IPR006553","IPR011713","IPR013101","IPR013210","IPR032675","IPR041283"]
LysM = ["IPR018392","IPR036779"]
L_Lec = ["IPR001220","IPR016363","IPR019825","IPR000985"]
B_Lec = ["IPR001480","IPR036426"]
C_Lec = ["IPR001304","IPR016186","IPR016187","IPR018378"]
Malectin = ["IPR021720","IPR024788"]
GNK2_homologous = ["IPR002902","IPR038408"]
Thaumatin = ["IPR001938","IPR017949","IPR037176"]
Chitinase = ["IPR009470","IPR011583","IPR029070"]
EGF_rep = ["IPR000742","IPR013032","IPR013111"]
SERK = ["IPR031048"]
PAN = ["IPR003609","IPR006583"]
TNFR = ["IPR001368"]

# essentials
KIN = ["IPR000719","IPR001245","IPR022126","IPR020635","IPR021820","IPR017892"]
TM = "TRANSMEMBRANE"
SP = "SIGNAL_PEPTIDE"

# first we filter all protein ID's as there are more lines per protein
for line in IPR:
	lin = line.split("\t")
	protID.append(lin[0])
tmp = set(protID)
protID = list(tmp)
print("Total proteins: " + str(len(protID)))

# then we filter our annotations from the input
x = 0
y = 0
z = 0
p = 0

dom = [LRR,LysM,L_Lec,B_Lec,C_Lec,Malectin,GNK2_homologous,Thaumatin,Chitinase,EGF_rep,SERK,PAN,TNFR]
dom_names = ["LRR","Lysin Motif","L-type Lectin","B-type Lectin","C-type Lectin","Malectin","GNK2-homologous","Thaumatin","Chitinase","EGF-repeat","SERK","PAN","TNFR"]

for id in protID:
	tm = False
	sp = False
	kin = False
	lst = []
	ann_hit = []
	name_hit = []
	p += 1
	for line in IPR:
		if id in line:
			if TM in line:
				x += 1
				tm = True
			elif SP in line:
				y += 1
				sp = True
			for k in KIN:
				if k in line:
					z += 1
					kin = True
	if tm == True:
		if sp == True:
			lst.append(line)
	# with the proteins with a signal peptide and transmembrane domain selected, now we need to select the extracellular domains
	length = ""
	for lin in lst:
		tmp = lin.split("\t")
		for m in tmp:
			for x in range(0,13):
				for n in dom[x]:
					if n in m:
						ann_hit.append(n)
						name_hit.append(dom_names[x])
		length = tmp[2]
	ann_hit = list(set(ann_hit))
	name_hit = list(set(name_hit))
	type = ""
	if kin == True:
		type = "RLK"
	elif kin == False:
		type = "RLP"
	with open("/hpc/uu_pmi/alejandro/InterProScan_sorted.tsv","a") as out:
		out.write("\n" + id + "\t" + type + "\t" + length + "\t" + str(name_hit) + "\t" + str(ann_hit))

# print stats
print(str(p) + " proteins in total")
print(str(x) + " proteins with a transmembrane domain.")
print(str(y) + " proteins with a signal peptide.")
print(str(z) + " proteins with a kinase domain.")
print(str(len(rlk_raw)) + " proteins with a signal peptide, transmembrane and kinase domain.")
print(str(len(rlp_raw)) + " proteins with a signal peptide, transmembrane domain but without a kinase domain.")
