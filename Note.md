# BEDintersec with TEAD1 and H3K9me3

#### Using MACS2 peak calling to generate narrawpeaks fo TEAD1 files. 

For control files, I use

- HK2-1perinput-rep1_S34.sorted.bam

- UOK121-1perinput-rep1_S30.sorted.bam

- UOK342-IgG-rep1_S31.sorted.bam

for test files (-t), I use following library for TEAD1 

- S27
    <ul>

      macs2 callpeak -t /Volumes/WD_BLACK/hg38_files/UOK121-TEAD1-rep2_S27.sorted.bam -c /Volumes/WD_BLACK/hg38_files/HK2-1perinput-rep1_S34.sorted.bam /Volumes/WD_BLACK/hg38_files/UOK121-1perinput-rep1_S30.sorted.bam /Volumes/WD_BLACK/hg38_files/UOK342-IgG-rep1_S31.sorted.bam -n UOK121-TEAD1-rep2_S27.sorted > UOK121-TEAD1-rep2_S27.sorted.macs.log 2> UOK121-TEAD1-rep2_S27.sorted.macs.err
    </ul>
- S8
    <ul>

      macs2 callpeak -t /Volumes/WD_BLACK/hg38_files/HK2-TEAD1-rep1_S8.sorted.bam -c /Volumes/WD_BLACK/hg38_files/HK2-1perinput-rep1_S34.sorted.bam /Volumes/WD_BLACK/hg38_files/UOK121-1perinput-rep1_S30.sorted.bam /Volumes/WD_BLACK/hg38_files/UOK342-IgG-rep1_S31.sorted.bam -n HK2-TEAD1-rep1_S8.sorted > HK2-TEAD1-rep1_S8.sorted.macs.log 2> HK2-TEAD1-rep1_S8.sorted.macs.err
    </ul>
- UOK122-TEAD1-rep2_S16.sorted.bam
    <ul>

      macs2 callpeak -t /Volumes/WD_BLACK/hg38_files/UOK122-TEAD1-rep2_S16.sorted.bam -c /Volumes/WD_BLACK/hg38_files/HK2-1perinput-rep1_S34.sorted.bam /Volumes/WD_BLACK/hg38_files/UOK121-1perinput-rep1_S30.sorted.bam /Volumes/WD_BLACK/hg38_files/UOK342-IgG-rep1_S31.sorted.bam -n UOK122-TEAD1-rep2_S16.sorted > UOK122-TEAD1-rep2_S16.sorted.macs.log 2> UOK122-TEAD1-rep2_S16.sorted.macs.err
    </ul>

- UOK342-TEAD1-rep1_S7.sorted.bam
    <ul>

      macs2 callpeak -t /Volumes/WD_BLACK/hg38_files/UOK342-TEAD1-rep1_S7.sorted.bam -c /Volumes/WD_BLACK/hg38_files/HK2-1perinput-rep1_S34.sorted.bam /Volumes/WD_BLACK/hg38_files/UOK121-1perinput-rep1_S30.sorted.bam /Volumes/WD_BLACK/hg38_files/UOK342-IgG-rep1_S31.sorted.bam -n UOK342-TEAD1-rep1_S7.sorted > UOK342-TEAD1-rep1_S7.sorted.macs.log 2> UOK342-TEAD1-rep1_S7.sorted.macs.err
    </ul>
note: there're replicate files, but this files I think might have the best quality

#### Using SICER peak calling to generate broadpeaks for H3K9me3 files.

#### TEAD1 and H3K9me3 Peaks in UOK121

- Finding UOK121-TEAD1 and UOK121-H3K9me3 intersected peaks
    <ul>

      bedtools intersect -wa -wb -a /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/0830_bedintersect/UOK121-TEAD1-rep2_S27.sorted_peaks.narrowPeak -b /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/0830_bedintersect/UOK121-H3K9me3-rep1_S23.sorted-W200-G600-FDR0.01-island.tabrm.bed > UOK121-TEAD1-H3K9me3.bedintsct
    </ul>
- finding UOK121-TEAD1 and UOK121-H3K9me3 peaks that are not intersected. 
    <ul>

      bedtools subtract -a /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/0830_bedintersect/UOK121-TEAD1-rep2_S27.sorted_peaks.narrowPeak -b /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/0830_bedintersect/UOK121-TEAD1-H3K9me3.bedintsct > >UOK121-TEAD1-H3K9me3.bedsbtrct
    </ul>

    <ul>
- visualization: using UOK121-TEAD1 and UOK121-H3K9me3 intersected peaks and subtracted peaks as reference files
    <ul>

      computeMatrix reference-point --referencePoint center -b 3000 -a 3000 -R UOK121-TEAD1-H3K9me3.bedintsct UOK121-TEAD1-H3K9me3.bedsbtrct -S /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/HK2-TEAD1-rep1_S8.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-TEAD1-rep2_S27.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK122-TEAD1-rep2_S16.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK342-TEAD1-rep1_S7.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-1perinput-rep1_S30.sorted.bigwig  /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-H3K9me3-rep1_S23.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK342-H3K9me3-rep2_S21.sorted.bigwig  -o UOK121-H3K9me3-TEAD1.mat.gz
    </ul>
  <ul>

      plotHeatmap -m UOK121-H3K9me3-TEAD1.mat.gz -out UOK121-H3K9me3-TEAD1.mat.png --colorMap Reds Reds Reds Reds Blues Greens Greens --whatToShow 'heatmap and colorbar' --samplesLabel HK2-TEAD1 UOK121-TEAD1 UOK122-TEAD1 UOK342-TEAD1 input UOK121-H3K9me3 UOK342-H3K9me3 -z Intersect Substraction
    ![Alt text](UOK121-H3K9me3-TEAD1.mat-1.png)
    </ul>
- To visualize only the intersected peaks and normalize the heatplot intensity.
    <ul>

      computeMatrix reference-point --referencePoint center -b 3000 -a 3000 -R UOK121-TEAD1-H3K9me3.bedintsct -S /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/HK2-TEAD1-rep1_S8.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-TEAD1-rep2_S27.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK122-TEAD1-rep2_S16.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK342-TEAD1-rep1_S7.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-1perinput-rep1_S30.sorted.bigwig  /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-H3K9me3-rep1_S23.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK342-H3K9me3-rep2_S21.sorted.bigwig  -o UOK121-H3K9me3-TEAD1.intsct.mat.gz
    </ul>
  <ul>

      plotHeatmap -m UOK121-H3K9me3-TEAD1.intsct.mat.gz -out UOK121-H3K9me3-TEAD1.intsct.mat.png --colorMap Reds Reds Reds Reds Blues Greens Greens --whatToShow 'heatmap and colorbar' -max 45 --kmeans 3 --samplesLabel HK2-TEAD1 UOK121-TEAD1 UOK122-TEAD1 UOK342-TEAD1 input UOK121-H3K9me3 UOK342-H3K9me3
    ![Alt text](UOK121-H3K9me3-TEAD1.intsct.mat.png)
    </ul>   
- Finding UOK342-TEAD1 and UOK342-H3K9me3 intersected peaks
    <ul>

      bedtools intersect -wa -wb -a /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/0830_bedintersect/UOK342-TEAD1-rep1_S7.sorted_peaks.narrowPeak -b /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/0830_bedintersect/UOK342-H3K9me3-rep2_S21.sorted-W200-G600-FDR0.01-island.tabrm.bed > UOK342-TEAD1-H3K9me3.bedintsct
    </ul>
- Finding UOK342-TEAD1 and UOK342-H3K9me3 peaks that are not intersected. 
    <ul>

      bedtools subtract -a /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/0830_bedintersect/UOK342-TEAD1-rep1_S7.sorted_peaks.narrowPeak -b /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/0830_bedintersect/UOK342-TEAD1-H3K9me3.bedintsct > UOK342-TEAD1-H3K9me3.bedsbtrct
    </ul>
    <ul>
- visualization: using UOK342-TEAD1 and UOK342-H3K9me3 intersected peaks and subtracted peaks as reference files.
    <ul>

      computeMatrix reference-point --referencePoint center -b 3000 -a 3000 -R UOK342-TEAD1-H3K9me3.bedintsct UOK342-TEAD1-H3K9me3.bedsbtrct -S /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/HK2-TEAD1-rep1_S8.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-TEAD1-rep2_S27.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK122-TEAD1-rep2_S16.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK342-TEAD1-rep1_S7.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-1perinput-rep1_S30.sorted.bigwig  /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-H3K9me3-rep1_S23.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK342-H3K9me3-rep2_S21.sorted.bigwig  -o UOK342-H3K9me3-TEAD1.mat.gz
    </ul>
  <ul>

      plotHeatmap -m UOK342-H3K9me3-TEAD1.mat.gz -out UOK342-H3K9me3-TEAD1.mat.png --colorMap Reds Reds Reds Reds Blues Greens Greens --whatToShow 'heatmap and colorbar' --samplesLabel HK2-TEAD1 UOK121-TEAD1 UOK122-TEAD1 UOK342-TEAD1 input UOK121-H3K9me3 UOK342-H3K9me3 -z Intersect Substraction
    ![Alt text](UOK342-H3K9me3-TEAD1.mat.png)
    </ul>
- To visualize only the intersected peaks and normalize the heatplot intensity.
    <ul>

      computeMatrix reference-point --referencePoint center -b 3000 -a 3000 -R UOK342-TEAD1-H3K9me3.bedintsct -S /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/HK2-TEAD1-rep1_S8.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-TEAD1-rep2_S27.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK122-TEAD1-rep2_S16.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK342-TEAD1-rep1_S7.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-1perinput-rep1_S30.sorted.bigwig  /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK121-H3K9me3-rep1_S23.sorted.bigwig /Users/jeffrey.liang/Library/CloudStorage/OneDrive-JohnsHopkins/Cai_Lab/7_ChIPseq/ChIP\ Library/hg38_alignment/UOK342-H3K9me3-rep2_S21.sorted.bigwig  -o UOK342-H3K9me3-TEAD1.intsct.mat.gz
    </ul>
  <ul>

      plotHeatmap -m UOK342-H3K9me3-TEAD1.intsct.mat.gz -out UOK342-H3K9me3-TEAD1.intsct.mat.png --colorMap Reds Reds Reds Reds Blues Greens Greens --whatToShow 'heatmap and colorbar' -max 45 --kmeans 3 --samplesLabel HK2-TEAD1 UOK121-TEAD1 UOK122-TEAD1 UOK342-TEAD1 input UOK121-H3K9me3 UOK342-H3K9me3
![Alt text](UOK342-H3K9me3-TEAD1.intsct.mat.png)
    </ul>


CEAS

http://cistrome.org/ap/

BETA

http://cistrome.org/BETA/

https://www.nature.com/articles/