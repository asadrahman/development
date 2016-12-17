#!/bin/env python
# randomQuizGenerator.py - creats quizzes with questions and answers
import random
import re

from Capitals import Capitals

def get_valid_response(input_text, validate_list):
	check_response = []

	while not check_response:
		response = input(input_text).upper()
		if response == 'Q':
			return None

		check_response = [i for i in validate_list if i == response]
		if check_response:
			return response



new_capitals = Capitals()
list_of_capitals = sorted(new_capitals.get_capitals())

countries = new_capitals.get_random_countries()
choices=list('ABCD')

country_enumerated = [ str(i + 1) for i, j in enumerate(list_of_capitals)]

country_number = get_valid_response("How many countries to test? (q to quit)", country_enumerated)
if country_number is None:
	country_number = 0
else:
	country_number = int(country_number)


number_correct = 0
number_incorrect = 0


for question_number in range(country_number):
	print("\n%s. What is the capital of %s?\n" %(question_number + 1, countries[question_number]) )
	
	answers = new_capitals.get_answers(countries[question_number])
	correct_answer = new_capitals.get_capital(countries[question_number])
	choice_list = dict(zip(choices, answers))

	for choice, city in sorted(choice_list.items()):
		print('    %s. %s\n' %(choice, city))
	
	response = get_valid_response("Enter [A,B,C,D ( q to quit)] >", choices)

	if not response:
		break

	if choice_list[response] == correct_answer:
		number_correct += 1
	else:
		number_incorrect += 1
		print("Your answer is incorrect %s. %s " %(response, choice_list[response]))

	print("Answer is correct %s. %s" %(list(choice_list.keys())[list(choice_list.values()).index(correct_answer)], correct_answer))
	print("Your score so far is %d" %(number_correct))


	
print("End of game, you scored %d out of %d" %(number_correct, country_number))










