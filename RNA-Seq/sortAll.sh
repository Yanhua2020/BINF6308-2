#!/usr/bin/env bash
# sortAll.sh
# Initialize variable to contain the directory of un-trimmed fastq files 
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
# Initialize variable to contain the suffix for the left reads
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"alignSuffix
pairedOutPath="Paired/"
unpairedOutPath="Unpaired/"
bamfilePath="bam/"
bamSuffix=".sorted.bam"
samfilepath="sam/"
alignSuffix=".sam" 
#Create the output directories
mkdir -p $bamfilePath
# Loop through all the left-read fastq files in $fastqPath
#function sortAll 
for leftInFile in $fastqPath*$leftSuffix
do
# Remove the path from the filename and assign to pathRemoved
         pathRemoved="${leftInFile/$fastqPath/}"
# Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
         sampleName="${pathRemoved/$leftSuffix/}"
   # Print $sampleName to see what it contains after removing the path
         echo $bamfilePath$sampleName
         samtools sort $samfilepath$sampleName$alignSuffix -o $bamfilePath$sampleName$bamSuffix

done

1>sortAll.log 2>sortAll.err &
                                                                                                                   
