#!/usr/bin/env bash
# indexAll.sh 
# Initialize variable to contain the directory of un-trimmed fastq files 
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
# Initialize variable to contain the suffix for the left reads
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
pairedOutPath="Paired/"
unpairedOutPath="Unpaired/"
baiSuffix=" .bai"
bamSuffix=" .sorted.bam"
bamfilePath=" bam/"
# Loop through all the left-read fastq files in $fastqPath
#function indexAll 
for leftInFile in $fastqPath*$leftSuffix
do
# Remove the path from the filename and assign to pathRemoved
               pathRemoved="${leftInFile/$fastqPath/}"
# Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
               sampleName="${pathRemoved/$leftSuffix/}"
# Print $sampleName to see what it contains after removing the path
               echo $sampleName
               samtools index $bamfilePath$sampleName.sorted.bam
done

1>indexAll.log 2>indexAll.err &

