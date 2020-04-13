# getDomains.sh
cut -f13 proteins.tsv | sort | uniq > domains.txt
