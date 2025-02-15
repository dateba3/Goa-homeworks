#2) დაიმატეთ ყველამ ერთმანეთი მეგობრებში და დაუმეგობრდით.
#ვისაც დაიმეგობრებთ, ამოიწერეთ მათი სახელები ტექსტურ ფაილში. level2.txt 
#და ატვირთეთ ეს გითჰაბზე

print("დავიმატე ყველა")






# 3) turtle-ის გამოყენებით დახატეთ კოშკი

from turtle import *
#make castle
width(7)
speed(30)

penup()
right(90)
forward(400)
left(90)
pendown()


forward(400)
left(180)
forward(800) 
right(90)
forward(300) #height of tower
right(90)
forward(100)
right(90)
forward(300)
right(180)
end_fill()

forward(250) #height of mini tower
right(90)
forward(60) 
right(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)


forward(190)
left(180)
forward(300)
right(90)
forward(100)
right(90)
forward(300)
right(180)
forward(250)
right(90)
forward(60)
right(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(250)
right(180)
forward(300)
right(90)
forward(100)
right(90)
forward(300)
right(180)
forward(250)
right(90)
forward(60)
right(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
right(90)
forward(60)
right(90)
forward(250)
right(180)
forward(300)
right(90)
forward(100)
right(90)
forward(300)
right(90)
forward(300)


#make castle door
forward(330)
right(90)
forward(160) #height of door
right(90)
forward(200)
right(90)
forward(160)
right(90)

penup()
left(180)
forward(330)
left(90)
forward(300)
pendown()

penup()
right(180)
forward(60)
right(90)
forward(60)
right(90)
forward(10)
pendown()

forward(200)
left(90)
forward(40)
right(90)
forward(120)
left(90)
forward(100)
left(90)
forward(120)
right(90)
forward(460)
right(90)
forward(120)
left(90)
forward(100)
left(90)
forward(120)
right(90)
forward(40)
left(90)
forward(200)

penup()
right(180)
forward(400)
right(90)
forward(200)
right(90)
forward(20)
pendown()


color("dark grey")
begin_fill()

left(90)
forward(340)
right(90)
forward(180)
right(90)
forward(340)
right(90)
forward(180)
end_fill()

color("black")
right(90)
forward(340)
right(90)
forward(180)
right(90)
forward(340)
right(90)
forward(180)

penup()
left(180)
forward(630)

pendown()

begin_fill()
color("dimgray")
left(90)
forward(20)
left(90)
forward(300)
left(90)
forward(100)
left(90)
forward(300)
left(90)


left(90)
color("dimgray")
begin_fill()
forward(300)
right(90)
forward(100)
right(90)
forward(300)
right(90)
forward(380)
right(90)
forward(300)
right(90)
forward(100)
right(90)
forward(300)

end_fill()

color("black")

right(90)
forward(100)
right(90)
forward(300)
right(90)
forward(100)
right(90)
forward(300)

left(90)
forward(280)
left(90)
forward(300)
left(90)
forward(100)
left(90)
forward(300)

left(90)
forward(400)
left(90)

color("dimgray")
begin_fill()

forward(300)
right(90)
forward(100)
right(90)
forward(300)

end_fill()

color("black")
left(180)
forward(300)
left(90)
forward(100)
left(90)
forward(300)
left(90)
forward(280)

color("dimgray")
begin_fill()
left(90)
forward(300)
right(90)
forward(100)
right(90)
forward(300)
end_fill()

color("black")
left(180)
forward(300)
left(90)
forward(100)
left(90)
forward(300)
left(90)
forward(100)

left(180)
forward(430)
left(140)
forward(180)
left(180)
forward(180)
left(40)
forward(200)

left(140)
forward(180)
left(180)
forward(180)
right(50)
forward(160)

penup()
forward(140)
left(90)
forward(430)
pendown()





exitonclick()

#4) Sololearn გაიარეთ Memory & Variables-ის ჩათვლით








# 4) შექმენი ცვლადი, სადაც შეინახავთ თქვენს სახელს და დაბეჭდეთ ის
name="Dato"
print(name)

# 5) თქვენი სიტყვებით აღწერეთ, თუ რა არის ცვლადი და რისთვის გამოიყენება ის
#ცვლადი არის მონაცემთა შესანახი ყუთი, და ის გამოიყენება მონაცემთა შესანახად და შემდეგ გამოსაყენად.
#მაგ:თუ გვაქვს ადამიანის ასაკი ის უნდა შვინახოთ ცვლადში age რომ შემდეგ უფრო მარტივად ვნახოთ მისი მნიშვნელობა