# Repo for QCB Final

## Data

Generates a data file from a markov model specified by a json file. 

In the model.json file you must specify the states, as well as the transitions for each states and a possible emission at each state. 

In the data/uniform_control_data directory there is an example model.json file along with a diagram that generates from a uniform distribution. 

How to run the generation code: 

python data/gen_data.py --gen_model data/uniform_control_data/model.json --num_examples 10 --output data/uniform_control_data/data.txt


Use the following command to see all the arguments:

python data/gen_data.py --help
