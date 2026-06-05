students = { "Asha": 78, "Rahul": 65, "Meena": 92, "Kiran": 55 }

for name,mark in students.items():
    
    
    if mark > 70:
        
        highest = mark
        high_scorer = name
        
    
print(high_scorer) 

top_student = max(students , key =students.get)

print(top_student ,"with marks", students[top_student])