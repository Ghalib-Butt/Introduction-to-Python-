from utility import clearTerminal

readFile = open("dummyfiles/dummyfile1.txt", "r")
fileContent = readFile.read()
print(fileContent)

writeFile = open("dummyfiles/dummyfile2.txt", "w")
writeFile.write("I'm creating a new file using \"file.write\" and \"w\" as an argument in open.\n")
writeFile.write("This method will see if a file with this name already exists. For the first time it will cearte a new file and afterwards it will overide the existing file.\n")
writeFile.write("If the existing file gets deleted it will create a new file again with this name and content.\n")
writeFile.close()

clearTerminal()