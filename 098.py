import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

grafico= sns.load_dataset('titanic')
print(grafico.head())

sns.swarmplot(x='class', y='age', data=grafico)
plt.show()