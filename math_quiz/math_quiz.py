import random


def generate_random_integer(min_val, max_val):
    """
    Generate a random integer between min_val and max_val (inclusive).
    """
    return random.randint(min_val, max_val)


def generate_random_operator():
    """
    Generate a random arithmetic operator (+, - *).
    """
    return random.choice(['+', '-', '*'])


def perform_operation(num1, num2, operator):
    """
    Perform the arithmetic operation based on the given numbers and operator.
    """
    result = 0
   
    if operator == '+': 
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else: 
        result = num1 * num2
        
    return f"{num1} {operator} {num2}", result

def math_quiz():
    """
    Main function for the Math Quiz Game.
    """
    score = 0
    total_questions = 3
    
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5) 
        operator = generate_random_operator()

        problem, answer = perform_operation(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
