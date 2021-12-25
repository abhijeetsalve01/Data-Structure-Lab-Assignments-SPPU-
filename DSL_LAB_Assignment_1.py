# Function for count of student absent for test
def absentSC(listOfStudent, numberOfStudent):
    count = 0
    for i in range(numberOfStudent):
        if listOfStudent[i]==0:
            count +=1
    return count
# Function for Maximum
def maxMarks(listOfStudent, numberOfStudent):
    max = 0
    for i in range(numberOfStudent):
        if max<listOfStudent[i]:
            max = listOfStudent[i]
    return max
# Function to calculate largest marks frequency
def largestMFreq(numberOfStudent, listOfStudent):
    count = 0
    check = maxMarks(listOfStudent, numberOfStudent)
    for i in range(numberOfStudent):
        if check == listOfStudent[i]:
            count += 1
    return count
# Function to calculate minimum marks frequency
def minMFreq(numberOfStudent, listOfStudent):
    count = 0
    check = minMarks(listOfStudent, numberOfStudent)
    for i in range(numberOfStudent):
        if check == listOfStudent[i]:
            count += 1
    return count
# Function for Minimum
def minMarks(listOfStudent, numberOfStudent):
    min = listOfStudent[0]
    for i in range(numberOfStudent):
        if min>listOfStudent[i]:
            min = listOfStudent[i]
    return min
# Function for Average
def averageOfMarks(listOfStudent, numberOfStudent):
    sumInitialize = 0
    for i in range(numberOfStudent):
        sumInitialize += listOfStudent[i]
    return (sumInitialize/numberOfStudent)
# main program
loop = True
listOfStudent = []   
numberOfStudent = int(input("Enter No of Student: "))
count = 1
for i in range(numberOfStudent):
    marks = int(input(f"Enter marks for student {count}: "))
    listOfStudent.append(marks)
    count+=1
def showList():
    print("--------------------Select Your Choice From Following list-----------------\n1) "
          "Enter 1 for Average\n2) Enter 2 for Maximum\n3) Enter 3 for Minimum\n4)Enter 4 for Largest Marks Frequency\n"
          "5)Enter 5 for minimum Marks Frequency\n6)Enter 6 for Count of absent student\n"
          "7) Enter 7 to create new list of marks"
          "\n8) Enter 8 to exit")
showList()
while loop:
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Average marks obtained by student is:",averageOfMarks(listOfStudent, numberOfStudent))
    elif choice == "2":
        print("Maximum marks obtained by student is: ",maxMarks(listOfStudent, numberOfStudent))
    elif choice == "3":
        print("Minimum marks obtained by student is: ",minMarks(listOfStudent, numberOfStudent))
    elif choice == "4":
        print(f"{maxMarks(listOfStudent, numberOfStudent)} is largest marks and its frequency is: ",largestMFreq(numberOfStudent, listOfStudent))
    elif choice == "5":
        print(minMarks(listOfStudent, numberOfStudent), " is minimum marks and its frequency is: ",minMFreq(numberOfStudent, listOfStudent))
    elif choice == "6":
        print("Number of absent student are: ", absentSC(listOfStudent, numberOfStudent))
    elif choice == "7":
        print("New list created")
        listOfStudent = []
        numberOfStudent = int(input("Enter No of Student: "))
        count = 1
        for i in range(numberOfStudent):
            marks = int(input(f"Enter marks for student {count}: "))
            listOfStudent.append(marks)
            count+=1
        print("--------------------Select Your Choice From Following list-----------------\n1) Enter 1 for Average\n"
              "2) Enter 2 for Maximum\n"
              "3) Enter 3 for Minimum\n"
              "4)Enter 4 for Largest Marks Frequency\n"
              "5)Enter 5 for minimum Marks Frequency\n"
              "6)Enter 6 for Count of absent student\n"
              "7) Enter 7 to create new list of marks\n"
              "8) Enter 8 to exit")
    elif choice == "8":
        loop = False
    else:
        print("You entered wrong choice try again")
