number_of_subject = int(input("Enter number of students: "))

report_card = []

total_score = 0

for i in range(number_of_subject):
    
    subject = input("Enter Subject Name Or enter \"end\" to stop the program: ")
    
    if subject =="end": break
    
    score = float(input("Enter Score: "))
    
    report_card.append({"subject": subject, "score" : score})
    
    total_score = total_score + score
    

for report in report_card:
    print("{} | {}".format(report["subject"], report["score"]))
    


print("Total Score: ", total_score)
print("Average Score: ", total_score / len(report_card))
