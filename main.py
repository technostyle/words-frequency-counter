#!/usr/bin/env python3
# -*- coding: utf-8 -*-

######################################################################################
# Данный скрипт записывает в выходной файл частоты всех слов из книг данной директории.
#
# Для работы требуется загрузить текстовые файлы в папку ./books 
######################################################################################


import create_stats
import merge_stats
import test
import os

folder_path = os.getcwd()
books_path = folder_path + '/books/'
stats_path = folder_path + '/stats/'
out_file = "words_freq.txt"

if 'stats' in os.listdir(folder_path):
	for file in os.listdir(stats_path):
		os.remove(stats_path + file)
	# os.rmdir(stats_path)	
else:
	os.mkdir(stats_path)

create_stats.create_stats(books_path, stats_path)
merge_stats.output_total_stats(stats_path, out_file)
test.check_files(stats_path, out_file)
