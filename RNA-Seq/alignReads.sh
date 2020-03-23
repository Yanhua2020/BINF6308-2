#!/usr/bin/env bash
# alignReads.sh
nice -n19 gsnap \
            -A sam \
            -D . \
            -d AiptasiaGmapDb \
            -s AiptasiaGmapIIT.iit \
             /Paired/Aip02.R1.paired.fastq \
             Aip02.R2.paired.fastq \
             1>Aip02.sam
alignReads 1>alignReads.log 2>alignReads.err &
