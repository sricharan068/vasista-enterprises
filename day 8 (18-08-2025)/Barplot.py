import seaborn as sns
import matplotlib.pyplot as plt

from warnings import filterwarnings

df = sns.load_dataset('tips')

df.head()
sns.set_style('darkgrid')

sns.barplot(x ='sex', y ='total_bill', data = df, palette ='plasma')

import numpy as np

sns.barplot(x ='sex', y ='total_bill', data = df, 
            palette ='plasma', estimator = np.std)
plt.show()
