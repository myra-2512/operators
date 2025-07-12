tree1=45
tree2=98
tree3=54
tree4=23
tree5=67

sum = tree1+tree2+tree3+tree4+tree5
print("The sum of all the 5 trees is:",sum)

average=sum/5
print("The average of all the 5 trees is:",average)


#Activity 2

amount=int(input("Please enter the amount for withrawal:"))

note_1=amount//500
note_2=(amount%500)//100
note_3=((amount%500)%100)//50
note_4=(((amount%500)%100)%50)//10

print("notes of 500 rupees:",note_1)
print("notes of 100 rupees:",note_2)
print("notes of 50 rupees:",note_3)
print("notes of 10 rupees:",note_4)


#Activity 3


print("Enter marks obtained in 5 subjects:")
maths=int(input("Maths: "))
science=int(input("Science: "))
english=int(input("English: "))
sst=int(input("SST: "))
hindi=int(input("Hindi: "))

sum=maths + science + english + sst + hindi
print("The sum of maths, science, english, sst and hindi is:", sum)

perc=(sum/500)*100
print("The percentage is:", perc)
