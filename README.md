# featureDataCleaning
Cleaning the data from Feature Extraction Project
the program will combine five refactoring featrues data files.
1. Reduce duplicate AST, and put refactoring type label for each AST. Write into All_Factoring.csv
2. Create five different csv files for each refactoring type with header: AST, IsType

use the below command to run the program: 
python fileparser.py EXTRACT_AND_MOVE_METHOD EXTRACT_METHOD EXTRACT_VARIABLE INLINE_VARIABLE MOVE_METHOD
