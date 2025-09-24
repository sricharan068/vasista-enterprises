import seaborn as sns
import matplotlib.pyplot as plt
from warnings import filterwarnings

df = sns.load_dataset('tips')

df.head()
sns.jointplot(x ='total_bill', y ='tip', data = df)

plt.show()
sns.jointplot(x ='total_bill', y ='tip', data = df, kind ='kde')
plt.show()

