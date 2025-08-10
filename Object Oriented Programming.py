class Eidth_A:
    print('8A class :')


    def __init__(self,name, Roll_no, Age,marks):
        self.name = name
        self.Roll_no = Roll_no
        self.Age = Age
        self.marks = marks


    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print('Hi!', self.name, 'your avg score is',sum/3)


s1 = Eidth_A('Adarsh', 1, 12,[56,23,45] )
print(s1.name)
print('Rollno. = ',s1.Roll_no)
print('Age = ',s1.Age)
s1.get_average()


s2 = Eidth_A('Daksh', 11, 12,[67,34,56])
print(s2.name)
print('Rollno. = ',s2.Roll_no)
print('Age = ',s2.Age)
s2.get_average()


s3 = Eidth_A('Dakshay', 10, 14, [100,56,45])
print(s3.name)
print('Rollno. = ',s3.Roll_no)
print('Age = ',s3.Age)
s3.get_average()


s4 = Eidth_A('Paras', 24, 12,[99,45,78])
print(s4.name)
print('Rollno. = ',s4.Roll_no)
print('Age = ',s4.Age)
s4.get_average()


s5 = Eidth_A('Mayank', 19, 15, [79,45,67])
print(s5.name)
print('Rollno. = ',s5.Roll_no)
print('Age = ',s5.Age)
s5.get_average()


s6 = Eidth_A('Jatin', 14, 12,[0,0,0])
print(s6.name)
print('Rollno. = ',s6.Roll_no)
print('Age = ',s6.Age)
s6.get_average()


s7 = Eidth_A('Samarth', 28, 11,[89,23,99])
print(s7.name)
print('Rollno. = ',s7.Roll_no)
print('Age = ',s7.Age)
s7.get_average()
