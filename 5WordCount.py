Sentence = "Data science is interesting"

new = 0
listed_sentence = Sentence.split()
print(listed_sentence)
for i in listed_sentence:
    new += 1                #using loop
    
total = len(listed_sentence) #using method
print(total)
print(new)