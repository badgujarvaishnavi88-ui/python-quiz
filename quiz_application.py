# Quiz Application


questions = [

{
"question":"What is the capital of India?",
"answer":"delhi"
},

{
"question":"Which language is used for web styling?",
"answer":"css"
},

{
"question":"What is 5 + 5?",
"answer":"10"
},

{
"question":"Which keyword is used to create a function in Python?",
"answer":"def"
}

]



score = 0


print("----- Python Quiz Application -----")



for q in questions:


    print("\n"+q["question"])


    user_answer = input("Your answer: ")



    if user_answer.lower() == q["answer"]:


        print("Correct Answer")

        score += 1


    else:

        print("Wrong Answer")




print("\n----- Result -----")


print("Total Questions:", len(questions))

print("Correct Answers:", score)


percentage = (score / len(questions))*100


print("Percentage:", percentage)



if percentage >= 75:

    print("Excellent Performance")


elif percentage >= 50:

    print("Good Performance")


else:

    print("Need More Practice")