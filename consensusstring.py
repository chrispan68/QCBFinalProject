import pandas as pd

def consensus(sequence):
	return sequence.idxmax(axis = 1)

def main():
	with open('control/MEME.json') as f:
		game = pd.read_json(f)
	consensusGame = consensus(game)
	with open('control/motif.json') as f:
		motif = pd.read_json(f)
	consensusMotif = consensus(motif)
	print(consensusGame)
	print(consensusMotif)
	print(all(consensusMotif == consensusGame))

if __name__ == "__main__":
	main()