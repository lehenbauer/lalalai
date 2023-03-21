

ksplitter.py takes lalaai_splitter.py to the next level.

1. Multiple stems can be extracted from one run of the program.  You can specify the stems you want from the command line.

1. It only uploads the file once regardless of the number of stems that are extracted.  (their python program, their website, and their app require the file be uploaded every time for each stem extracted)

3. It only downloads the backing track (like for vocals, everything but vocals) for vocals by default, but you can specify other backing tracks from the command line

python3 ksplitter.py --license xxxxxxxxxxxxxxxx --input /Users/karl/Music/Logic/virtual/con funk shun/da lady/Bounces/da lady.mp3 --output output --stems vocals drum bass electric_guitar synthesizer voice strings wind --backingstems vocals drum

In the above command we extract from the specified input file to the specified output directory, the list of stems specificied and the optional list of backing tracks.

python TK

brew install python-tk@3.11


