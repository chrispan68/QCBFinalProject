from motifscoring import scoreMotif
import pandas as pd
import numpy as np

# To be finished tomorrow (basically just call all of the functions)
def scoreAll():
	print("Long motif: ")
	with open('long_motif/motif.json') as f:
		template = pd.read_json(f)
	with open('long_motif/meme.json') as f:
		meme = pd.read_json(f)
	with open('long_motif/GAME.json') as f:
		game = pd.read_json(f)
	with open('long_motif/MITSU.json') as f:
		mitsu = pd.read_json(f)
	with open('long_motif/GEMFA.json') as f:
		gemfa = pd.read_json(f)
	with open('long_motif/qpms9.json') as f:
		qpms9 = pd.read_json(f)
	with open('long_motif/GLAM2.json') as f:
		glam2 = pd.read_json(f)
	memeScore = scoreMotif(template, meme, 0.25, 0.25, 0.25, 0.25)
	gameScore = scoreMotif(template, game, 0.25, 0.25, 0.25, 0.25)
	mitsuScore = scoreMotif(template, mitsu, 0.25, 0.25, 0.25, 0.25)
	gemfaScore = scoreMotif(template, gemfa, 0.25, 0.25, 0.25, 0.25)
	qpms9Score = scoreMotif(template, qpms9, 0.25, 0.25, 0.25, 0.25)
	glam2Score = scoreMotif(template, glam2, 0.25, 0.25, 0.25, 0.25)
	print(memeScore)
	print(gameScore)
	print(mitsuScore)
	print(gemfaScore)
	print(qpms9Score)
	print(glam2Score)

def main():
	scoreAll()


if __name__ == "__main__":
	main()