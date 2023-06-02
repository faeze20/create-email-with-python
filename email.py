import random
import string
emails=[]
passwords=[]
word_length = int(input("enter number"))  # تعیین طول کلمه

# create words
random_word = ''.join(random.choices(string.ascii_lowercase, k=word_length)) 
# print("کلمه تصادفی: ", random_word.encode('utf-8').decode('utf-8'))


# create characters
characters = string.ascii_lowercase + string.digits + '_'
# print("لیست کاراکترها: ", characters)

# create numbers
numbers = list(range(10))




num=int(input("enter a number"))
for i in range(num):
    email = random_word + random.choice(characters) + str(random.choice(numbers)) + "@" + random.choice(["gmail.com","yahoo.com"])
    emails.append(email)
    password=random_word + random.choice(characters) + str(random.choice(numbers))
    passwords.append(password)
print(list(zip(emails,passwords)))    
with open('text.txt',"a") as file:
    file.write("\n".join([str(item.index(),item) for item in zip(emails, passwords)]) + "\n")
    file.close()
with open("text.txt",'r') as file:
    s=file.read()
    print(s)        