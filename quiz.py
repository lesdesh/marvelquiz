from gamecomponents.quizquestions import question
from gamecomponents import gamevars, quiztally

answer1 = question["q1"][input(question["q1"]["question"])]
print(answer1)

gamevars.quiztotal += answer1
print("+++++++++\n")

answer2 = question["q2"][input(question["q2"]["question"])]
print(answer2)

gamevars.quiztotal += answer2
print("+++++++++\n")

answer3 = question["q3"][input(question["q3"]["question"])]
print(answer3)

gamevars.quiztotal += answer3
print("+++++++++\n")

answer4 = question["q4"][input(question["q4"]["question"])]
print(answer4)

gamevars.quiztotal += answer4
print("+++++++++\n")

answer5 = question["q5"][input(question["q5"]["question"])]
print(answer5)

gamevars.quiztotal += answer5
print("+++++++++\n")

answer6 = question["q6"][input(question["q6"]["question"])]
print(answer6)

gamevars.quiztotal += answer6
print("+++++++++\n")


print("total so far: " + str(gamevars.quiztotal)+"\n")

quiztally.total(gamevars.quiztotal)
