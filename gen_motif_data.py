import sys
import os
import json
import argparse
import random
from gen_background import validate_model, generate_data

def place_motif(backgrounds, motif, length):
    """ Uses a list of backgrounds generated and places the stochastically generated 
    motif randomly and uniformly in one position of the background. 

    Keyword arguments: 
    backgrounds -- list of background distribution instances. 
    motif -- list representing the frequency table of the motif.
    length -- length of the background
    """

    output = []
    for background in backgrounds:
        motif_instance = ""
        for nucleotide in motif: 
            choices = ['A', 'T', 'G', 'C']
            weights = [nucleotide['A'], nucleotide['T'], nucleotide['G'], nucleotide['C']]
            motif_instance += random.choices(choices, weights=weights)[0]
        ind = random.randint(0, length)
        background = background[:ind] + motif_instance + background[ind:]
        output.append(background)
    return output




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, help="Directory for input / output files for motif generation.", default=None)
    parser.add_argument("--num_examples", type=int, help="The number of examples generated", default=200)
    parser.add_argument("--length", type=int, help="Length per generation", default=40)
    args = parser.parse_args()

    with open(os.path.join(args.dir, "motif.json")) as f:
        motif = json.load(f)
    
    with open(os.path.join(args.dir, "background.json")) as f:
        model = json.load(f)
    
    error = validate_model(model=model)
    if not error is None:
        print("Error.")
        print("Model format incorrect:")
        print(error)
        print("No data generated, please fix and retry.")
        return
    
    data = place_motif(backgrounds=generate_data(model=model, num_examples=args.num_examples, length=args.length), motif=motif, length=args.length)
    with open(os.path.join(args.dir, "data.fa"), 'w') as f_out:
        for i, sample in enumerate(data):
            f_out.write(">seq" + str(i) + "\n")
            f_out.write(sample + "\n")
    
    print("Generation successful!")

if __name__ == "__main__":
    main()