from src.gedcom import *
from src.sprint1.story4 import test

def main():
    File = open('Khalid_GEDCOM.txt')
    New_file = open("Gedcome-output.txt","w")
    data,New_file = createoutput(File,New_file)
    New_file = test(data,New_file)
    New_file.close()
    File.close()

if __name__ == "__main__":
    main()