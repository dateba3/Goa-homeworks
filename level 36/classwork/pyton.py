#1) მომხმარებელს შემოატანინეთ სახელი და დაბეჭდეთ ის uppercase-ში
name=((input("please enter name: ").upper()))
print(name.upper())
#2) იგივე სახელი დაბეჭდეთ lowercase-ში
print(name.lower())

#3) იგივე სახელი დაბეჭდეთ ისე, რომ მისი პირველი ასო იყოს uppercase-ში დაწერილი, ხოლო დანარჩენი lowercase-ში
print(name.capitalize())

#4) შექმენით ცვლადი, სადაც შეინახავთ ნებისმიერ სიტყვას. მომხმარებელს შემოატანინეთ სიმბოლო, რომლის ინდექსიც უნდა იპოვოთ სთრინგში და დუბეჭდოთ შემდეგი ფორმატით "a - 0"
#თუ მომხმარებელმა ჩაწერა ისეთი სიმბოლო, რომელიც არ არის სიტყვაში. დაუბეჭდეთ რომ "This symbol is not in word"

txt="python"

finding=input(f"Enter a symbol you want to find in the text: {txt} ")

found=txt.find(finding)

if finding not in txt:
    print("This symbol is not in a text")
else: print(f"{finding} - {found}")