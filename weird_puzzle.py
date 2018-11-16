from multiprocessing import Process, Manager
import sys
import os

class Puzzle:
	def __init__(self, matrix, diag, words, matches):
		self.matrix = matrix
		self.diag = diag
		self.words = words
		self.matches = matches

	def __iter__(self):
		return self

	def __next__(self):
		if self.matches['not found'] == 0 or len(diag) == 0:
			raise StopIteration
		return diag.pop()

def pprint(matrix):
	for row in matrix:
		print(row)

if __name__ == '__main__':
	with Manager() as manager:
		with Pool(processes=sys.argv[1]) as pool:
			size = int(input())
			diag = manager.list(i for i in range(size))
			matrix = []
			for _ in range(size):
				matrix.append(list(input()))
			
			matches = manager.dict([
						('not found', []),
						('found', [])
						])
			for _ in range(int(input())):
				matches['not found'] += [input()]

			puzzle = Puzzle(matrix, diag, words, matches)
			pool.map(solver, puzzle)

			processes = [Process(target=solver, args=(puzzle,)) for i in range(sys.argv[1])]

