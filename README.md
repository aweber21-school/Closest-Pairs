# Closest-Pairs
This repository contains the Closest Pairs algorithm for EN.605.621 Programming Assignment 1

## Implementation
The Closest Pairs algorithm is implemented in Python. This algorithm can be ran
the same way as any other Python script, along with flags to control
functionality. An example command line command is shown below:

```
python Closest-Pairs.py -t -P 500 -m 50 -i inputFile.txt -o outputFile.txt
```

## Files
This repository contains this README, the source code for the Closest Pairs
algorithm, traces, and test cases. The file structure is shown below:

Closest-Pairs
|---> README.md
|---> Closest-Pairs.py
|---> traces/
|     |---> trace-P#-m#/
|     |     |---> input-P#-m#.txt
|     |     |---> output-P#-m#.txt
|     |     |---> results-P#-m#.txt
|     |     |---> traceOutput-P#-m#/
|     |           |---> Closest-Pairs.cover
|     |           |---> random.cover
|     |---> ...
|---> testCases/
      |---> constant-P/
      |     |---> testCase-P#-m#/
      |     |     |---> input-P#-m#.txt
      |     |     |---> output-P#-m#.txt
      |     |     |---> results-P#-m#.txt
      |     |     |---> traceOutput-P#-m#/
      |     |           |---> Closest-Pairs.cover
      |     |           |---> random.cover
      |     |---> ...
      |---> constant-m/
            |---> testCase-P#-m#/
            |     |---> input-P#-m#.txt
            |     |---> output-P#-m#.txt
            |     |---> results-P#-m#.txt
            |     |---> traceOutput-P#-m#/
            |           |---> Closest-Pairs.cover
            |           |---> random.cover
            |---> ...
