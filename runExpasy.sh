#!/bin/bash

while IFS= read -r line
do
    if [[ $line =~ ^\>.+ ]]; then
        title=$(echo "$line")
        echo "$title" >> input.fasta
    else
        sequence=$(echo "$line" | sed 's/ACTG/'"$line"'/')
        curl -s -d "dna_sequence=$sequence&output_format=fasta&style=raw" https://web.expasy.org/cgi-bin/translate/dna2aa.cgi >> input.fasta
    fi
done < sequencias.fa
