# lalalai_splitter.py

lalalai_splitter.py is an example of interacting with the LALAL.AI API as described in [https://www.lalal.ai/api/help/](https://www.lalal.ai/api/help/)

By specifying a list of stems and optional backing tracks to be extracted, the program will upload the file once and then process the stems one at a time without reuploading.

## Usage

```bash
% python3 lalalai_splitter.py --input <input directory or a file> \
                      --license <user license> \
                      --output <output directory> \
                      --stem <list of stems> \
                            default: 'vocals'
                            choices: 
                                ['vocals', 'drum', 'bass',
                                 'piano', 'electric_guitar', 
                                'acoustic_guitar', 'synthesizer', 'voice',
                                'strings', 'wind']
                            Stem option:
                            vocals, drum, bass, voice, electric_guitar, acoustic_guitar, synthesizer, strings, wind.
                            Stems voice, strings, wind are not supported by Cassiopeia
                      --backingtracks <list of stem types> \
                            default: 'vocals'
                      --filter <post-processing filter> \
                            default: 1
                            choices:
                                [0, 1, 2]
                            0: mild, 1: normal, 2: aggressive
                      --splitter <splitter type>
                            default: 'phoenix'
                            choices: 
                                ['phoenix', 'cassiopeia']
                            The type of neural network used to split audio
```
