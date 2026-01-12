print("started ")


quiz = [{"questions":"What is the capital of France?","options":"A) Paris\nB) London\nC) Berlin\nD) Madrid","answer":"A"},
        {"questions":"What is achieved after mixing yellow and red?","options":"A) Green\nB) Orange\nC) Purple\nD) Brown","answer":"B"},
        {"questions":"What is the largest planet in our solar system?","options":"A) Earth\nB) Jupiter\nC) Saturn\nD) Mars","answer":"B"}]
score = 0
question_num = 1
guess = 0

for que in quiz:
    print(f"Question-{question_num} : " , que["questions"])
    question_num += 1
    print(que["options"])
    user_answer = input("Please Enter Your Answer : ").upper()
    if user_answer == que["answer"]:        
        print("Correct !")
        score += 1
        guess += 1
    else:
        print("Incorrect !")
        print(f"Answer is : {que["answer"]}")
        guess += 1

print(f"Your Final Score is {score}")
print(f"Wrong Answers : {guess - score}")




