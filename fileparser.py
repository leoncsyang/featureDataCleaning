import csv
import sys
import  os


#Fuction: mergeRefactorFiles(targetName)
#Traverse all folder and find the same file fName, append merge together
#and return a new file Call fName
#input: file name
#return file name after merge
def mergeRefactorFiles(targetName):
    filesname = []
    dir_path = os.path.dirname(os.path.realpath(__file__)) 
    #print(dir_path)
    for root, dirs, files in os.walk(dir_path): 
        for file in files:
            # the one of your choice. 
            if file.startswith(targetName): 
                #print root+'/'+str(file) 
                filename = root +'/' + str(file)
                print("found: ", filename)
                filesname.append(filename)

    srcName = "ALL_" + targetName

    with open(srcName, 'w') as outfile:
        for fname in filesname:
            with open(fname) as infile:
                outfile.write(infile.read())
    outfile.close()
    return srcName


#Function: readFile(fName,label)
#Read data file and return as dictionary with label
#input: file nane, label
#return: dictionary
def readFile(fName,label):
    print("parsing: ", fName, "with label: ", label)
    f = open(fName,"r")
    lines = [line.rstrip('\n') for line in f]
    f.close()
    fDict = {}
    for line in lines:
        fDict[line] = label
    return fDict


#Function: mergeDict(dict1, dict2,dict3,dict4,dict5)
#Merge five dictionaries into one dictionary And put the label
#input: five dictionaries
#return: one groupped dictionary
def mergeDict(dict1, dict2,dict3,dict4,dict5):
   ''' Merge dictionaries and keep values of common keys in list'''
   dictA = {**dict1, **dict2}
   for key, value in dictA.items():
       if key in dict1 and key in dict2:
               dictA[key] =  dict1[key] + value
   dictB = {**dictA, **dict3}
   for key, value in dictB.items():
       if key in dictA and key in dict3:
           dictB[key] = dictA[key] + value
   dictC = {**dictB, **dict4}
   for key, value in dictC.items():
       if key in dictB and key in dict4:
           dictC[key] = dictB[key] + value
   dictD = {**dictC, **dict5}
   for key, value in dictD.items():
       if key in dictC and key in dict5:
           dictD[key] =  dictC[key] + value

   return dictD


#Function: splitDict(gDict, label, fName)
#Split the groupped dictionary by desired label, return to a new file
#input: group dictionary, label, output file name
#return: new dictionary
def splitDict(gDict, label, fName):
    subDict = {}
    for key, value in gDict.items():
        if label in value:
            subDict[key] = 1
        else:
            subDict[key] = 0
    outputName = "OUT_" + fName
    with open(outputName, 'w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f) 
        writer.writerow(["AST", "IsType"])
        for key, value in subDict.items():
            writer.writerow([key, value])
    f.close()
    return subDict


if __name__ == '__main__':
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    file3 = sys.argv[3]
    file4 = sys.argv[4]
    file5 = sys.argv[5]

    filename1 = mergeRefactorFiles(file1)
    filename2 = mergeRefactorFiles(file2)
    filename3 = mergeRefactorFiles(file3)
    filename4 = mergeRefactorFiles(file4)
    filename5 = mergeRefactorFiles(file5)

    exMetAndMo = readFile(filename1, "A")
    exMet = readFile(filename2, "B")
    exVar = readFile(filename3, "C")
    inVar = readFile(filename4, "D")
    moMet = readFile(filename5, "E") 

    # exMetAndMo = readFile("EXTRACT_AND_MOVE_METHOD", "A")
    # exMet = readFile("EXTRACT_METHOD", "B")
    # exVar = readFile("EXTRACT_VARIABLE", "C")
    # inVar = readFile("INLINE_VARIABLE", "D")
    # moMet = readFile("MOVE_METHOD", "E") 

    groupDict = mergeDict(exMetAndMo,exMet,exVar,inVar,moMet)
    #print(groupDict.items())
    new_exMetAndMo = splitDict(groupDict,"A","EXTRACT_AND_MOVE_METHOD.csv")
    new_exMet = splitDict(groupDict,"B","EXTRACT_METHOD.csv")
    new_exVar = splitDict(groupDict,"C","EXTRACT_VARIABLE.csv")
    new_inVar = splitDict(groupDict,"D","INLINE_VARIABLE.csv")
    new_moMet = splitDict(groupDict,"E","MOVE_METHOD.csv")

    #put groupDict into a file
    with open("All_Refactor.csv", 'w',encoding='utf-8',newline='') as f:
        writer = csv.writer(f) 
        writer.writerow(["AST", "IsType"])
        for key, value in groupDict.items():
            writer.writerow([key, value])
    f.close()



