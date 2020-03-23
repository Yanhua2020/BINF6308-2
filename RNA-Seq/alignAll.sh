#!/usr/bin/env bash
# alignAll.sh
# Initialize variable to contain the directory of un-trimmed fastq files 
fastqPath="/scratch/AiptasiaMiSeq/fastq/"
# Initialize variable to contain the suffix for the left reads
leftSuffix=".R1.fastq"
rightSuffix=".R2.fastq"
pairedOutPath="Paired/"
unpairedOutPath="Unpaired/"
samfilePath="sam/"
samSuffix=".sam"
mkdir -p $samfilePath
# Loop through all the left-read fastq files in $fastqPath
function alignAll 
for leftInFile in $fastqPath*$leftSuffix
do
# Remove the path from the filename and assign to pathRemoved
       pathRemoved="${leftInFile/$fastqPath/}"
       echo $pathRemoved
# Remove the left-read suffix from $pathRemoved and assign to suffixRemoved
       sampleName="${pathRemoved/$leftSuffix/}"
# Print $sampleName to see what it contains after removing the path
       echo $sampleName
       nice -n19 gsnap \
       -A sam \
       -D . \
       -d AiptasiaGmapDb \
       -s AiptasiaGmapIIT.iit \
       $pairedOutPath$sampleName$leftSuffix \
       $pairedOutPath$sampleName$rightSuffix \
       1>$samfilePath$sampleName$samSuffix
done

alignAll 1>alignAll.log 2>alignAll.err &




