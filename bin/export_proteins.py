#!/usr/bin/env python3

from Bio import SeqIO
import sys
import os

#basic_args
input_file = sys.argv[1]
#script
output_name = input_file.split(".")[0].strip("_")

for seq_record in SeqIO.parse(input_file , 'genbank'):
    with open(output_name+".fasta", "w") as protein_fasta:
        with open(output_name+"_hypothetical_proteins"+".fasta", "w") as hypothetical_fasta:
            for feature in seq_record.features:
                if feature.type == "CDS" and "hypothetical" in feature.qualifiers['product'][0]:
                    protein_locus = feature.qualifiers['locus_tag'][0]
                    protein_name = feature.qualifiers['product'][0]
                    protein_sequence = feature.qualifiers['translation'][0]            
                    hypothetical_fasta.write(">{0}|{1}\n{2}\n".format(protein_locus,protein_name,protein_sequence))
                if feature.type == "CDS" and "hypothetical" not in feature.qualifiers['product'][0]:
                    protein_locus = feature.qualifiers['locus_tag'][0]
                    protein_name = feature.qualifiers['product'][0]
                    protein_sequence = feature.qualifiers['translation'][0]            
                    protein_fasta.write(">{0}|{1}\n{2}\n".format(protein_locus,protein_name,protein_sequence))

