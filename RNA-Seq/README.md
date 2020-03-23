# Short Read Alignment

## Yanhua Gao

#  Methods

#The experiment was designed to study immune response and symbiosis of the sea anemones, Aiptasis pallida[1]. In the beginning of the experiment, 24 sea anemones  were randomly collected (four treatments each with six replicates). In order to identify the difference in the gene expression level, the  gnomic reading of the tested sea anemones  were analyzed using RNA-Seq aligner.  

#In this class exercise, we chose to use a set of QC sequencing results instead of the full data set. There were a total of four coding exercises included. The first one is a class demonstration, which was used to trim the raw data using Trimmomatic [2]. Trimmomatic is a quality based trimmer, which can remove not only low quality score reads but also adapter sequences. Based on the setting of this class, no base pair needs to be removed from the beginning of the reads regardless of  the quality. The minimum quality for trimming the start and end of reads were set to be 20.  The second part of this exercise is the alignment.  “aligAll.sh” should run gsnap for every paired trimmed files result from the previous step and out put the sam files to the same directory. The GMAP database was also extracted using shell scrip from the previous exercise of this week.  In the two steps, the aligned sam files were sorted and indexed with samtools in BAM format. 

#1. Sweeney, T. (2020). Module 4: Biopython. [Gitbook slides] Retrieved February 20, 2020, from https://app.gitbook.com/@bioinformatics/s/binf6308/module_6/module_6_practice

#2. Bolger, A. M., Lohse, M., & Usadel, B. (2014). Trimmomatic: A flexible trimmer for Illumina Sequence Data. Bioinformatics, btu170 
