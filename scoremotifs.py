from motifscoring import scoreMotif
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# To be finished tomorrow (basically just call all of the functions)
def scoreAll():
	df = pd.DataFrame()
	folders = ['control', 'long_background', 'long_motif', 'plasmodium_falciparum', 'random_motif', 'short_motif', 'tandem_repeat']
	for variable in folders:
		print(variable)
		with open(variable + '/motif.json') as f:
			template = pd.read_json(f)
		if(variable != 'tandem_repeat'):
			with open(variable + '/meme.json') as f:
				meme = pd.read_json(f)
				memeScore = scoreMotif(template, meme, 0.25, 0.25, 0.25, 0.25)
		else:
			memeScore = float("nan")
		with open(variable + '/GAME.json') as f:
			game = pd.read_json(f)
		if(variable != 'tandem_repeat'):
			with open(variable + '/MITSU.json') as f:
				mitsu = pd.read_json(f)
				mitsuScore = scoreMotif(template, mitsu, 0.25, 0.25, 0.25, 0.25)
		else:
			mitsuScore = float("nan")
		if(variable != 'tandem_repeat'):
			with open(variable + '/qpms9.json') as f:
				qpms9 = pd.read_json(f)
				qpms9Score = scoreMotif(template, qpms9, 0.25, 0.25, 0.25, 0.25)
		else:
			qpms9Score = float("nan")
		with open(variable + '/GEMFA.json') as f:
			gemfa = pd.read_json(f)
		with open(variable + '/GLAM2.json') as f:
			glam2 = pd.read_json(f)
		if(variable != 'tandem_repeat'):
			with open(variable + '/MotifSampler.json') as f:
				motifsampler = pd.read_json(f)
				motifsamplerScore = scoreMotif(template, motifsampler, 0.25, 0.25, 0.25, 0.25)
		else:
			motifsamplerScore = float("nan")
		gameScore = scoreMotif(template, game, 0.25, 0.25, 0.25, 0.25)
		gemfaScore = scoreMotif(template, gemfa, 0.25, 0.25, 0.25, 0.25)
		glam2Score = scoreMotif(template, glam2, 0.25, 0.25, 0.25, 0.25)

		df[variable] = [memeScore, gameScore, gemfaScore, glam2Score, motifsamplerScore, qpms9Score, mitsuScore]
		print(memeScore)
		print(gameScore)
		print(gemfaScore)
		print(glam2Score)
		print(motifsamplerScore)
		print(qpms9Score)
		print(mitsuScore)
	df.index = ['MEME', 'GAME', 'GEMFA', 'GLAM2', 'MotifSampler', 'qpms9', 'MITSU']
	print(df)
	sns.heatmap(df, annot=True)
	plt.show()

def main():
	scoreAll()


if __name__ == "__main__":
	main()