from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('train.csv', header=0)
df1=df.iloc[:,2:]
kmeans = KMeans(n_clusters=2, random_state=10).fit(df1)
df1['activity']=kmeans.labels_
df_count_type=df1.groupby('activity').apply(np.size)

df_count_type

kmeans.cluster_centers_

new_df=df1[:]
new_df
new_df.to_csv('train.csv')


pca = PCA(n_components=2)
new_pca = pd.DataFrame(pca.fit_transform(new_df))


d = new_pca[new_df['activity'] == 0]
plt.plot(d[0], d[1], 'r.')
d = new_pca[new_df['activity'] == 1]
plt.plot(d[0], d[1], 'go')
d = new_pca[new_df['activity'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.gcf().savefig('kmeans.png')
plt.show()