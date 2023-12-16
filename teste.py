import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

grafico= sns.load_dataset('titanic')
print(grafico.head())

sns.catplot(x='class', y='survived', data= grafico, kind='bar')

plt.show()

'''#Mapa de cluster
sns.clustermap(vp, cmap='coolwarm', standard_scale=1)
plt.show()'''