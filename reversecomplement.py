# Written by Charlie Vrattos

import pandas as pd

def generateComplement(sequence):
	sequence.columns = ['T', 'A', 'G', 'C']
	sequence = sequence[::-1].reset_index(drop=True)
	return sequence

def main():
	with open('control/GAME.json') as f:
		game = pd.read_json(f)
	generateComplement(game)

if __name__ == "__main__":
	main()