# Repo for QCB Final

## Data

To generate data, we need a motif file (frequency matrix) and also a HMM model used for background data generation. 

For example, run the following command to generate data with a motif 'ATATAT' placed into a uniform distribution:

<<<<<<< HEAD
python gen_motif_data.py --motif_file uniform/motif.json --background_file uniform/uniform_background.json --num_examples 20 --length 5 --output uniform/data.txt
=======
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
>>>>>>> 11019d22c86d9c5cfd1eb48da6f81eca16828bd7
