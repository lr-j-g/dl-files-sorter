import os, shutil

class fileSort:
    def __init__(self):
        self.filePath = None             #this variable contains the file path where we want to sort.
        self.files = []                  #this is a list variable containing all files in the path.

    def enterPath(self):
        
        while True:
            filePath = input("Enter file path: ")
            if not os.path.exists(filePath):
                print("This file path do not exist.")
            else:
                break
            
        self.filePath = f"{filePath}"

        for file in os.listdir(self.filePath):
            self.files.append(file)


    def sortFiles(self):
        for file in self.files:
            fileName, fileExtension = os.path.splitext(self.filePath + "/" + file)      #extract file extension of each file
            
            if fileExtension == '':                                                     #skip folders they do not need sorting.
                pass

            if not os.path.exists(self.filePath + "/" + fileExtension):                 #create folder for a specific filetype
                os.makedirs(self.filePath + "/" + fileExtension)

            if not os.path.exists(self.filePath + "/" + fileExtension + "/" + file):    #move files to folders according to their file extension.
                shutil.move(self.filePath + "/" + file, self.filePath + "/" + fileExtension + "/" + file)

        