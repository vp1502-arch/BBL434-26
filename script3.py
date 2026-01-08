#!/usr/bin/env python3

import sys
from Bio import SeqIO

# -----------------------------
# CHECK ARGUMENTS
# -----------------------------
if len(sys.argv) != 2:
    sys.exit("Usage: python3 count_headers.py <multifasta_file>")

fasta_file = sys.argv[1]

# -----------------------------
# COUNT FASTA HEADERS
# -----------------------------
try:
    count = sum(1 for _ in SeqIO.parse(fasta_file, "fasta"))
except FileNotFoundError:
    sys.exit(f"Error: File '{fasta_file}' not found")

# -----------------------------
# OUTPUT
# -----------------------------
print(count)

