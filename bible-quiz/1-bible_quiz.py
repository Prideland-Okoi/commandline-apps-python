#!/usr/bin/python3
import json
import random


def load_questions(filename):
    with open(filename, "r") as file:
        data = json.load(file)
    return data["questions"]


def save_user_data(filename, user_data):
    with open(filename, "w") as file:
        json.dump(user_data, file)


def load_user_data(filename):
    try:
        with open(filename, "r") as file:
            user_data = json.load(file)
    except FileNotFoundError:
        user_data = {}
    return user_data


def ask_question(question):
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i + 1}. {option}")
    user_answer = input("Your answer: ")
    if user_answer == question["answer"]:
        print("Correct Entry!")
        return 1
    else:
        print(f"Incorrect. The correct answer is {question['answer']}.")
        return 0


def run_quiz(questions, level):
    random.shuffle(questions)
    score = 0
    for question in questions:
        if question["level"] == level:
            score += ask_question(question)
    return score


def register_user(user_data):
    username = input("Enter a username: ")
    if username in user_data:
        print("Username already taken. Please choose another.")
        return register_user(user_data)
    password = input("Enter your password: ")
    user_data[username] = {"password": password, "level": 1, "score": 0}
    return username


def sign_in_user(user_data):
    username = input("Enter your username: ")
    if username not in user_data:
        print("Username not found. Please try again or register a new account.")
        return sign_in_user(user_data)
    password = input("Enter your password: ")
    if password != user_data[username]["password"]:
        print("Password is incorrect. Please try again.")
        return sign_in_user(user_data)
    return username


def main():
    questions_filename = "questions.json"
    user_data_filename = "user_data.json"

    questions = load_questions(questions_filename)
    user_data = load_user_data(user_data_filename)

    print("Welcome to Pride Bible Quiz")
    while True:
        action = input(
            "Enter 'r' to register a new account, 's' to sign in or 'q' to quit: ")
        if action == "r":
            current_user = register_user(user_data)
            break
        elif action == "s":
            current_user = sign_in_user(user_data)
            break
        elif action == "q":
            return
        else:
            print("Invalid input. Please try again.")

    while True:
        level = user_data[current_user]["level"]
        if level > 10:
            print(
                "Congratulations! You have completed all levels of the Pride Bible Quiz!")
            action = input(
                "Enter 'r' to restart from level 1 or 'q' to quit: ")
            if action == "r":
                user_data[current_user]["level"] = 1
                user_data[current_user]["sore"] = 0
                continue
            elif action == "q":
                break
            else:
                print("Invalid input. Please try again.")
                continue
        score = run_quiz(questions, level)
        user_data[current_user]["score"] += score
        print(f"Your current score is {user_data[current_user]['score']}.")
        if score == len([q for q in questions if q["level"] == level]):
            user_data[current_user]["level"] += 1
            print(
                f"You have advanced to level {user_data[current_user]['level']}!")
        action = input(
            "Enter 'c' to continue playing, 'r' to restart from level 1 or 'q' to quit: ")
        if action == "r":
            user_data[current_user]["level"] = 1
            user_data[current_user]["score"] = 0
        elif action == "q":
            break
        elif action != "c":
            print("Invalid input. Please try  again.")
    save_user_data(user_data_filename, user_data)
    print("Thanks for playing the Pride Bible Quiz!")


if __name__ == "__main__":
    main()
