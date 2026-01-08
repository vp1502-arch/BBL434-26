#!/usr/bin/env python3

import sys
from Bio import SeqIO

# -----------------------------
# CHECK ARGUMENTS
# -----------------------------
if len(sys.argv) != 2:
    sys.exit("Usage: python3 fasta_length.py <fasta_file>")

fasta_file = sys.argv[1]

# -----------------------------
# PARSE FASTA FILE
# -----------------------------
try:
    record = next(SeqIO.parse(fasta_file, "fasta"))
except FileNotFoundError:
    sys.exit(f"Error: File '{fasta_file}' not found")
except StopIteration:
    sys.exit("Error: FASTA file is empty")

# -----------------------------
# OUTPUT SEQUENCE LENGTH
# -----------------------------
seq_length = len(record.seq)
print(seq_length)
