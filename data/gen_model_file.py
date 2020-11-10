import sys
import json
import argparse


def gen_tail(average_tail, front_name, back_name, tail_name):
    """ Generates a tail that starts at state front_name and generates random base pairs geometrically,
    then ends at back_name. 

    Keyword arguments:
    average_tail -- the average length of the tail. 
    front_name -- the first state of the tail. 
    back_name -- the last state of the tail. 
    tail_name -- the unique name of the tail to make sure we don't reuse states. 
    """
    
    output = {}
    base_pairs = ["A", "T", "G", "C"]
    tail_emission_names = [(tail_name + "_" + x) for x in base_pairs] # holds the name of the four emission states of a tail
    p = 1 / (average_tail + 1) # sets the geometric probability p based on the average tail length. 
    
    # sets the front state for the tail
    front_state_transitions = []
    for emission_state in tail_emission_names:
        transition = {
            "state": emission_state,
            "prob": (1 - p) / 4
        }
        front_state_transitions.append(transition)
    front_state_transitions.append(
        {
            "state": back_name, 
            "prob": p
        }
    )
    tail_front_state = {
        "emission": "None", 
        "transitions": front_state_transitions
    }
    output[front_name] = tail_front_state

    # sets each of the emission states for the tail:
    for emission_state, emission in zip(tail_emission_names, base_pairs):
        output[emission_state] = {
            "emission": emission, 
            "transitions": [
                {
                    "state": front_name,
                    "prob": 1
                }
            ]
        }
    
    return output


    
    

def generate_model_one_motif(motif, average_tail):
    """ Generates a markov model that creates datapoints that include two tails generated
    with a geometrically distributed length, centered on a motif, specified by a frequency matrix. 

    Keyword arguments:
    motif -- the frequency matrix of the motif
    average_tail -- average length of geometrically distributed tail
    seed -- optional argument to specify a random seed to be used
    """

    output = {}
    n = len(motif)
    base_pairs = ["A", "T", "G", "C"]

    for i in range(n):
        motif_state_name = "MOTIF_" + str(i)
        next_motif_state_name = "MOTIF_" + str(i+1)

        motif_state_transitions = []
        for bp in base_pairs:
            emission_state_name = motif_state_name + "_" + bp
            # initialize the intermediate motif emission states
            output[emission_state_name] = {
                "emission": bp,
                "transitions": [
                    {
                        "state": next_motif_state_name,
                        "prob": 1
                    }
                ]
            }

            # add a transition probability into the current motif state
            motif_state_transitions.append(
                {
                    "state": emission_state_name, 
                    "prob": motif[i][bp]
                }
            )

        
        output[motif_state_name]= {
            "emission": "None",
            "transitions": motif_state_transitions
        }
        
    # initialize tails
    start_tail = gen_tail(average_tail, "<START>", "MOTIF_0", "START_TAIL")
    end_tail = gen_tail(average_tail, "MOTIF_" + str(n), "<END>", "END_TAIL")
    output.update(start_tail)
    output.update(end_tail)

    output["<END>"] = {
        "emission": "None", 
        "transitions": [
            {
                "state": "<END>",
                "prob": 1.0
            }
        ]
    }

    return output



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--motif_file", type=str, help="Location of the motif file used to generate moddel. Should be a json file.")
    parser.add_argument("--average_tail_length", type=int, help="The average length of the tails", default=0)
    parser.add_argument("--output", type=str, help="Location of the output file in a .json format.", default="model.json")
    args = parser.parse_args()

    with open(args.motif_file) as f:
        motif = json.load(f)

    model = generate_model_one_motif(motif=motif, average_tail=args.average_tail_length)
    
    with open(args.output, 'w') as f_out:
        json.dump(model, f_out, indent=4)
    
    print("Generation successful!")

if __name__ == "__main__":
    main()