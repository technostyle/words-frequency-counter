#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#############################################################################
# Функция считает, действительно ли в сумма всех частот равна 100%.
# Проверяются все файлы в папке статистики и результирующий файл с частотами.
#############################################################################
import os

def check_files(path_to_stats, res_file_name):

	print "----------------------------- testing ---------------------------------"
	print "counting sum"
	# files = os.listdir( path)
	data = {}

	for file in os.listdir(path_to_stats):
		count = 0
		f = open(path_to_stats + file, "r")
		for line in f:
			count += float(line.split(":")[1])
		print file + " ------- sum = " + str(count) + "%"
		data[file] = count
		f.close()

	count = 0
	f = open(res_file_name, "r")
	for line in f:
		count += float(line.split(":")[1])
	print res_file_name + " ------ sum = " + str(count)  + "%"
	data[res_file_name] = count
	f.close()

	test = True
	for key in data:
		if data[key] is 100:
			test = False

	if test:
		print "----------------------------- ok ---------------------------------"
