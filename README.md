# Repo for QCB Final

## Data

Generates a data file from a markov model specified by a json file. 

In the model.json file you must specify the states, as well as the transitions for each states and a possible emission at each state. 

In the data/uniform_control_data directory there is an example model.json file along with a diagram that generates from a uniform distribution. 

How to run the generation code: 

### Given a HMM model

python data/gen_data.py --gen_model data/uniform_control_data/model.json --num_examples 10 --output data/uniform_control_data/data.txt


Use the following command to see all the arguments:

python data/gen_data.py --help

### Given a motif

Run two commands: 

python data/gen_model_file.py --motif_file data/example_motif/motif.json --average_tail_length 4 --output data/example_motif/model.json

python data/gen_data.py --gen_model data/example_motif/model.json --num_examples 10000 --output data/example_motif/data.txt

First command generates a model.json file from the motif.json file. Second command actually generates the data. Same as before. 

Again use --help to see the arguments. 
