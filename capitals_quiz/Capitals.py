#!/bin/env python
import json
import random
from pprint import pprint


class Capitals(object):
	"""List of Capitals"""
	def __init__(self, filename = 'country_capitals.json'):
		self.answers = None
		with open(filename, 'r') as f:
			self.capitals = json.load(f)
		
	def print_capitals(self):
		pprint(self.capitals)

	def get_capitals(self):
		return self.capitals

	def get_random_countries(self):
		countries = list(self.capitals.keys())
		random.shuffle(countries)

		return countries

	def get_answers(self, country):

		self.correct_answer = self.capitals[country]
		wrong_answers = list(self.capitals.values())
		del wrong_answers[wrong_answers.index(self.correct_answer)]
		wrong_answers = random.sample(wrong_answers, 3)
		self.answers = wrong_answers + [self.correct_answer]
		random.shuffle(self.answers)
		
		return self.answers

	def get_capital(self, country):
		return self.capitals[country]

	def get_correct_answer(self):
		return self.correct_answer

if __name__ == '__main__':
	capitals = Capitals()
	capitals.print_capitals()