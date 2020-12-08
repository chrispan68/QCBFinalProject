#! /bin/bash
# Author: Alfredo Velasco

#meme ../../Data/example.fa -w 10 -seed 10 -dna -nmotifs 1 -p 16 -oc Experiment1

meme /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/control/data.fa  -w 10 -oc control -dna -nmotifs 1 -seed 10 -p 16
meme /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/long_background/data.fa  -w 10 -oc long_background -dna -nmotifs 1 -seed 10 -p 16
meme /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/long_motif/data.fa  -w 30 -oc long_motif -dna -nmotifs 1 -seed 10 -p 16
meme /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/plasmodium_falciparum/data.fa  -w 10 -oc plasmodium_falciparum -dna -nmotifs 1 -seed 10 -p 16
meme /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/random_motif/data.fa  -w 10 -oc random_motif -dna -nmotifs 1 -seed 10 -p 16
meme /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/short_motif/data.fa  -w 6 -oc short_motif -dna -nmotifs 1 -seed 10 -p 16
meme /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/tandem_repeat/data.fa  -w 10 -oc tandem_repeat -dna -nmotifs 1 -seed 10 -p 16
