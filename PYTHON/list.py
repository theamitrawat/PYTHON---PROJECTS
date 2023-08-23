print('\nEnter the seven fruits name here!\n')
fruit_list=[]
for i in range(7):
    f = input(f'Fruit {i+1}: ')
    fruit_list.append(f)

print(f'\nFruit List: {fruit_list}\n')



print('\nEnter the marks of 6 students!\n')

marks_list=[]
for i in range(6):
    print(f'~~ STUDENT {i+1} ~~\n')
    marks=[]
    for j in range(5):
        stu_marks = int(input(f'\tSubject {j+1}: '))
        marks.append(stu_marks)
    marks_list.append(tuple(marks))

print('\nMarks List!\n')

for m,marks in enumerate(marks_list,start=1):
    print(f'Student {m}: {marks}')
    

num_list = int(input("\nEnter the number of elements: "))

newList = [];
for i in range(num_list):
    element = int(input(f'Enter the {i+1} number: '))
    newList.append(element)
print('\n Your entered list: ',newList)
print(sum(num_list))
print(num_list.count(0))