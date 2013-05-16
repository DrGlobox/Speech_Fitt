#!/bin/bash
#
#SPEECH2TXT version 1.0
#by Christophe Varlet       #Please visit http://leprojetscribe.com
#
#Un script de reconnaissance vocale depuis la ligne de commande 
#Ce script utilise l'api google speech-input




#requiert : flac        #You need to install flac to run this script


arecord -q -f cd -t wav -d 3 -r 16000 | flac --totally-silent - -f --best --sample-rate 16000 -o out.flac;

wget -q -O speech.txt --post-file out.flac --header="Content-Type: audio/x-flac; rate=16000" http://www.google.com/speech-api/v1/recognize?lang=fr;

cat speech.txt | cut -d'"' -f12 >> records.txt;
cat speech.txt | cut -d'"' -f12;
rm out.flac speech.txt;

exit 0


