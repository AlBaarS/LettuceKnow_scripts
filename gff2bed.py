gff = open("/hpc/uu_pmi/alejandro/Lsativa_genes.gff","r")
out = open("/hpc/uu_pmi/alejandro/Lactuca_sativa_lettuce_GENES.bed","w")
out.write("#chrom\tchromStart\tchromEnd\n")
out.close()
for line in gff:
	if '#' not in line:
		data = line.split("\t")
		newline = str(data[0]) + "\t" + str(data[3]) + "\t" + str(data[4])
		with open("/hpc/uu_pmi/alejandro/Lactuca_sativa_lettuce_FULL.bed","a") as out:
			out.write(newline + "\n")
