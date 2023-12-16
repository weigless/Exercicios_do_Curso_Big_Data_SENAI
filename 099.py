import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

grafico= sns.load_dataset('titanic')
print(grafico.head())

sns.countplot(x='sex', data=grafico)

plt.show()