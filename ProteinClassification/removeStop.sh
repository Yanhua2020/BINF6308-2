#!/usr/bin/env bash
#removeStop.sh

sed 's/*//' ../BLAST/Trinity.fasta.transdecoder.pep > output.fasta
head output.fasta -n 500500500500500 > proteins.fasta
