from Bio import SeqIO
from Bio.Seq import Seq
import re

with open("Seq_coding.fasta") as handle:
    newRecords = []
    for record in SeqIO.parse(handle, "fasta"):
        genesMito = record.description.split()[1].split("=")[1].split("]")[0]
        if genesMito == "nd1" or genesMito == "ND1" :
            newRecords.append(record)

    SeqIO.write(newRecords, "nd1.fasta", "fasta")