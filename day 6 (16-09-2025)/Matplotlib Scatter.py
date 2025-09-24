x = np.array([3, 12, 9, 20, 5, 18, 22, 11, 27, 16])
y = np.array([95, 55, 63, 77, 89, 50, 41, 70, 58, 83])

a = [20, 50, 100, 200, 500, 1000, 60, 90, 150, 300] # size
b = ['red', 'green', 'blue', 'purple', 'orange', 'black', 'pink', 'brown', 'yellow', 'cyan'] # color

plt.scatter(x, y, s=a, c=b, alpha=0.6, edgecolors='w', linewidth=1)
plt.title("Scatter Plot with Varying Colors and Sizes")
plt.show()
