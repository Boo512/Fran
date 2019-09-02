# Fran

Yeah so huh... I needed a simple tool for frequency analysis in a cryptography CTF so i made it as a command line python tool

usage: fran.py [-h] [-j JUMP] [-k KEEP] [-s START] [-e END] [--short] filename {1,2,3}

positional arguments:
  filename                  name of the file to analize
  {1,2,3}                   count groups of n characters

optional arguments:
  -h, --help                show this help message and exit
  
  -j JUMP, --jump JUMP      count every j character
  
  -k KEEP, --keep KEEP      print only the first k results
  
  -s START, --start START   start at a defined place
  
  -e END, --end END         stop at a defined place

  

