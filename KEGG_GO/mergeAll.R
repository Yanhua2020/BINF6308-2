#!/usr/bin/env Rscript
# mergeAll.R

# Load BLAST results as a table using tab (\t) as separator.
# There is no header with column names, so set header=FALSE
blast <- read.table("../BLAST/alignPredicted.txt", sep="\t", header=FALSE)
# Set column names to match fields selected in BLAST
colnames(blast) <- c("qseqid", "sacc", "qlen", "slen",
                         "length", "nident", "pident", "evalue", "stitle")
# Calculate the coverage as nident/slen
blast$cov <- blast$nident/blast$slen
# Select only blast rows where coverage is greater than .9
blast <- subset(blast, cov > .9, select=-c(stitle))
# Read kegg.txt, produced by get_kegg_ids, as a table
kegg <- read.table("kegg.txt", sep="\t", header=FALSE)
# Set the column names for kegg
colnames(kegg) <- c("sacc", "kegg")
# Remove the up: prefix from the accession number so it will match the BLAST
# subject accession (sacc)
kegg$sacc <- gsub("up:", "", kegg$sacc)
# Merge the tables. Since one column name in common, just give
# the two tables as parameters to merge.
blast_kegg <- merge(blast, kegg)
# merge the KO
KO <- read.table("ko.txt", sep="\t", header=FALSE)
colnames(KO) <- c("kegg","KO")
blast_kegg_KO <-merge(blast_kegg, KO)

# merge the pathway
pathway<-read.table("koPathway.txt", sep="\t", header=FALSE)
colnames(pathway)<-c("KO","Pathway_IDs")
blast_kegg_KO_pathway<-merge(blast_kegg_KO, pathway)

# merge the pathway descriptions 
PathwayDesc<-read.table("ko",sep="\t", header=FALSE)
colnames(PathwayDesc) <- c("Pathway_IDs","Pathway_Desc")
blast_kegg_KO_pathway_PathwayDesc<-merge(blast_kegg_KO_pathway, PathwayDesc)


# merge the go file
go <- read.table("sp_go.txt", sep="\t",stringsAsFactor=FALSE, header=FALSE, fill=FALSE, quote = "")
colnames(go) <- c("sacc", "GOTerm")
mergedfile<-merge(blast_kegg_KO_pathway_PathwayDesc, go)
head (mergedfile)


#output file into a csv formate
write.table ( mergedfile, "mergedfile.tsv", row.names=FALSE, sep="\t") 







