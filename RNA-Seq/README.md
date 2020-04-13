# Short Read Alignment

### author: Yanhua Gao

#  Methods

### Source of data

The data came from a experiment which was designed to study immune response and symbiosis of the sea anemones, Aiptasis pallida [[3]](#3). In the beginning of the experiment, 24 sea anemones were randomly collected (four treatments each with six replicates). In order to identify the difference in the gene expression level, the genomic reading of these 24 selected sea anemones were analyzed by aligning their RNA sequence against the built GMAP database [[3]](#3). To reduce the computational time, a set of QC sequencing results instead of the full data set was chosen for this module.

### Procedure  and scrips  

The alignment includes four steps. Each step is completed by one scrip, which means a total of four scripts needed here. The first scrip is a GitBook material, named **trimAll.sh**, which is used to trim the raw data using Trimmomatic [[1]](#1). Trimmomatic is a quality based trimmer, which can remove not only low quality score reads but also adapter sequences. Based on the setting of this class, no base pair needs to be removed from the beginning of the reads regardless of the quality. Also, the minimum quality for trimming the start and end of reads is set to be 20. 

The second scrip is the actual alignment named **aligAll.sh**.  It runs gsnap, which is alignment tool, for every paired and trimmed files produced from the first scrip and outputs the result SAM files into the sam directory. After the alignment, the result SAM files need to be modified. This is because most assemblers requires SAM files to be sorted and in BAM format, which is the binary version of SAM files. Therefore,scrips **sortAll.sh** and **indexAll.sh** was created. They can sort and index the output SAM files from the previous alignment into a BAM format using samtools utility [[2]](#2).
 
#  Reference 

<a id="1">[1]</a> . Bolger, A. M., Lohse, M., & Usadel, B. (2014). Trimmomatic: A flexible trimmer for Illumina Sequence Data. Bioinformatics, btu170 

<a id="2">[2]</a> . Samtools - Documentation. (2019). Retrieved April 12, 2020, from http://www.htslib.org/doc/

<a id="3">[3]</a> . Sweeney, T. (2020). Module 6: Short Read Alignment. [Gitbook slides] Retrieved February 20, 2020, from https://app.gitbook.com/@bioinformatics/s/binf6308/module_6/module_6_practice

