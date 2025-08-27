DNA Toolkit (Python CLI)
Project Overview
This is a simple command-line interface (CLI) tool designed for performing basic bioinformatics tasks on DNA sequences. The project demonstrates my foundational skills in Python programming and my ability to apply coding to solve problems in a scientific context.

FASTA Format: The toolkit works with files in FASTA format, a standard text-based format for representing nucleotide or amino acid sequences.

Skills Demonstrated:

Python Programming: Creating functions and a main execution loop for a CLI application.

File I/O: Reading and parsing data from text files (.fasta).

String Manipulation: Handling DNA sequences as strings.

Regular Expressions (re module): For advanced motif searching.

Features
This toolkit currently supports two core functions:

GC Content Calculation: Calculates the percentage of Guanine (G) and Cytosine (C) bases in a DNA sequence.

Motif Searching: Finds all occurrences of a specific short DNA pattern (motif) within a sequence.

How to Use
Prerequisites
Python 3.x installed on your system.

Running the Tool
Save the code as dna_toolkit.py on your computer.

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Commands
1. Calculate GC Content
To calculate the GC content for all sequences in a FASTA file:

python dna_toolkit.py gc your_sequence.fasta

2. Find a Motif
To search for a specific motif (e.g., "GATTACA") in a FASTA file:

python dna_toolkit.py find_motif your_sequence.fasta GATTACA

Example FASTA File
To test the script, you can create a simple text file named test_sequences.fasta with the following content:

>Sequence1
ATGCCTAGGCATCGATCGATCGATCGATCGA
TGCATGCATGCATGCATGCATGCATGCATGC
>Sequence2
AGATTACAGATTACAGATTACAGATTACA
AGATTACAGATTACAGATTACAGATTACA

Then, you can run the commands using this file as the input.

Future Improvements
Adding a function to calculate the reverse complement of a DNA sequence.

Expanding the motif search to handle regular expression patterns.

Integrating a simple graphical user interface (GUI) instead of a command-line tool.
