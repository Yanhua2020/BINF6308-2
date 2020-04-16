#!/usr/bin/env bash
#removeStop.sh

sed 's/*//' ../BLAST/Trinity.fasta.transdecoder.pep > output.fasta
head output.fasta -n 500 > proteins.fasta
