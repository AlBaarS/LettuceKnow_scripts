dir="/hpc/uu_pmi/alejandro/SOBIR1-like_A_vcf_snps_indel"

echo "#Sample,Total_entries,SNPs,Others"

for vcf in $dir/* ; do
	name=`echo $(basename $vcf .full.vcf)`
	entries=`cat $vcf | grep -v '#' | wc -l`
	SNPs=`cat $vcf | grep -v '#' | grep -E '*SNP*|*Snp*|*snp*' | wc -l`
	misc=`expr $entries - $SNPs`
	echo $name,$entries,$SNPs,$misc
done

