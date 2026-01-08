# kbc
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C",
        "amount": 1000
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B",
        "amount": 2000
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Jane Austen"],
        "answer": "C",
        "amount": 3000
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D",
        "amount": 4000
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A) Au", "B) Ag", "C) Fe", "D) Hg"],
        "answer": "A",
        "amount": 5000
    }
]
total_amount =0
for q in questions:
    
    print(q["question"])
    print(q["options"])
    user_answer = input("Your answer (A/B/C/D): ").strip().upper()
    if user_answer == q["answer"]:
        total_amount += q["amount"]
        print(f"Correct! You've won ${total_amount}\n")
    else:
        print(f"Wrong answer. The correct answer was {q['answer']}. You leave with ${total_amount}\n")
        break