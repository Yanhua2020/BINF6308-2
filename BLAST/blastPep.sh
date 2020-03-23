#!/usr/bin/env bash
# blastPep.sh
blastp -query Trinity.fasta.transdecoder_dir/longest_orfs.pep  \
        -db swissprot  -max_target_seqs 1 \
        -outfmt 6 -evalue 1e-5 -num_threads 4 1> blastp.outfmt6 \
        2>blastp.err &
