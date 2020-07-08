# LettuceKnow_scripts
Just some scripts I use/have used to extract my data

# Descriptions:
## calculateRawDepth.R
Processed the depth for my gene of interest. Depth was calculated with samtools depth for BAM files for my gene of interest for each position (base) within that gene. Then, depth for every position was divided by the average depth from the whole BAM file for that sample, to compensate for sample differences.

## count_VCF_entries.sh
Counts all VCF entries in a given VCF file by counting the number of lines that do not have a '#'. Then, it also searches within those lines whether they contain SNP/Snp/snp to count the number of SNPs. Finally, it subtracts the amount of SNPs from the total amount of lines to calculate the number of alternative variants. It prints the sample and the calculated numbers in a csv format

## filter_RLP_RLK.py:
This script I used to extract my genes of interest (RLKs/RLPs) from InterProScan data in tsv format. Currently in the final testing stage.
The domain selection was based on "Genome assembly with in vitro proximity ligation data and whole-genome triplication in lettuce" by Sebastian Reyes-Chin-Wo et. al. (Nature comm., 2017) and manually searching the InterPro database. The domains selected were globally researched for the kind of organisms they appeared in and in what kind of genes, so it was not completely arbitrary.

## gff2bed.py
Does what it says on the tin...

## label2pass.py
There was an annoying issue in my VCF files that they had a label "SnpCluster", which caused GATK to skip these variants when generating alternative coding sequences. This python script will take an arbitrary label as input and a file, and will make a new copy of that file where that label has been changed to PASS. This script has been written with argparse, so it can be used by others as well with no modifications.

## sample2species.py
In the later stages of my project, I want to change the sample IDs for species name. So I wrote a script to do that for me, rather than manually re-writing 100 names per file. It takes an input file, a csv file with the sample IDs and species name and an output directory to paste the new file into (the old file is not affected). It can either replace the label or keep the label, but paste the species in front of it, seperated by an underscore, which is convenient if you have more samples per species (like I do).

## stats_RLP_RLK.py
Generate some statistics on my selected RLPs and RLKs (my genes of interest)
