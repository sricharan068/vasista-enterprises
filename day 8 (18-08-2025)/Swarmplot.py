import seaborn as sns
import matplotlib.pyplot as plt
from warnings import filterwarnings

df = sns.load_dataset('tips')

df.head()
sns.swarmplot(x ='day', y ='total_bill', data = df)

plt.show()
