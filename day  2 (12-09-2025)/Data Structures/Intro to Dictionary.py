def create_dict(names, marks):
    return dict(zip(names, marks))

if __name__ == "__main__":
    N = int(input("Enter number of students: "))


    names = input("Enter names: ").split()


    marks = list(map(int, input("Enter marks: ").split()))

    student_dict = create_dict(names, marks)

    for name in sorted(student_dict.keys()):
        print(name, student_dict[name])
