import seaborn as sns
import matplotlib.pyplot as plt
from warnings import filterwarnings

df = sns.load_dataset('tips')

df.head()
sns.violinplot(x ='day', y ='total_bill', data = df, hue ='sex', split = True)

plt.show()
