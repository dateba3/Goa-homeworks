#1) კომენტარებით ახსენით რა არის არგუმენტი, range ფუნქცია და რა ხდება მაშინ, როდესაც მას გადაეცემა ერთი, ორი ან სამი არგუმენტი.

#არგუმნტი არის მნიშვნელობა რომლიც ფუნქციას გადაეეცმა მის გასაშვებად
#range ფუნქცია ქმნის რიცხვბის მიმდვრობას
#1-შემთხვვაში არის range stop იწყება 0დან და მთვრდება stop მდე
#2-შემთვევაში იწყება start იდან და მთავრდება stop მდე
#3-შემთხვევაში იწყება start იდან მთავრდება stop მდე მაგრამ ყოველი ახალი რიცხვი მცირედბა ან იზრდება step ის მიხდვით

#2) დაითვალეთ რამდენი ლუწი რიცხვია 1-დან 50-ის ჩათვლით(გამოიყენეთ for loop-ი)
count=0
 
for i in range(2,51,2):
    count=count+1
print(count)

#3) დაბეჭდეთ 1-დან 100-მდე ყველა ლუწი რიცხვის საშუალო არითმეტიკული. გამოიყენეთ for loop-ი.(დაგჭირდებათ ორი ცვლადის შექმნა, ერთში შეინახავთ ჯამს, მეორეში რაოდენობას)

sum=0
count=0

for i in range(2,100, 2):
   sum=sum+i
   count=count+1

print(sum//count)

#4) დაბეჭდეთ ყველა რიცხვი 1-დან 30-მდე, რომელიც იყოფა 3-ზე(გამოიყენეთ for loop-ი)

for i in range(1,31,):
    if i % 3 == 0:
        print(i)

        
#5) მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მიღებული რიცხვის ყველა გამყოფი(გამოიყენეთ for loop-ი)
number=int(input("enter number: "))

print("gamyopi is: ")
for i in range(1, number+1):
    if number % i==0:
        print(i)
        
#6) დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაბეჭდავს ეს რიცხვი დადებითია, უარყოფითია თუ 0-ია
number=int(input("please enter you number: "))
if number>0:
    print("dadebitia")
else:
    print("uaryopitia")

#7) დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოატანინებს წელს და გაიგებს არის თუ არა ის ნაკიანი(წელი როდესაც თებერვალში 29 დღე გვაქვს).
#  ნაკიანი არის წელი თუ ის იყოფა 4-ზე და არ იყოფა 100-ზე ან იყოფა 400-ზე.(გამოიყენეთ and და or ოპერატორები)

year = 2016

if year % 4 == 0 and year % 400 != 0:
    print(True)
else:
    print(False)