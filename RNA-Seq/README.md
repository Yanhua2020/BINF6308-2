# Short Read Alignment

## Yanhua Gao

#  Methods

#This module precise includes four coding excises. The data came from a experiment which was designed to study immune response and symbiosis of the sea anemones, Aiptasis pallida (Sweeney, 2020). In the beginning of the experiment, 24 sea anemones were randomly collected (four treatments each with six replicates). In order to identify the difference in the gene expression level, the gnomic reading of these 24 selected sea anemones were analyzed using RNA-Seq aligner.

#To reduce the computational time, we chose to use a set of QC sequencing results instead of the full data set. The first scrip was a class demonstration, named **trimAll.sh**, which was used to trim the raw data using Trimmomatic (Bolger, 2014). Trimmomatic is a quality based trimmer, which can remove not only low quality score reads but also adapter sequences. Based on the setting of this class, no base pair needed to be removed from the beginning of the reads regardless of the quality. The minimum quality for trimming the start and end of reads were set to be 20. 

#The second scrip is the actual alignment, **aligAll.sh**.  It ran gsnap for every paired and trimmed files coming from the first scrip and out put the result sam files into the sam directory. The third and fourth scrips for this module are named **sortAll.sh** and **indexAll.sh**. They sorted and indexed the output sam files from the previous alignment into a BAM format using samtools utility. 

#1. Bolger, A. M., Lohse, M., & Usadel, B. (2014). Trimmomatic: A flexible trimmer for Illumina Sequence Data. Bioinformatics, btu170 

#2. Sweeney, T. (2020). Module 6: Short Read Alignment. [Gitbook slides] Retrieved February 20, 2020, from https://app.gitbook.com/@bioinformatics/s/binf6308/module_6/module_6_practice



