import seaborn as sns
import matplotlib.pyplot as plt
from warnings import filterwarnings

df = sns.load_dataset('tips')

df.head()
sns.boxplot(x ='day', y ='total_bill', data = df, hue ='smoker')

plt.show()
