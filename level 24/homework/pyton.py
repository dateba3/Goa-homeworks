#2) მომხმარებელს შემოატანინე 5 რიცხვი და დაბეჭდეთ მათი ნამრავლი
for i in range(5):
    number=int(input("please enter number: "))
    product=number
print("namravli aris ", product)
#3) დაბეჭდეთ 50-დან 10-ის ჩათვლით ყოველი მეორე რიცხვი.
for i in range(50, 9, -2):
    print(i)

#4) შექმენით პროგრამა, სადაც მომხმარებელი გამოიცნობს ჩაფიქრებულ რიცხვს 1-დან 10-ის ჩათვლით.
#დაგჭირდებათ ცვლადი, სადაც შეინახავთ ნებისმიერ რიცხვს 1-დან 10-მდე(ეს იქნება ჩაფიქრებული რიცხვი).
#while loop-ის გამოყენებით მომხმარებელს იქამდე შემოატანინეთ რიცხვი სანამ არ გამოიცნობს. მომხმარებელს ექნება 3 ცდა ჩაფიქრებული რიცხვის გამოსაცნობად.
#ყოველი არასწორი რიცხვის შეყვანისას დაბეჭდეთ "Wrong number" და აცნობეთ მომხმარებელს რამდენი ცდა დარჩა.
#თუ გამოიცნო, გათიშეთ while ციკლი და დაბეჭდეთ You win, ხოლო თუ ცდები ამოეწურა ასევე გათიშეთ while ციკლი და დაბეჭდეთ "You lose"

number=3
tries=0
max_tries=3
guess=0
while tries<max_tries and guess != number:
    guess=int(input("please enter number (0-10):"))
    if guess==number:
        print("you win!")
    else:
        tries+=1
        if tries<max_tries:
            print("you are wrong")
        else:
            print("you lose")
    
