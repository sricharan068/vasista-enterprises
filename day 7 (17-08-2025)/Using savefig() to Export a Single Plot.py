import matplotlib.pyplot as plt  

plt.plot([1, 2, 3, 4], [10, 20, 25, 30], marker='o', linestyle='--', color='b')  
plt.title("Sample Plot")  

plt.savefig("plot.pdf", format="pdf")  

plt.show()
