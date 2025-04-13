#1) მომხმარებელს შემოატანინეთ მისი ასაკი და სახელი, შემდეგ if/else-ის გამოყენებით შეამოწმეთ არის თუ არა ის სრულწლოვანი
#და უდრის თუ არა მისი სახელი თქვენს სახელს.(შემოწმების შედეგიდან გამომდინარე დაბეჭდეთ True/False) 
user_name = input("please enter you name: ")
user_age = int(input("please enter you age: "))

my_name = "dato"

if user_age >= 18:
    print("adult: True")
else:
    print("adult: False")

if user_name == my_name:
    print("name mach: True")
else:
    print("name mach: False")

#2) მომხმარებელს შემოატანინეთ სახელი და თუ ის თქვენს სახელს ემთხვევა დაბეჭდეთ "coincidence"

name="dato"
name1=input("please enter you name: ")
if name==name1:
   print("coincidence")

#3) მოხმარებელს შემოატანინეთ გამოცდის ქულა და შეინახეთ score ცვლადში ინტეჯერად, თუ ქულა მეტია 70-ზე დაუბეჭდეთ რომ გამოცდა გადალახა "passed" სხვა შემთხვევაში კი რომ ჩაიჭრა "failed
score= int(input("please enter you score: "))
if score > 70:
    print("you pased")
else:
    print("you failed")

#4) მომხმარებელს შემოატანინეთ ქულა `score` და შეინახეთ ცვლადში, როგორც **integer**.
#შემდეგ, ქულის მიხედვით განსაზღვრეთ შეფასება (**grade**):  
# A – თუ `score` **მეტია 80-ზე**  
# B – თუ `score` **მეტია 60-ზე**  
# C – თუ `score` **მეტია 40-ზე**  
# D – თუ `score` **მეტია 20-ზე**  
# F – თუ `score` **20-ზე ნაკლებია**  

#ბოლოს, დაბეჭდეთ შესაბამისი **grade**.

score= int(input("please enter you score: "))
if   score>80:
    print("A")
elif score>60:
    print("B")
elif score>40:
    print("c")
elif score<20:
    print("F")
#5) კომენტარებით ახსენით რა არის Algorithm-ი. მოიყვანეთ ალგორითმის მაგალითი რეალური ცხოვრებიდან.

#ალგორითმი არის რასაც მუდმივად ვაკეთბთ და ვიმეორებთ
#მაგალითად ყოველთვის ჩაის მომზადება და ყოვეელთვის დილით გაღვიძება


