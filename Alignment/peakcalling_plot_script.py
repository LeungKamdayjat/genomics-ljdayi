import os

def process_file(cell_line, protein_name, reference_name):
    output_filename = f"{cell_line}-{protein_name}-all.plot.sh"

    with open(output_filename, "w") as output_file:
        output_file.write("#$ -l h_fsize=100G\n")
        output_file.write("#$ -cwd\n")
        output_file.write("#$ -m e -M jliang58@jhu.edu\n")
        output_file.write("#$ -l mem_free=40G,h_vmem=40G\n")
        output_file.write("#$ -pe local 2\n\n")
        output_file.write("module load python\n")
        output_file.write("export PATH=\"$HOME/.local/bin:$PATH\"\n")
        command = f"computeMatrix reference-point \\\n--referencePoint center \\\n-b 3000 -a 3000 \\\n-S HK2-TEAD1.merged.sorted.bigwig \\\nHK2-H3K9me3.merged.sorted.bigwig \\\nHK2-YAP1.merged.sorted.bigwig \\\nUOK121-TEAD1.merged.sorted.bigwig \\\nUOK121-H3K9me3.merged.sorted.bigwig \\\nUOK121-YAP1.merged.sorted.bigwig \\\nUOK122-TEAD1.merged.sorted.bigwig \\\nUOK122-H3K9me3.merged.sorted.bigwig \\\nUOK122-YAP1.merged.sorted.bigwig \\\nUOK342-TEAD1.merged.sorted.bigwig \\\nUOK342-H3K9me3.merged.sorted.bigwig \\\nUOK342-YAP1.merged.sorted.bigwig \\\n-R {reference_name} \\\n--skipZeros -o {cell_line}-{protein_name}-all.mat.gz \\\n--outFileSortedRegion regions1_{cell_line}-{protein_name}_gene.bed\n\n"
        output_file.write(command)
        output_file.write(f"plotHeatmap -m {cell_line}-{protein_name}-all.mat.gz \\\n-out {cell_line}-{protein_name}-all.pdf \\\n--colorMap Greens \\\n--whatToShow 'heatmap and colorbar' \\\n--kmeans 3")

    print(f"MACS commands have been written to {output_filename}")

# List of files
file_list = [
    ("HK2-TEAD1_macs_peaks.narrowPeak"),("HK2-H3K9me3_macs_peaks.broadPeak"),("HK2-YAP1_macs_peaks.narrowPeak"),
    ("UOK121-TEAD1_macs_peaks.narrowPeak"),("UOK121-H3K9me3_macs_peaks.narrowPeak"),("UOK121-H3K7ac_macs_peaks.narrowPeak"),("UOK121-YAP1_macs_peaks.narrowPeak"),
    ("UOK122-H3K27ac_macs_peaks.narrowPeak"),("UOK122-TEAD1_macs_peaks.narrowPeak"),("UOK122-YAP1_macs_peaks.narrowPeak"),
    ("UOK342-H3K9me3_macs_peaks.narrowPeak"),("UOK342-H3K27ac_macs_peaks.narrowPeak"),("UOK342-TEAD1_macs_peaks.narrowPeak"),("UOK342-YAP1_macs_peaks.narrowPeak")
    
]

# Process each file pair
for replicate_files in file_list:
    basename = os.path.splitext(replicate_files)[0]
    parts = basename.split("-")
    cell_line = parts[0]
    end_name = parts[1]
    end_parts = end_name.split("_")
    protein_name = end_parts[0]

    process_file(cell_line, protein_name, replicate_files)
