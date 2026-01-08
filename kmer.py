#!/usr/bin/env python3

import sys
from Bio import SeqIO

# -----------------------------
# CHECK ARGUMENTS
# -----------------------------
if len(sys.argv) != 3:
    sys.exit("Usage: python3 kmer_count.py <fasta_file> <k>")

fasta_file = sys.argv[1]
k = int(sys.argv[2])

# -----------------------------
# PARSE FASTA FILE (SINGLE RECORD)
# -----------------------------
try:
    record = next(SeqIO.parse(fasta_file, "fasta"))
except FileNotFoundError:
    sys.exit(f"Error: File '{fasta_file}' not found")
except StopIteration:
    sys.exit("Error: FASTA file is empty")

sequence = str(record.seq).upper()
seq_len = len(sequence)

if k <= 0 or k > seq_len:
    sys.exit("Error: k must be > 0 and <= sequence length")

# -----------------------------
# K-MER COUNTING
# -----------------------------
kmer_counts = {}

for i in range(seq_len - k + 1):
    kmer = sequence[i:i + k]
    kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1

# -----------------------------
# OUTPUT
# -----------------------------
print(f"Sequence length : {seq_len}")
print(f"k-mer length    : {k}")
print(f"Unique k-mers   : {len(kmer_counts)}\n")

print("k-mer\tCount")
print("-" * 20)

for kmer, count in sorted(kmer_counts.items()):
    print(f"{kmer}\t{count}")
