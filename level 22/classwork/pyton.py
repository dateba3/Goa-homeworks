#1) დაბეჭდეთ 0-დან 10-მდე ყველა რიცხვი, შემდეგ კი 0-დან 10-ის ჩათვლით
for i in range(11):
    print(i)
for i in range(10):
    print(i)
#2) დაბეჭდეთ 20-დან 100-ის ჩათვლით ყველა რიცხვი
for i in range(20, 101):
    print(i)
#3) დაბეჭდეთ 0-დან 20-ის ჩათვლით ყველა ლუწი რიცხვი(ყოველი მეორე რიცხვი)
for i in range(0, 21, 2):
    print(i)
#4) დაბეჭდეთ 30-დან 50-მდე ყოველი მეოთხე რიცხვი
for i in range(30, 51, 4):
    print(i)
#5) მომხარებელს შემოატანინეთ რიცხვი. შეამოწმეთ, თუ შემოტანილი რიცხვი არის ლუწი დაბეჭდეთ "The numbers is even", სხვა შემთხვევაში დაბეჭდეთ "The number is odd"
number=int(input("please enter you number: "))
    
if number % 2==0:
    print("The number is even")
else:
    print("The number is odd")