#!/usr/bin/env bash
quast.py
nice -n19 /usr/bin/quast.py \
Rhodo/contigs.fasta \
-o quast \
1>quast.log 2>quast.err &
