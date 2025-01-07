
# KBC Game - Basic Version
questions = [
    "What is the capital of India?",
    "Which is the largest planet in the Solar System?",
    "What is the square root of 64?",
    "Who is known as the father of the Indian Constitution?",
    "Which element has the chemical symbol 'O'?"
]

options = [
    ["1. Mumbai", "2. New Delhi", "3. Chennai", "4. Kolkata"],
    ["1. Earth", "2. Venus", "3. Jupiter", "4. Saturn"],
    ["1. 6", "2. 7", "3. 8", "4. 9"],
    ["1. Mahatma Gandhi", "2. B. R. Ambedkar", "3. Jawaharlal Nehru", "4. Subhash Chandra Bose"],
    ["1. Oxygen", "2. Gold", "3. Osmium", "4. Ozone"]
]

answers = [2, 3, 3, 2, 1]  # Correct option numbers

print("Welcome to KBC! Answer by typing the option number (1-4). Good luck!\n")


win=0
for i in range(len(questions)):
    print(questions[i])
    for j in options[i]:
        print(j)

    inputu=int(input("Enter your answer here:-------"))

    if inputu==answers[i]:
        win+=1000
        print("yo won ",win,"amount")
    else:
        print("sorry")    
        break