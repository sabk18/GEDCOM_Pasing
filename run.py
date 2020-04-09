from src.gedcom import *
from src.sprint1.story4 import s4test
from src.sprint1.story1_peer import s1test
from src.sprint1.story3 import s3test
from src.sprint2.story7 import s7test
from src.sprint2.story8 import s8test
from src.sprint2.story5 import s5test
from src.sprint2.story2 import s2test
from src.sprint2.story09 import s09_test
from src.sprint3.story30 import s30_test
from src.sprint3.story31 import s31_test
from src.sprint2.story21 import s21_test
from src.sprint2.story25 import s25test
from src.sprint3.story35 import s35_run
from src.sprint3.story28 import s28_run
from src.sprint3.story32 import s32_run
from src.sprint3.story37 import s37_run
from src.sprint3.story41 import s41test
from src.sprint3.story42 import s42test
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
    New_file = s09_test(data,New_file)
    New_file = s30_test(data,New_file)
    New_file = s31_test(data,New_file)
    New_file = s21_test(data,New_file)
    New_file = s25test(data, New_file)
    New_file = s35_run(data,New_file)
    New_file = s28_run(data, New_file)
    New_file = s32_run(data, New_file)
    New_file = s37_run(data, New_file)

    New_file = s41test(data, New_file)
    New_file = s42test(data, New_file)

    New_file.close()
    File.close()

if __name__ == "__main__":
    main()
