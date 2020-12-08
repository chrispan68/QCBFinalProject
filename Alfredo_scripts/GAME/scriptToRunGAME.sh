#!/bin/bash
# Author: Alfredo Velasco
# java -jar motif.jar -i ../../Data/example.fa -minw 1 -expw 12 -maxw 20 -n 1 -o Experiment1.txt

java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/control/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 10 -expw 10 -maxw 10 -o control.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/control2/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 10 -expw 10 -maxw 10 -o control2.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/control3/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 10 -expw 10 -maxw 10 -o control3.txt

java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/long_background/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 10 -expw 10 -maxw 10 -o long_background.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/long_background2/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 10 -expw 10 -maxw 10 -o long_background2.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/long_background3/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 10 -expw 10 -maxw 10 -o long_background3.txt

java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/long_motif/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 30 -expw 30 -maxw 30 -o long_motif.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/long_motif2/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 30 -expw 30 -maxw 30 -o long_motif2.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/long_motif3/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 30 -expw 30 -maxw 30 -o long_motif3.txt

java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/plasmodium_falciparum/data.fa -a 0.41 -g 0.09 -c 0.09 -t 0.41 -minw 10 -expw 10 -maxw 10 -o plasmodium_falciparum.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/plasmodium_falciparum2/data.fa -a 0.41 -g 0.09 -c 0.09 -t 0.41 -minw 10 -expw 10 -maxw 10 -o plasmodium_falciparum2.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/plasmodium_falciparum3/data.fa -a 0.41 -g 0.09 -c 0.09 -t 0.41 -minw 10 -expw 10 -maxw 10 -o plasmodium_falciparum3.txt

java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/random_motif/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 10 -expw 10 -maxw 10 -o random_motif.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/random_motif2/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 10 -expw 10 -maxw 10 -o random_motif2.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/random_motif3/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 10 -expw 10 -maxw 10 -o random_motif3.txt

java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/short_motif/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 6 -expw 6 -maxw 6 -o short_motif.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/short_motif2/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 6 -expw 6 -maxw 6 -o short_motif2.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/short_motif3/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 6 -expw 6 -maxw 6 -o short_motif3.txt

java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/tandem_repeat/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 8 -expw 8 -maxw 10 -o tandem_repeat.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/tandem_repeat2/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 8 -expw 8 -maxw 10 -o tandem_repeat2.txt
java -jar motif.jar -i /home/nalfredo/School/CompBio/Project/Data/QCBFinalProject-master/tandem_repeat3/data.fa -a 0.25 -g 0.25 -c 0.25 -t 0.25 -minw 8 -expw 8 -maxw 10 -o tandem_repeat3.txt

