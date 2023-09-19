import os

def filter_fasta(input_filename, output_filename):
    input_filename = os.path.expanduser(input_filename)
    output_filename = os.path.expanduser(output_filename)

    with open(input_filename, 'r') as fasta_file:
        lines = fasta_file.readlines()

    processed_lines = []
    sequence_set = set()
    header = None
    for line in lines:
        line = line.strip()  # remove trailing newlines
        if line.startswith(">"):
            header = line
        else:
            sequence = line.upper()
            if sequence not in sequence_set and len(sequence) >= 8:
                sequence_set.add(sequence)
                processed_lines.append(header)
                processed_lines.append(line)

    with open(output_filename, 'w') as out_file:
        for line in processed_lines:
            out_file.write(line + "\n")  # add newline character back in
 

# replace 'input.fasta' and 'output.fasta' with your file names
filter_fasta('/Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/MEME/UOK342-H3K9me3-TEAD1_expanded.int.ops.fa', 'UOK342-TEAD1-H3K9me3_expanded.int.ops.filtered.fasta')
