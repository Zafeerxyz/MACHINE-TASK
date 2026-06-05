text = "Data Science With Python" 
new_text = text.lower()
print(new_text)

words = new_text.split()
counts = len(words) #using len()

print("count", counts)
count = 0
for i in words:
    count +=  1
print("Number of words with out len ",count) #without len()