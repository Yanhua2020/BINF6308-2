# AssemblyMethods.md

## Yanhua Gao

#  Methods

### After obtaining a collection of RNA-Seq reads, we often need to assemble a transcriptome from those reads (Sweeney, 2020). There are two ways to preform transcriptome assembly It all depends on if there is a reference transcriptome. When a transcriptome for the organism from which the obtain RNA-seq reads exists, a reference-guided transcriptome assembly can be preformed. When a reference transcriptome does not exist or in sufficient, a de-novo transcriptome assembly will be used. In this case, we chose to use Trinity software (“ RNA-Seq Denovo Assembly Using Trinity”, 2018) for both reference-guide and de-novo transcriptome assemblies.

### For the reference-guide assembly, we wrote two scripts. The first script ** MergeAll.sh** was used to merge all individual BAM files, which were the output from the previous  module, into a single sorted BAM file. The second script **runTrinity.sh** was used to read the single merged BAM file output from the first script into a transcriptome. To check  the assembly statistics, we ran a perl script called TrinityStats.pl with the assembled transcriptome result as input using the script **analyzeTrinity.sh**.

### The de-novo transcriptome assembly is slightly different. Trinity requires two separated list of files as input. Therefore, script **trinityDeNovo1.sh** was wrote to modified  and created two lists of files for the left and right reads. Script **trinityDeNovo.sh** was a modified version of script **trinityDeNovo1.sh** by adding the trinity de-novo command. To check the de-novo assembly statistics, we ran TrinityStats.pl again but using the de-novo assembly result as input.

#  Reference 

### 1. Sweeney, T. (2020). Module 7: Transcriptome Assembly. [Gitbook slides] Retrieved February 20, 2020, from https://app.gitbook.com/@bioinformatics/s/binf6308/module_7/module_7_practice

### 2. RNA-Seq Denovo Assembly Using Trinity ( 2018, April) Retrieved February 30, 2020, from https://github.com/trinityrnaseq/trinityrnaseq/wiki
