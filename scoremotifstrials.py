from motifscoring import scoreMotif
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# To be finished tomorrow (basically just call all of the functions)
def scoreAll():
	for trial in ['', '2', '3']:
		df = pd.DataFrame()
		folders = ['control', 'long_background', 'long_motif', 'plasmodium_falciparum', 'random_motif', 'short_motif', 'tandem_repeat']
		for variable in folders:
			print(variable)
			with open(variable + trial + '/motif.json') as f:
				template = pd.read_json(f)
			with open(variable + trial + '/meme.json') as f:
				meme = pd.read_json(f)
				memeScore = scoreMotif(template, meme, 0.25, 0.25, 0.25, 0.25)
			with open(variable + '/GAME.json') as f:
				game = pd.read_json(f)
			# if(variable != 'tandem_repeat'):
			# 	with open(variable + '/MITSU.json') as f:
			# 		mitsu = pd.read_json(f)
			# 		mitsuScore = scoreMotif(template, mitsu, 0.25, 0.25, 0.25, 0.25)
			# else:
			# 	mitsuScore = float("nan")
			with open(variable + trial + '/qpms9.json') as f:
				qpms9 = pd.read_json(f)
				qpms9Score = scoreMotif(template, qpms9, 0.25, 0.25, 0.25, 0.25)
			# with open(variable + trial + '/GEMFA.json') as f:
			# 	gemfa = pd.read_json(f)
			with open(variable + trial + '/GLAM2.json') as f:
				glam2 = pd.read_json(f)
			if(variable != 'tandem_repeat' or trial != ''):
				with open(variable + trial + '/MotifSampler.json') as f:
					motifsampler = pd.read_json(f)
					motifsamplerScore = scoreMotif(template, motifsampler, 0.25, 0.25, 0.25, 0.25)
			else:
				motifsamplerScore = float("nan")
			gameScore = scoreMotif(template, game, 0.25, 0.25, 0.25, 0.25)
			# gemfaScore = scoreMotif(template, gemfa, 0.25, 0.25, 0.25, 0.25)
			glam2Score = scoreMotif(template, glam2, 0.25, 0.25, 0.25, 0.25)

			df[variable] = [memeScore, gameScore, glam2Score, motifsamplerScore, qpms9Score]
			print(memeScore)
			print(gameScore)
			# print(gemfaScore)
			print(glam2Score)
			print(motifsamplerScore)
			print(qpms9Score)
			# print(mitsuScore)
		df.index = ['MEME', 'GAME', 'GLAM2', 'MotifSampler', 'qpms9']
		print(df)
		sns.heatmap(df, annot=True)
		plt.show()

def main():
	scoreAll()


if __name__ == "__main__":
	main()