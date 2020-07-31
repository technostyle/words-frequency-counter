#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########################################################################################
# Данный скрипт объединяет фаилы с частотностью и выводит общую частотность.
# 
# Для работы требуется указать название папки статистики. 
# ПРЕДУПРЕЖДЕНИЕ: в папке статистики должны бать только нужные файлы!
#########################################################################################

import create_stats
import os

# stats_path = folder_path + '/stats/'

def get_stat_list(fname):
	res = []

	file = open(fname, "r")
	for line in file:
		pair = line.split(":")
		res.append([ pair[0], float(pair[1]) ])
	file.close()

	return res

def merge_stats(stats_path):
	res = {'' : 0}
	all_stats = [] # [ [word, freq], ... ]

	print "merging common data..."
	for stat_file in os.listdir(stats_path):
		all_stats += get_stat_list(stats_path + stat_file)

	all_stats.sort()
	last_word = ''

	print "counting common statistics..."
	for i in range(len(all_stats)):
		cur_word = all_stats[i][0] #['word']
		cur_freq = all_stats[i][1] #['freq']

		if last_word == cur_word:
			res[last_word] += cur_freq
		else:
			last_word = cur_word
			res[last_word] = cur_freq

		# print "progress: " + str(i) + " of " + str(length)

	total = len(os.listdir(stats_path))
	print "deviding..."
	for key in res:
		res[key] /= total


	return res

def output_total_stats(input_stats_path, output_file_name):
	print "-----------------"
	res = []

	int_dict = merge_stats(input_stats_path)
	for key in int_dict:
		res.append(key + ":" + str(int_dict[key]))

	print "sorting statistics..."
	res.sort()

	print "outputing to >>> " + output_file_name   
	file = open(output_file_name, "w")
	for item in res:
		file.write(item + "\n")
	file.close()

