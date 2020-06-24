## load libraries
library("R.utils")
library("dplyr")
library("ggplot2")
library("tidyr")
library("tibble")
library("matrixStats")

## import first data
files <- list.files(path="/hpc/uu_pmi/alejandro/SOBIR1_like_A_depth/", pattern="*.depth", full.names=TRUE, recursive=FALSE)
tmp <- list.files(path="/hpc/uu_pmi/alejandro/SOBIR1_like_A_depth/", pattern="*.depth", full.names=FALSE, recursive=FALSE)
filenames <- substr(sapply(strsplit(tmp, "_", fixed=TRUE), "[", 1), 1,100)
rm(tmp)
len <- countLines(files[1])
pos <- seq(1,len)
depth_df <- read.table(text = "", col.names=pos)
full_averages <- read.table("/hpc/uu_pmi/alejandro/Lsativa_full.depth")
full_avr_vector <- pull(full_averages[4])

## load data into dataframe
for (i in 1:length(files)) {
tmp_df <- read.table(file=files[i], sep="\t",header=FALSE)
tmp_vec <- pull(tmp_df[3])
tmp_vec <- tmp_vec / full_avr_vector[i]
add_df <- as.data.frame(t(tmp_vec))
colnames(add_df) <- pos
rownames(add_df) <- filenames[i]
depth_df <- rbind(depth_df, add_df)
}

## data prep for generating heatmap
depth_long <- pivot_longer(data=depth_df, cols=everything(), names_to="Position", values_to="Depth")
filenames_2065x <- rep(filenames, each=2065)
depth_long <- add_column(depth_long, Sample = filenames_2065x, .before = 1)
depth_long <- transform(depth_long, Position = as.numeric(Position))

## generating the actual heatmap
depth.heatmap <- ggplot(data = depth_long, mapping = aes(x = Position, y = Sample, fill = Depth)) +
geom_tile() +
xlab(label = "Position in the gene") +
ylab(label = "Sample")

## saving plot
ggsave(filename = "Lsativa_SOBIR1L_depth.png", plot = depth.heatmap, device = png(), path = "/hpc/uu_pmi/alejandro/", width = 8, height = 11)

## stats *** WIP ***
depth_stats <- data.frame(Means=rowMeans(depth_df[,-1]),StDev=rowSds(as.matrix(depth_df[,c(-1)])))
depth_stats <- tibble::rownames_to_column(depth_stats, "Samples")
write.table(depth_stats, "/hpc/uu_pmi/alejandro/SOBIR1L_depth_mean_stdev.csv", quote=FALSE, sep=",", row.names=FALSE)

ref_sample <- as.numeric(as.vector(depth_df[98,]))
depth_Pval <- read.table(text = "", col.names="P-value")