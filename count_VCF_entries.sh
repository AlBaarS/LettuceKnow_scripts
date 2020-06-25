dir="/hpc/uu_pmi/alejandro/SOBIR1-like_A_vcf_snps_indel"

echo "#Sample,Total_entries,SNPs,Others,Low_effect,Medium_effect,High_effect,Modifier"

for vcf in $dir/* ; do
	name=`echo $(basename $vcf .full.vcf)`
	entries=`cat $vcf | grep -v '#' | wc -l`
	SNPs=`cat $vcf | grep -v '#' | grep -E '*SNP*|*Snp*|*snp*' | wc -l`
	misc=`expr $entries - $SNPs`
	low=`cat $vcf | grep -v '#' | grep -F '|LOW|' | wc -l`
	med=`cat $vcf | grep -v '#' | grep '|MODERATE|' | wc -l`
	hi=`cat $vcf | grep -v '#' | grep '|HIGH|' | wc -l`
	mod=`cat $vcf | grep -v '#' | grep '|MODIFIER|' | wc -l`
	echo $name,$entries,$SNPs,$misc,$low,$med,$hi,$mod
done

