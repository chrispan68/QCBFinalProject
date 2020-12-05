from motifscoring import scoreMotif
import pandas as pd
import numpy as np

# To be finished tomorrow (basically just call all of the functions)
def scoreAll():
	print("Long background: ")
	with open('long_motif/motif.json') as f:
		template = pd.read_json(f)
	with open('long_motif/meme.json') as f:
		meme = pd.read_json(f)
	with open('long_motif/GAME.json') as f:
		game = pd.read_json(f)
	memeScore = scoreMotif(template, meme, 0.25, 0.25, 0.25, 0.25)
	gameScore = scoreMotif(template, game, 0.25, 0.25, 0.25, 0.25)
	print(memeScore)
	print(gameScore)

def main():
	scoreAll()


if __name__ == "__main__":
	main()