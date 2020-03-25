from src.gedcom import *
from src.sprint1.story4 import s4test
from src.sprint1.story1_peer import s1test
from src.sprint1.story3 import s3test
from src.sprint2.story7 import s7test
from src.sprint2.story8 import s8test
from src.sprint2.story5 import s5test
from src.sprint2.story2 import s2test

def main():
    File = open('Khalid_GEDCOM.txt')
    New_file = open("Gedcome-output.txt","w")
    data,New_file = createoutput(File,New_file)
    New_file = s7test(data,New_file)
    New_file = s8test(data,New_file)
    New_file = s4test(data,New_file)
    New_file = s1test(data,New_file)
    New_file = s2test(data,New_file)
    New_file = s5test(data,New_file)
    New_file.close()
    File.close()

if __name__ == "__main__":
    main()
