# Repo for QCB Final

## Data

To generate data, we need a motif file (frequency matrix) and also a HMM model used for background data generation. 

For example, run the following command to generate data with a motif 'ATATAT' placed into a uniform distribution:

python data/gen_motif_data.py --motif_file data/uniform/motif.json --background_file data/uniform/uniform_background.json --num_examples 20 --length 5 --output data/uniform/data.txt
