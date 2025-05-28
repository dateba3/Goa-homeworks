#1) მომხმარებელს შემოატანინეთ ასაკი და შეამოწმეთ თუ ის ნაკლებია 18-ზე მაშინ შეამოწმეთ თუ ასაკი
#ნაკლებია 14-ზე დაუბეჭდეთ Discount 20%, სხვა შემთხვევაში Discount 10%.
#თუ პირველი if-ი არასწორია დაბეჭდეთ No discount
#გამოიყენეთ ჩაშენებული if

age=int(input("please enter you number: "))

if age<18 and age<14:
    print("Discount 20%: ")
elif age>18:
    print("No Discount: ")
else:
    print("Discount 10%: ")
      

#2) შექმენით infinity loop-ი(გამოიყენეთ while loop-ი)
num=5
while num<10:
    print("infinite loop")