#2) კომენტარებით ახსენით რა არის slicing

#slicing არის გზა რომ აიღო ნაწილი სიიადან მაგ:
#name=[დასაწყისი:დასასრული:ნაბიჯი]

#3) გაიმეორეთ range ფუნქცია და გააკეთეთ 3 მაგალითი
for i in range(5):             #1
    print(i)

for i in range(3,9):           #2
    print(i)

for i in range(10,0,-1):       #3
    print(i)

#4) შექმენით 10 ელემენტიანი სია და slicing-ის გამოყენებით დაბეჭდეთ სიის მე-2, მე-5 და მე-8 ელემენტი

sia=[11,22,33,44,55,66,77,88,99,100]
sia1=[sia[1], sia[4], sia[7]]
print(sia1)
#5) slicing-ის გამოყენებით დაბეჭდეთ იგივე სიის მე-3 ელემენტიდან დაწყებული სიის ყველა ელემენტი

sia3=sia[2:]
print(sia3)
