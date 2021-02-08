


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What is output for −' ' in 'python' ?\n(a) Python\n(b)False\n(c)Name error\n(d)None\n\n",
     "What is the output of following code −\n[ (a,b) for a in range(3) for b in range(a) ]\n(a)[ (1,0),(2,1),(3,2)]\n(b)[ (0,0),(1,1),(2,2)]\n(c)[(1,0),(2,1),(2,1)]\n(d)[ (1,0),(2,0),(2,1)]\n\n",
     "Syntax error in python is detected by _________at _______?\n(a)compiler/ compile time\n(b)interpreter/ run time\n(c)compiler/ run time\n(d)interpreter/ compile time\n\n",
     "Which of these is not a core data type?\n(a) Lists\n(b) Dictionary\n(c) Tuples\n(d) Class\n\n",
     "Which of the following function convert a string to a float in python?\n(a)int(x [,base])\n(b)long(x [,base] )\n(c)float(x)\n(d)str(x)\n\n",
     "What is the output of the following code :print 9//2 \n (a)4.5 \n(b)4.0 \n(c)4 \n(d)Error\n\n",
]

questions = [
     Question(question_prompts[0], "d"),
     Question(question_prompts[1], "d"),
     Question(question_prompts[2], "b"),
     Question(question_prompts[3], "d"),
     Question(question_prompts[4], "c"),
     Question(question_prompts[5], "c"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))
     if score>=4:
            print("U did it,\n Congratulations...")
     else:
            print("U loss,\nTry again")
run_quiz(questions)

