#2) გაიმეორეთ ყველა განვლილი მასალა: range ფუნქცია for/while ციკლები და if/elif/else

#3) მომხმარებელს შემოატანინეთ 5 რიცხვი. თქვენი დავალებაა დაითვალოთ აქედან დადებითი და უარყოფითი რიცხვები. საბოლოოდ დაბეჭდეთ შემდეგი ფორმატით:
#"Positive numbers count: {count}"
#"Negative numbers count: {count}"
positive_count = 0
negative_count = 0

for i in range(5):
    number = int(input("Enter number {i+1}: "))
    
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1

print("Positive number count:",positive_count)
print("Negative number count:",negative_count)

#4) მომხმარებელს შემოატანინეთ 3 რიცხვი და დაითვალეთ რამდენი მათგანია 10-ზე მეტი. თუ ყველა შემოტანილი რიცხვი ათზე მეტია, დაბეჭდეთ "All the numbers that are larger than ten.",
#სხვა შემთხვევაში დაბეჭდეთ "Some numbers that are less than or equal to ten."
num=10
gus1=int(input("please enter number: "))
gus2=int(input("please enter number: "))
gus3=int(input("please enter number: "))

if gus1 and gus2 and gus3 > num:
    print("All the numbers that are larger than ten")
else:
    print("Some numbers that are less than or equal to ten")

#5) მომხმარებელს შემოატანინეთ რიცხვი და გაიგეთ არის თუ არა ეს რიცხვი მარტივი(მარტივი არის რიცხვი, რომელიც მხოლოდ 1-ზე და საკუთარ თავზე იყოფა). შემდეგ კი დაბეჭდეთ 
#"This is prime number" თუ რიცხვი მარტივია, სხვა შემთხვევაში "This isn't prime number"
guess=0
guess=int(input("please enter number: "))
easy=1 and guess

if guess==easy:
    print("this is prime number")
else:
    print("This isn't prime number")