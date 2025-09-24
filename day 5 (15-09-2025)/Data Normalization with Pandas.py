import pandas as pd  
import matplotlib.pyplot as plt  

df = pd.DataFrame([
    [180000, 110, 18.9, 1400],  
    [360000, 905, 23.4, 1800],  
    [230000, 230, 14.0, 1300],  
    [60000, 450, 13.5, 1500]
], columns=['Col A', 'Col B', 'Col C', 'Col D'])

print(df)

df.plot(kind='bar')
plt.show()


