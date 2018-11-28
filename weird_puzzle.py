# mpirun -n 4 python3 mpi.py

import os
import sys

from mpi4py import MPI
from operator import itemgetter
from collections import Counter
from socket import gethostname

def column(m, i):
	return list(map(itemgetter(i), m))

def position_info(m, i, find):
	ret = dict()
	ret['row'] = m[i][:]
	ret['column'] = column(m, i)
	ret['find'] = find
	ret['found'] = []
	return ret

def data_preprocessing_root(size):
	matrix_size = int(input())
	matrix = []
	for _ in range(matrix_size):
		matrix.append(list(input()))
	
	find = []
	for _ in range(int(input())):
		find += [input()]

	unscatterable = [position_info(matrix, i, find) for i in range(matrix_size)]
	scatterable = [[] for i in range(size)]

	for index, position in enumerate(unscatterable):
		scatterable[index % size].append(position)

	return scatterable

def solver(scatterable):
	for position in scatterable:
		row = Counter(position['row'])
		column = Counter(position['column'])
		
		for word in position['find']:
			freq = Counter(word)
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
				position['found'] += [word]

# ----------------- MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
	scatterable = data_preprocessing_root(size)
else:
	scatterable = None

# scatter for magic
scatterable = comm.scatter(scatterable, root=0)

# do the magic
print(gethostname())
solver(scatterable)

# gather the magic
scatterable = comm.gather(scatterable, root=0)

if rank == 0:
	found = []
	for position in scatterable:
		for chunk in position:
			found += chunk['found']

	found = list(set(found))
	
	print(len(found))
	for word in found:
		print(word)

else:
	scatterable = None
