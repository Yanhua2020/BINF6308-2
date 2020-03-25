# AssemblyMethods.md

## Yanhua Gao

#  Methods

#There are two ways to preform transcriptome assembly. When a transcriptome for the organism from which the obtain RNA-seq reads exist, a reference-guided transcriptome assembly can be preformed (Sweeney, 2020). When a reference transcriptome does not exist or in sufficient, a de-novo transcriptome assembly will be used.

#In this case, we chose to use Trinity software (“ RNA-Seq Denovo Assembly Using Trinity”, 2018) for both reference-guide and de-novo transcriptome assemblies. For the reference-guide assembly, we wrote two scripts. The first script ** MergeAll.sh** was used to merge all individual bam files, which were the output from the previous module, into a single sorted bam file. The second script **runTrinity.sh** was used to read the single merged bam file output from the first script into a transcriptome. To check the assembly statistics, we ran TrinityStats.pl with the assembled transcriptome result as input using the script **analyzeTrinity.sh**.

#For de-novo transcriptome assembly, Trinity required two separated list of files as input. Therefore, script **trinityDeNovo1.sh** modified the created two lists of files for the left and right reads. Script **trinityDeNovo.sh** was a modified version of script **trinityDeNovo1.sh** by adding the trinity de-novo command. To check the de-novo assembly statistics, we ran TrinityStats.pl again but using the de-novo assembly result as input.

#1. Sweeney, T. (2020). Module 7: Transcriptome Assembly. [Gitbook slides] Retrieved February 20, 2020, from https://app.gitbook.com/@bioinformatics/s/binf6308/module_7/module_7_practice

#2. RNA-Seq Denovo Assembly Using Trinity ( 2018, April) Retrieved February 30, 2020, from https://github.com/trinityrnaseq/trinityrnaseq/wiki
