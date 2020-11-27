import sys
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
    parser.add_argument("--motif_file", type=str, help="Location of the motif file used to generate moddel. Should be a json file.")
    parser.add_argument("--background_file", type=str, help="Location of the background distribution HMM model. Should be a json file.")
    parser.add_argument("--num_examples", type=int, help="The number of examples generated", default=0)
    parser.add_argument("--length", type=int, help="Length per generation")
    parser.add_argument("--output", type=str, help="Location of the output data.", default="data.txt")
    parser.add_argument("--random_seed", type=int, help="Optional random seed to specify for generation.", default=None)
    args = parser.parse_args()

    if args.random_seed is not None:
        random.seed(args.random_seed)

    with open(args.motif_file) as f:
        motif = json.load(f)
    
    with open(args.background_file) as f:
        model = json.load(f)
    
    error = validate_model(model=model)
    if not error is None:
        print("Error.")
        print("Model format incorrect:")
        print(error)
        print("No data generated, please fix and retry.")
        return
    
    data = place_motif(backgrounds=generate_data(model=model, num_examples=args.num_examples, length=args.length), motif=motif, length=args.length)
    with open(args.output, 'w') as f_out:
        f_out.write("\n".join(data))
    
    print("Generation successful!")

if __name__ == "__main__":
    main()