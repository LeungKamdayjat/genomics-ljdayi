Alignment files, mostly python script that can generate shell script to run in JHPCE.

Template shell script - using Sun Grid Engine (SGE)
-------------------------------------------------------------------------------------------------------------------------------------------------------
#$ -l h_fsize=500G
#$ -cwd 
#$ -m e -M jliang58@jhu.edu
#$ -l mem_free=16G,h_vmem=16G
#$ -pe local 24

module load fastqc
module load trimgalore
module load cutadapt
module load bowtie2
module load samtools
module load python
export PATH="$HOME/.local/bin:$PATH"
pip3 install --user deeptools

cat UOK122-H3K9me3-rep1_S10_L001_R1_001.fastq.gz UOK122-H3K9me3-rep1_S10_L002_R1_001.fastq.gz > UOK122-H3K9me3-rep1_S10_R1_cat.fastq.gz
cat UOK122-H3K9me3-rep1_S10_L001_R2_001.fastq.gz UOK122-H3K9me3-rep1_S10_L002_R2_001.fastq.gz > UOK122-H3K9me3-rep1_S10_R2_cat.fastq.gz
fastqc UOK122-H3K9me3-rep1_S10_R1_cat.fastq.gz
fastqc UOK122-H3K9me3-rep1_S10_R2_cat.fastq.gz
trim_galore --illumina --paired UOK122-H3K9me3-rep1_S10_R1_cat.fastq.gz UOK122-H3K9me3-rep1_S10_R2_cat.fastq.gz >UOK122-H3K9me3-rep1_S10.trim.log 2>UOK122-H3K9me3-rep1_S10.trim.err
zcat UOK122-H3K9me3-rep1_S10_R1_cat_val_1.fq.gz >UOK122-H3K9me3-rep1_S10_R1_trimmed.fq
zcat UOK122-H3K9me3-rep1_S10_R2_cat_val_2.fq.gz >UOK122-H3K9me3-rep1_S10_R2_trimmed.fq
bowtie2 -p 20 -x /users/jliang/chm13.draft_v1.0_plusY/chm13.draft_v1.0_plusY -N 0 -k 20  -1 UOK122-H3K9me3-rep1_S10_R1_trimmed.fq -2 UOK122-H3K9me3-rep1_S10_R2_trimmed.fq 2>UOK122-H3K9me3-rep1_S10.align.log |
samtools view -b - |
samtools sort -@ 12 - |
samtools rmdup -s - UOK122-H3K9me3-rep1_S10_trimmed.rmd.bam
samtools sort UOK122-H3K9me3-rep1_S10_trimmed.rmd.bam -o UOK122-H3K9me3-rep1_S10.sorted.bam
samtools index -b UOK122-H3K9me3-rep1_S10.sorted.bam
bamCoverage -b UOK122-H3K9me3-rep1_S10.sorted.bam -o UOK122-H3K9me3-rep1_S10.bigwig -of bigwig
------------------------------------------------------------------------------------------------------------------------------------------------------

Followed by alignment, would be peak calling(MACS2) and heatmap (using DeepTools):

For convenience, .py script would be generated based on individual purposes: 
- bam file merging for two replicates
- bam coverage for bigwig
- macs2 peak calling (with -bedgraph)
- plotHeatmap and plotCorrelation
