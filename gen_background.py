import sys
import json
import argparse
import os
import numpy.random as random

def validate_model(model, eps = 1e-10):
    """ Validates that a given model is a valid markov model for generating DNA string data. 
    In particular, performs the following checks:
    1) There is a start state
    2) In every state, the emissions are None, A, T, G, C or R for trinucleotide repeat
    3) In every state the transition probabilities are positive numbers. 
    4) In every state the transition probabilities sum to 1. 

    Returns an error message as to which check is failed. If return is None, then all checks are passed. 

    Keyword arguments:
    model -- the model to be validated. 
    eps -- the mathematical precision used to verify equality. 
    """

    # First check: there is a start state
    if not "<START>" in model.keys():
        return "Model does not have a start state." 
    
    # Second check: in every state the emissions are None, A, T, G or C
    for state in model.keys():
        if model[state]["emission"] not in ["None", "A", "T", "G", "C", "R"]:
            return "Model emission for state " + state + " is " + model[state]["emission"] + " which is not one of None, A, T, G, C. or R (tandem repeat)"
    
    # Third check and fourth check: in every state the transition probabilities are positive numbers, also they sum to 1
    for state in model.keys():
        sum = 0
        for trans in model[state]["transitions"]:
            if trans['prob'] < 0:
                return "Model probability for state " + state + " transition " + trans['state'] + " is negative."
            sum += trans['prob']
        if abs(sum - 1) > eps:
            return "The model transition probabilites for state " + state + " do not sum to 1."
    
    # All checks passed!
    return None





def generate_data(model, num_examples, length):
    """ Generates data given a model and the number of examples to be generated. 
    Returns a list of size num_examples, where each element is an independent generation. 
    This method does not validate the model, so make sure validate_model is called before. 

    Keyword arguments:
    model -- the model used for generation
    num_examples -- the number of generations to create. 
    length -- how long the generated sequences will be. 
    seed -- optional argument to specify a random seed to be used. 
    """

    output = [] # list of outputs for the total dataset. 
    for _ in range(num_examples):
        example_output = "" # stores the output for the current example
        cur_state = "<START>"
        cur_length = 0
        while cur_length < length:
            # emits if the state has an associated emission
            if model[cur_state]["emission"] in ["A", "T", "G", "C"]:
                example_output += model[cur_state]["emission"]
                cur_length += 1
            elif model[cur_state]["emission"] == "R":
                rep = example_output[-3:]
                if(length - cur_length < 3):
                    rep = rep[:length - cur_length]
                example_output += rep
                cur_length += 3
            states = []
            probs = []
            # transitions to the next state stochastically
            for trans in model[cur_state]["transitions"]:
                states.append(trans["state"])
                probs.append(trans["prob"])
            # updates current state
            cur_state = random.choice(states, p=probs)
        output.append(example_output)
    return output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", type=str, help="Directory for input / output files for motif generation.")
    parser.add_argument("--num_examples", type=int, help="Number of reads to generate.", default=200)
    parser.add_argument("--length", type=int, help="Length per generation", default=40)
    args = parser.parse_args()
    

    with open(os.path.join(args.dir, "background.json")) as f:
        model = json.load(f)
    
    error = validate_model(model=model)
    if not error is None:
        print("Model format incorrect:")
        print(error)
        print("No data generated, please fix and retry.")
        return

    
    examples = generate_data(model=model, num_examples=args.num_examples, length=args.length)

    with open(os.path.join(args.dir, "background.fa"), 'w') as f_out:
        for i, sample in enumerate(examples):
            f_out.write(">seq" + str(i) + "\n")
            f_out.write(sample + "\n")
    
    print("Generation successful!")

if __name__ == "__main__":
    main()