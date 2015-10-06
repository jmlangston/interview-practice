# variation on hackerrank python introduction problem called 'finding the percentage'

# given: list of students and their grades for math, physics, and chemistry
# return: average grade for 

# N = raw_input()
# student1 = raw_input()
# student2 = raw_input()
# student3 = raw_input()
# output_student = raw_input()

N = '3'
student1 = 'Krishna 67 68 69'
student2 = 'Arjun 70 98 63'
student3 = 'Malika 52 56 60'
output_student = 'Malika'

stu_dict = {}

stu1 = student1.split(' ')
stu2 = student2.split(' ')
stu3 = student3.split(' ')

stu_dict[stu1[0]] = stu1[1:]
stu_dict[stu2[0]] = stu2[1:]
stu_dict[stu3[0]] = stu3[1:]

grades = stu_dict[output_student]
output = (int(grades[0]) + int(grades[1]) + int(grades[2])) / int(N)

print output


# d={}
# for i in range(int(raw_input())):
#     line=raw_input().split()
#     d[line[0]]=sum(map(float,line[1:]))/3

# print '%.2f' % d[raw_input()]
