#!/usr/bin/env bash
# spades.sh

nice -n19 /usr/local/programs/SPAdes-3.10.0-Linux/bin/spades.py \
-o Rhodo \
-1 Paired/SRR522244_1.fastq \
-2 Paired/SRR522244_2.fastq \
-t 4 \

1>spades.log 2>spades.err &


