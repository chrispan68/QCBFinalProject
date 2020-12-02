import sys
import json
import argparse
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ground_truth", type=str, help="Location of the ground truth json file.")
    parser.add_argument("--model_output", type=str, help="Location of the model output json file.")
    args = parser.parse_args()

    with open(args.ground_truth) as f:
        ground_truth = json.load(f)
    
    with open(args.model_output) as f:
        model_output = json.load(f)
    
    
    
    print("Generation successful!")

if __name__ == "__main__":
    main()