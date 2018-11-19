import os
import sys

from operator import itemgetter
from collections import Counter
from multiprocessing import Process, Manager

def pprint(matrix):
	for row in matrix:
		print(row)

def column(m, i):
	return list(map(itemgetter(i), m))

def row_and_column(m, i):
	ret = dict()
	ret['row'] = m[i][:]
	ret['column'] = column(m, i)
	return ret

def solver(rc, find, found):
	found[os.getpid()] = []
	for word in find:
		freq = Counter(word)
		row = Counter(rc['row'])
		column = Counter(rc['column'])
		in_row = True
		in_column = True

		for letter in freq.keys():
			if letter in row.keys():
				in_row = in_row and (freq[letter] <= row[letter])
			else:
				in_row = False

			if letter in column.keys():
				in_column = in_column and (freq[letter] <= column[letter])
			else:
				in_column = False

		if (in_row or in_column):
			found[os.getpid()] += [word]

def word_counter(found):
	s = set()
	for process in found.keys():
		for word in found[process]:
			s.add(word)
	return s

if __name__ == '__main__':
	with Manager() as manager:
		size = int(input())
		matrix = []
		for _ in range(size):
			matrix.append(list(input()))
		
		find = []
		found = manager.dict()

		for _ in range(int(input())):
			find += [input()]

		processes = []

		for position in range(size):
			processes += [Process(target=solver, args=(row_and_column(matrix, position), find, found))]
			processes[position].start()

		for process in processes:
			process.join()

		w = word_counter(found)

		print(len(w))
		for word in w:
			print(word)