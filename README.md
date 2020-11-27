# Repo for QCB Final

## Data

To generate data, we need a motif file (frequency matrix) and also a HMM model used for background data generation. 

For example, run the following command to generate data with a motif 'ATATAT' placed into a uniform distribution:

python data/gen_motif_data.py --motif_file data/uniform/motif_deterministic_ATGTACACGGAT.json --background_file data/uniform/uniform_background.json --num_examples 100 --length 30 --output data/uniform/data.txt