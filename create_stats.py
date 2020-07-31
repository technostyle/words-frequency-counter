#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################################
# Данный скрипт записывает в папку статистики файлы c частотностью слов из книг данной
# директории.
#
# Для работы требуется указать названия папки с текстовыми файлами и папки статистики. 
######################################################################################

import os

# ----------------------------
#	  START OF BOOK ANALYSE
# ----------------------------

def cyr_lower(letter):
	big = "ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
	small = "ёйцукенгшщзхъфывапролджэячсмитьбю"

	return small[big.index(letter) : big.index(letter) + 2]

def clear_word(word):
	res = ""
	for i in range(len(word) - 1):
		letter = word[i : i + 2]
		if 'А' <= letter and letter <= 'Я':
			res += cyr_lower(letter)
		if 'а' <= letter and letter <= 'я':
			res += letter

	return res


def get_all_words_in_text(text_file):
	words = []

	file = open(text_file, "r")
	for line in file:
		for word in str(line).split(" "):
			clr = clear_word(word)
			if len(clr) > 0:
				words.append(clr)
	file.close()

	return words

def get_all_words_frequency_in_text(text_file):
	res = {'' : 0}
	last_word = ''

	words = get_all_words_in_text(text_file)
	words.sort()
	length = len(words)
	print "total words: " + str(length)

	for i in range(len(words)):
		if last_word == words[i]:
			res[last_word] += 1
		else:
			last_word = words[i]
			res[last_word] = 1


	for key in res:
		res[key] = float(res[key]) / length * 100

	return res

def output_frequency_form_book(input_file, output_file):
	frequency = get_all_words_frequency_in_text(input_file)
	
	pairs = []
	for word in frequency.keys():
		pairs.append(word + ":" + str(frequency[word]))
	pairs.sort()

	out_f = open(output_file, "w")
	for item in pairs:
 		out_f.write(item + "\n")
	out_f.close()	

# ----------------------------
#	  END OF BOOK ANALYSE
# ----------------------------


def create_stats(books_path, stats_path):
	for book in os.listdir(books_path):
		print "---------------"
		print book
		output_frequency_form_book(input_file = books_path + book, output_file = stats_path + book)

