from src.gedcom import *
<<<<<<< Updated upstream
from src.sprint1.story4 import test

=======
from src.sprint1.story4 import s4test
from src.sprint1.story1_peer import s1test
from src.sprint1.story10 import s10test
>>>>>>> Stashed changes
def main():
    File = open('Khalid_GEDCOM.txt')
    New_file = open("Gedcome-output.txt","w")
    data,New_file = createoutput(File,New_file)
<<<<<<< Updated upstream
    New_file = test(data,New_file)
=======
    New_file = s4test(data,New_file)
    New_file = s1test(data,New_file)
    New_file = s10test(data,New_file)
>>>>>>> Stashed changes
    New_file.close()
    File.close()

if __name__ == "__main__":
    main()