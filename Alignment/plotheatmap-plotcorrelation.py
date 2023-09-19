import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming data is your correlation matrix as a list of lists
data = [
    ['UOK121-TEAD1-rep2_S27.sorted.bam',	1.0000,	0.8634,	0.5288,	0.4878,	0.4673,	0.5404,	0.5184,	0.3028,	0.3808,	0.3104,	0.1723],
    ['UOK121-TEAD1-rep2_S27.XS.sorted.bam',	0.8634,	1.0000,	0.4233,	0.3933,	0.5633,	0.4739,	0.4335,	0.1213,	0.1492,	0.2561,	0.1139],
    ['UOK122-TEAD1-rep2_S16.sorted.bam',	0.5288,	0.4233,	1.0000,	0.7748,	0.6856,	0.6847,	0.6100,	0.6405,	0.5123,	0.3530,	0.2666],
    ['UOK342-TEAD1-rep1_S7.sorted.bam', 0.4878, 0.3933, 0.7748, 1.0, 0.8881, 0.6193, 0.5745, 0.5703, 0.4524, 0.3337, 0.2525], 
    ['UOK342-TEAD1-rep1_S7.XS.sorted.bam', 0.4673, 0.5633, 0.6856, 0.8881, 1.0, 0.5671, 0.5196, 0.4085, 0.2713, 0.292, 0.1988], 
    ['UOK342-TEAD1-rep2_S19.sorted.bam', 0.5404, 0.4739, 0.6847, 0.6193, 0.5671, 1.0, 0.5768, 0.2704, 0.1509, 0.3601, 0.2155], 
    ['HK2-TEAD1-rep2_S24.sorted.bam', 0.5184, 0.4335, 0.61, 0.5745, 0.5196, 0.5768, 1.0, 0.5683, 0.3502, 0.4564, 0.2082], 
    ['HK2-1perinput-rep1_S34.sorted.bam', 0.3028, 0.1213, 0.6405, 0.5703, 0.4085, 0.2704, 0.5683, 1.0, 0.767, 0.2966, 0.2109], 
    ['UOK121-1perinput-rep1_S30.sorted.bam', 0.3808, 0.1492, 0.5123, 0.4524, 0.2713, 0.1509, 0.3502, 0.767, 1.0, 0.1767, 0.1845], 
    ['HK2-TEAD1-rep1_S8.sorted.bam', 0.3104, 0.2561, 0.353, 0.3337, 0.292, 0.3601, 0.4564, 0.2966, 0.1767, 1.0, 0.1619], 
    ['UOK122-TEAD1-rep1_S6.sorted.bam', 0.1723, 0.1139, 0.2666, 0.2525, 0.1988, 0.2155, 0.2082, 0.2109, 0.1845, 0.1619, 1.0]
]

# Convert your data to DataFrame and sort the index (row labels)
df = pd.DataFrame(data).set_index(0).sort_index()

# Sort the columns (alphabetically)
df.columns = df.index.tolist()
df = df.sort_index(axis=1)

plt.figure(figsize=(10,10))
sns.heatmap(df.astype(float), cmap='viridis')

plt.title('Correlation Heatmap')
plt.show()
