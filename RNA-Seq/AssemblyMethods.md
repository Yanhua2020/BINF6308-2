# AssemblyMethods.md

## Yanhua Gao

# There are two ways to preform transcriptome assembly. When a  transcriptome for the organism from which the obtain RNA-seq reads exist, a reference-guided trnscriptome assembly can be preformed. When a reference transcriptome does not exist or in sufficient, a de-novo transcriptome assembly will be chosen. 

# In this case, we chose to use Trinity for both reference-guide and de-novo assemblies. For the reference-guide assembly, we used two scrips.  Script, MergeAll.sh, was used to merge all individual bam files into a single sorted bam file.   Script, runTrinity.sh, was used to read the single merged bam file into a transcriptome.  To check the assembly statistics, we ran TrinityStats.pl with the assembled transcriptome  result as input using script analyzeTrinity.sh. 

# For de-novo assembly, trinity requires two separated list of files as input. Therefore, script trinityDeNovo1.sh created two lists of files for the left and right reads.  Script, trinityDeNovo.sh, is a modified version of script trinityDeNovo1.sh by adding the trinity de-novo command. To check the de-novo assembly statistics, we ran Trinity Stats.pl  again but using the de-novo assembly result as input. 



