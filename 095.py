import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

grafico= sns.load_dataset('titanic')
print(grafico.head())

sns.jointplot(x= 'fare', y= 'age', data=grafico, kind='reg')
plt.show()