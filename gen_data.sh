#!/bin/sh

python gen_background.py --dir control
python gen_motif_data.py --dir control
python gen_background.py --dir control2
python gen_motif_data.py --dir control2 
python gen_background.py --dir control3
python gen_motif_data.py --dir control3

python gen_background.py --dir long_background 
python gen_motif_data.py --dir long_background 
python gen_background.py --dir long_background2
python gen_motif_data.py --dir long_background2
python gen_background.py --dir long_background3
python gen_motif_data.py --dir long_background3

python gen_background.py --dir long_motif
python gen_motif_data.py --dir long_motif
python gen_background.py --dir long_motif2
python gen_motif_data.py --dir long_motif2
python gen_background.py --dir long_motif3
python gen_motif_data.py --dir long_motif3

python gen_background.py --dir plasmodium_falciparum
python gen_motif_data.py --dir plasmodium_falciparum
python gen_background.py --dir plasmodium_falciparum2
python gen_motif_data.py --dir plasmodium_falciparum2
python gen_background.py --dir plasmodium_falciparum3
python gen_motif_data.py --dir plasmodium_falciparum3

python gen_background.py --dir random_motif
python gen_motif_data.py --dir random_motif
python gen_background.py --dir random_motif2
python gen_motif_data.py --dir random_motif2
python gen_background.py --dir random_motif3
python gen_motif_data.py --dir random_motif3

python gen_background.py --dir short_motif
python gen_motif_data.py --dir short_motif
python gen_background.py --dir short_motif2
python gen_motif_data.py --dir short_motif2
python gen_background.py --dir short_motif3
python gen_motif_data.py --dir short_motif3

python gen_background.py --dir tandem_repeat
python gen_motif_data.py --dir tandem_repeat
python gen_background.py --dir tandem_repeat2
python gen_motif_data.py --dir tandem_repeat2
python gen_background.py --dir tandem_repeat3
python gen_motif_data.py --dir tandem_repeat3