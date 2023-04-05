# Machine-Learning-Notebooks
Bunch of ML/DL notebooks. Code, exercises, testing, etc.

## Third Project: Morse Code Decoder

This project is a Morse code decoder that takes a string of binary-encoded Morse code and decodes it into human-readable text. 
The decoder processes the input bits and uses a clustering algorithm to determine the Morse code's structure.

The code first decodes the binary string into Morse code by identifying the lengths of ones and zeros, representing dots, dashes, and spaces. 
Then, it clusters the lengths to differentiate between dots, dashes, and spaces within characters and words. Finally, it translates the clustered Morse code into human-readable text.

+---------------------+           +---------------------+           +---------------------+           +---------------------+           +---------------------+
|  Binary-encoded     | --------> |  Decode Bits into   | --------> |  Cluster Lengths    | --------> |  Translate Morse    | --------> |  Human-readable     |
|  Morse Code Input   |           |  Morse Code         |           |  to Differentiate   |           |  Code to Text       |           |  Text Output        |
+---------------------+           +---------------------+           +---------------------+           +---------------------+           +---------------------+


