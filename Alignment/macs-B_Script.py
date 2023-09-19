import os

def process_file(cell_line,repeat_name ,protein_name, replicate_files, control_files):
    output_filename = f"{cell_line}-{protein_name}-{repeat_name}_macs-B_commands.sh"

    with open(output_filename, "w") as output_file:
        output_file.write("#$ -l h_fsize=100G\n")
        output_file.write("#$ -cwd\n")
        output_file.write("#$ -m e -M jliang58@jhu.edu\n")
        output_file.write("#$ -l mem_free=8G,h_vmem=8G\n")
        output_file.write("#$ -pe local 2\n\n")
        output_file.write("module load python\n")
        output_file.write("export PATH=\"$HOME/.local/bin:$PATH\"\n")
        output_file.write("pip3 install --upgrade numpy\n")
        output_file.write("pip3 install macs3\n\n")
        command = f"macs3 callpeak -t {replicate_files} -c {control_files} -B -n {cell_line}-{protein_name}-{repeat_name} > {cell_line}-{protein_name}-{repeat_name}.macs.log 2> {cell_line}-{protein_name}-{repeat_name}.macs.err\n"
        output_file.write(command)

    print(f"MACS commands have been written to {output_filename}")

# List of files
file_list = [
("UOK342-TEAD1-rep2_S19.sorted.bam"),
("UOK122-YAP1-rep2_S17.sorted.bam"),
("UOK121-YAP1-rep2_S26.sorted.bam"),
("HK2-YAP1-rep1_S22.sorted.bam"),
("UOK342-TEAD1-rep1_S7.sorted.bam"),
("UOK342-YAP1-rep1_S11.sorted.bam"),
("HK2-H3K27ac-rep1_S4.sorted.bam"),
("HK2-TEAD1-rep2_S24.sorted.bam"),
("UOK121-TEAD1-rep2_S27.sorted.bam"),
("UOK121-H3K7ac-rep1_S1.sorted.bam"),
("UOK122-TEAD1-rep2_S16.sorted.bam"),
("UOK122-YAP1-rep1_S9.sorted.bam"),
("HK2-YAP1-rep2_S32.sorted.bam"),
("UOK342-H3K9me3-rep1_S12.sorted.bam"),
("HK2-H3K9me3-rep1_S14.sorted.bam"),
("UOK122-H3K9me3-rep2_S18.sorted.bam"),
("UOK122-H3K27ac-rep1_S2.sorted.bam"),
("UOK122-H3K9me3-rep1_S10.sorted.bam"),
("UOK342-H3K27ac-rep2_S13.sorted.bam"),
("UOK122-TEAD1-rep1_S6.sorted.bam"),
("UOK342-YAP1-rep2_S20.sorted.bam"),
("UOK121-H3K9me3-rep2_S29.sorted.bam"),
("UOK342-H3K9me3-rep2_S21.sorted.bam"),
("UOK121-H3K27ac-rep2_S28.sorted.bam"),
("UOK342-H3K27ac-rep1_S3.sorted.bam"),
("UOK122-H3K27ac-rep2_S25.sorted.bam"),
("HK2-H3K9me3-rep2_S33.sorted.bam"),
("UOK121-H3K9me3-rep1_S23.sorted.bam"),
("HK2-TEAD1-rep1_S8.sorted.bam"),
("UOK121-YAP1-rep1_S15.sorted.bam")
]

# Process each file pair
for replicate_files in file_list:
    basename = os.path.splitext(replicate_files)[0]
    print(basename)
    parts = basename.split("-")
    cell_line = parts[0]
    protein_name = parts[1]
    repeat_name = parts[2]
    control_files = "UOK121-1perinput-rep1_S30.sorted.bam HK2-1perinput-rep1_S34.sorted.bam UOK342-IgG-rep1_S31.sorted.bam"

    process_file(cell_line,repeat_name ,protein_name, replicate_files, control_files)
