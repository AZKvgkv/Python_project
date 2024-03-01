names = ('AZ','YX','MZ','CXQ')
ages = (24,23,20,22)
jobs = ('学生','打工er','群众')

for name,age,job in zip(names,ages,jobs):
    print("{0}-----{1}-----{2}".format(name,age,job))
    pass
