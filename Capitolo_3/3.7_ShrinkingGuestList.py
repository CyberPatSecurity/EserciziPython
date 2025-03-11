famous_person = ['Linus Torvalds', 'Albert Einstein','Jimi Hendrix']

message_1 = f"Hi {famous_person[0]}, i'd like to share a computer science lesson with you!"
print(message_1)
message_2 = f"Hi {famous_person[1]}, i'd like to share a math lesson with you!"
print(message_2)
message_3 = f"Hi {famous_person[2]}, i'd like to share a jam session with you!\n"
print(message_3)

print("Albert Einstein can't partecipate at my invitation\n")
famous_person[1] = 'Chatgpt'
message_1 = f"Hi {famous_person[0]}, i'd like to share a computer science lesson with you!"
print(message_1)
message_2 = f"Hi {famous_person[1]}, i'd like to share a math lesson with you!"
print(message_2)
message_3 = f"Hi {famous_person[2]}, i'd like to share a jam session with you!\n"
print(message_3)
print("Hi people, i found another dinner table and i'd like to share the dinner with more people!\n")

famous_person.insert(0,'Luisa Fancelli')
famous_person.insert(2,'Bianca Egidi Fancelli')
famous_person.append('Coky\n')
#print(famous_person)
message_1 = f"Hi {famous_person[0]}, i'd like to share a computer science lesson with you!"
print(message_1)
message_2 = f"Hi {famous_person[1]}, i'd like to share a math lesson with you!"
print(message_2)
message_3 = f"Hi {famous_person[2]}, i'd like to share a jam session with you!"
print(message_3)
message_4 = f"Hi {famous_person[3]}, i'd like to share a jam session with you!"
print(message_4)
message_5 = f"Hi {famous_person[4]}, i'd like to share a jam session with you!"
print(message_5)

print("Hello people, i'm so sorry because the table won't arrive in time and i have space only for two person\n")
print(famous_person)
first_remove = famous_person.pop(1)
print(f"I'm so sorry {first_remove.title()} i can't invite you for the dinner!")
second_remove = famous_person.pop(2)
print(f"I'm so sorry {second_remove.title()} i can't invite you for the dinner!")
third_remove = famous_person.pop(2)
print(f"I'm so sorry {third_remove.title()} i can't invite you for the dinner!")
fourth_remove = famous_person.pop(2)
print(f"I'm so sorry {fourth_remove.title()} i can't invite you for the dinner!\n")
print(f"Hello darling, {famous_person[0]} and {famous_person[1]} i'm glad to stay with you!\n")

del famous_person[0]
del famous_person[0]
print(famous_person)