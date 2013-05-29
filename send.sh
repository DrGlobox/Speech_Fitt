#!/bin/bash
#requiert : flac        #You need to install flac to run this script


wget -q -O speech.txt --post-file sound_$1.flac --header="Content-Type: audio/x-flac; rate=16000" http://www.google.com/speech-api/v1/recognize?lang=fr;
cat speech.txt | cut -d'"' -f12 >> records.txt;
cat speech.txt | cut -d'"' -f12;
rm sound_$1.flac speech.txt;

exit 0


