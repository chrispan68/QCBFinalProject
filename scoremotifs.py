# Written by Charlie Vrattos

from motifscoring import scoreMotif
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from reversecomplement import generateComplement

# To be finished tomorrow (basically just call all of the functions)
def scoreAll():
	df = pd.DataFrame()
	folders = ['control', 'long_background', 'long_motif', 'plasmodium_falciparum', 'random_motif', 'short_motif', 'tandem_repeat']
	for variable in folders:
		if(variable != 'plasmodium_falciparum'):
			weightA = 0.25
			weightT = 0.25
			weightG = 0.25
			weightC = 0.25
		else:
			weightA = 0.41
			weightT = 0.41
			weightG = 0.09
			weightC = 0.09
		print(variable)
		with open(variable + '/motif.json') as f:
			template = pd.read_json(f)
		with open(variable + '/meme.json') as f:
			meme = pd.read_json(f)
			memeScore = scoreMotif(template, meme, weightA, weightC, weightG, weightT)
		with open(variable + '/GAME.json') as f:
			game = pd.read_json(f)
		if(variable != 'tandem_repeat'):
			with open(variable + '/MITSU.json') as f:
				mitsu = pd.read_json(f)
				mitsuScore = scoreMotif(template, mitsu, weightA, weightC, weightG, weightT)
			with open(variable + '/MotifSampler2.json') as f:
				motifsampler2 = pd.read_json(f)
				motifsampler2Score = scoreMotif(template, motifsampler2, weightA, weightC, weightG, weightT)
		else:
			mitsuScore = float("nan")
			motifsampler2Score = float("nan")
		with open(variable + '/qpms9.json') as f:
			qpms9 = pd.read_json(f)
			qpms9Score = scoreMotif(template, qpms9, weightA, weightC, weightG, weightT)
		if(variable != 'tandem_repeat'):
			with open(variable + '/GEMFA.json') as f:
				gemfa = pd.read_json(f)
				gemfaScore = scoreMotif(template, gemfa, weightA, weightC, weightG, weightT)
		else:
			gemfaScore = float("nan")
		with open(variable + '/GLAM2.json') as f:
			glam2 = pd.read_json(f)
		# if(variable != 'tandem_repeat'):
		# 	with open(variable + '/MotifSampler.json') as f:
		# 		motifsampler = pd.read_json(f)
		# 		motifsamplerScore = scoreMotif(template, motifsampler, weightA, weightC, weightG, weightT)
		# else:
		# 	motifsamplerScore = float("nan")
		with open(variable + '/BruteSub.json') as f:
			brutesub = pd.read_json(f)
		gameScore = scoreMotif(template, game, weightA, weightC, weightG, weightT)
		reverseGame = generateComplement(game)
		reverseGameScore = scoreMotif(template, reverseGame, weightA, weightC, weightG, weightT)
		if(reverseGameScore < gameScore):
			gameScore = reverseGameScore
		# gemfaScore = scoreMotif(template, gemfa, weightA, weightC, weightG, weightT)
		glam2Score = scoreMotif(template, glam2, weightA, weightC, weightG, weightT)
		brutesubScore = scoreMotif(template, brutesub, weightA, weightC, weightG, weightT)

		df[variable] = [memeScore, gameScore, gemfaScore, glam2Score, qpms9Score, mitsuScore, brutesubScore, motifsampler2Score]
		print(memeScore)
		print(gameScore)
		print(gemfaScore)
		print(glam2Score)
		# print(motifsamplerScore)
		print(qpms9Score)
		print(mitsuScore)
		print(brutesubScore)
		print(motifsampler2Score)
	df.index = ['MEME', 'GAME', 'GEMFA', 'GLAM2', 'qpms9', 'MITSU', 'Brute Force Substring', 'MotifSampler']
	print(df)
	sns.heatmap(df, annot=True)
	plt.show()

def main():
	scoreAll()


if __name__ == "__main__":
	main()