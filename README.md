# LettuceKnow_scripts
Just some scripts I use/have used to extract my data

# Descriptions:
## filter_RLP_RLK.py:
This script I used to extract my genes of interest (RLKs/RLPs) from InterProScan data in tsv format. Currently in the final testing stage.
The domain selection was based on "Genome assembly with in vitro proximity ligation data and whole-genome triplication in lettuce" by Sebastian Reyes-Chin-Wo et. al. (Nature comm., 2017) and manually searching the InterPro database. The domains selected were globally researched for the kind of organisms they appeared in and in what kind of genes, so it was not completely arbitrary.

## select_domains.py
This script is the predecessor of filter_RLP_RLK.py, which I made on my desktop rather than on the HPC to extract from pre-organised data.

## gff2bed.py
Does what it says on the tin...
