#!/bin/bash
#requiert : flac        #You need to install flac to run this script

#Enregistre 3 seconde en flac

arecord -q -f cd -t wav -d 3 -r 16000 | flac --totally-silent - -f --best --sample-rate 16000 -o sound_$1.flac;
exit 0


