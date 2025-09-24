import matplotlib.pyplot as plt

def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i])

x = ["Engineering", "BSc", "MBA", "Bcom", "BBA", "MSc"]
y = [9330, 4050, 3030, 5500, 8040, 4560]

plt.bar(x, y)

add_labels(x, y)

plt.title("College Admission")
plt.xlabel("Courses")
plt.ylabel("Number of Admissions")

plt.show()
