# Elias Woldie
# Python –-> File IO
# This program quizzes the user on the state capitals

import random


def read_file_to_dict(file_name):
    """
    This function reads the text file and converts it into a dictionary as a key:value pair.

    Argument: read_file_to_dict(file_name): takes the data in the text file
    Return: a dictionary of key:value or State:Capital pair
    """
    # Opening and reading the text file
    file = open(file_name)
    names = file. readlines()
    # creating a dictionary to store the data in the text file
    dict = {}
    for line in names:
        (state, capital) = line.strip().split(',')
        dict[(state)] = capital
    return dict


def get_random_state(states):
    """
    This Function Convert the dictionary to a list of key:value pairs, then choose a random key:value     pair from the list and return it. 

    Argument: get_random_state(states): takes the dictionary as key:value pair
    Return: the correct state:capital pair that will be used for each question
    """
    # Converting the dictionary to a list of key:value pairs,
    dictList = list(states.items())
    for i in states:
        # choosing a random key:value pair from the list
        randChoice = random.choice(dictList)
    return randChoice


def get_random_choices(states, correct_capital):
    """
    This function takes the dictionary and converts it into to a list of values to choose 3 incorrect choices from created list and randomly shuffles it along with the correct value. 

    Argument: get_random_choices (states): takes the dictionary as key:value pair
              get_random_choices (correct_capital): passes the capital of the correct answer
    Return: the randomly shuffled list
    """
    # Taking the dictionary and coneverting it into a list of values/Capitals
    capitalValues = list(states.values())
    # Randomly choosing and shuffeling the list
    sampled_list = random.sample(capitalValues, 3)
    randChoice = [correct_capital, *sampled_list]
    random.shuffle(randChoice)
    return randChoice


def ask_question(correct_state, possible_answers):
    """
    This function displays the question to the user and the four possible answers as a multiple choice and validates that the inputs range are from A-D. It then converts the input to 0-3 (A=0, B=1, C=2, D=3) 

    Argument: ask_question(correct_state): passes the correct state from get_random_state
              ask_question(correct_state): passes the randomly shuffled choice from get_random_choices
    Return: the integer value of the converted input
    """

  # Asking the user and giving the choices
    print("    A. " + possible_answers[0] + "    " + "B. " + possible_answers[1] +
          "    " + "C. " + possible_answers[2] + "    " + "D. " + possible_answers[3])
    user_choice = input("Enter selection: ").capitalize()
  # Validating the input is in between A-D
    while True:
        if user_choice in ['A', 'B', 'C', 'D']:
            # converting the input to 0-3
            if user_choice == 'A':
                user_choice = 0
            elif user_choice == 'B':
                user_choice = 1
            elif user_choice == 'C':
                user_choice = 2
            elif user_choice == 'D':
                user_choice = 3
            break
        else:
            print("Invalid input. Input choice A-D")
            user_choice = input("Enter selection: ").capitalize()

    return user_choice


def main():
    """
    This function read in the file then have a loop that repeats 10 times, one for each of the quiz 
questions. Calls all the declared functions above and passes the appropriate arguments
    """
    print("- State Capitals Quiz – ")
    file = "StateCapitals.txt"
    counter = 0  # To count the correct results
    question = 1  # To count the question
    # Looping the question 10 times
    for i in range(1, 11):
        dictionary = read_file_to_dict(file)
        randStates = get_random_state(dictionary)
        # setting the 2nd index from get_random_state as the capital
        correctCapitals = randStates[1]
        # setting the 1st index from get_random_state as the State
        correctStates = randStates[0]
        correctDict = get_random_choices(dictionary, correctCapitals)
        print(question, ".", "The capital of ", correctStates, " is: ")
        choices = ask_question(correctStates, correctDict)
        # Matching the answer
        if correctDict[choices] == correctCapitals:
            print("Correct!")
            counter = counter + 1
        else:
            print("Incorrect!  The correct answer is: ", correctCapitals)
        question = question + 1

    print("End of test. You got", counter, "correct.")


main()
