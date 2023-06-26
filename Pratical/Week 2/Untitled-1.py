#varible here
male = int(input("Enter the amount of male "))
female = int(input("Enter the amount of female "))

maxSum = male + female

precentMale = male / float(maxSum)
precentFemale = female / float(maxSum)

print(f"The precentage of male in clss is {precentMale * 100}%")
print(f"The precentage of female in calss is {precentFemale * 100}%")