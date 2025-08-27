# Project Title: DNA Toolkit (Python CLI)
#
# This Python script provides a command-line interface (CLI) tool to perform
# common bioinformatics tasks on DNA sequences. This project showcases proficiency
# in Python scripting, handling biological data formats (like FASTA), and
# creating a user-friendly command-line application.
#
# This project is highly relevant to a biomedical sciences background, as it
# demonstrates the ability to apply programming skills to a scientific problem.

import re
import sys

# Function to read a FASTA file and return a dictionary of sequences
def read_fasta(file_path):
    """
    Reads a FASTA file and returns a dictionary where keys are sequence headers
    and values are the DNA sequences.
    """
    sequences = {}
    current_header = None
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                current_header = line[1:].split()[0]
                sequences[current_header] = ''
            else:
                sequences[current_header] += line
    return sequences

# Function to calculate GC content (percentage of G and C bases)
def calculate_gc_content(sequence):
    """
    Calculates the percentage of Guanine (G) and Cytosine (C) bases in a DNA sequence.
    """
    gc_count = sequence.upper().count('G') + sequence.upper().count('C')
    total_bases = len(sequence)
    if total_bases == 0:
        return 0
    return (gc_count / total_bases) * 100

# Function to search for a specific motif (a pattern) in a sequence
def find_motifs(sequence, motif):
    """
    Searches for all occurrences of a given motif in a DNA sequence and returns
    a list of their starting positions.
    """
    return [match.start() for match in re.finditer(f'(?={motif.upper()})', sequence.upper())]

def main():
    """
    The main function to run the CLI tool.
    """
    # The script expects at least two command-line arguments: the script name and a command.
    if len(sys.argv) < 2:
        print("Usage: python dna_toolkit.py <command> [arguments]")
        print("Commands:")
        print("  gc <fasta_file>")
        print("  find_motif <fasta_file> <motif>")
        return

    command = sys.argv[1]

    if command == 'gc':
        if len(sys.argv) < 3:
            print("Usage: python dna_toolkit.py gc <fasta_file>")
            return
        fasta_file = sys.argv[2]
        sequences = read_fasta(fasta_file)
        if not sequences:
            print("No sequences found in file.")
            return
        print("GC Content:")
        for header, sequence in sequences.items():
            gc_percentage = calculate_gc_content(sequence)
            print(f"  {header}: {gc_percentage:.2f}%")

    elif command == 'find_motif':
        if len(sys.argv) < 4:
            print("Usage: python dna_toolkit.py find_motif <fasta_file> <motif>")
            return
        fasta_file = sys.argv[2]
        motif = sys.argv[3]
        sequences = read_fasta(fasta_file)
        if not sequences:
            print("No sequences found in file.")
            return
        print(f"Searching for motif '{motif}'...")
        for header, sequence in sequences.items():
            positions = find_motifs(sequence, motif)
            if positions:
                print(f"  Motif found in {header} at positions: {positions}")
            else:
                print(f"  Motif not found in {header}.")

    else:
        print(f"Unknown command: {command}")
        print("Available commands: gc, find_motif")

if __name__ == '__main__':
    main()
