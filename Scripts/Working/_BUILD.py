import os
import sys

def replaceScript(CURRENT_POS, CURRENT_COMMAND):
    print("Replacing in script ",CURRENT_POS,CURRENT_COMMAND)
    CURRENT_SCRIPT = str(10 * CURRENT_POS + CURRENT_COMMAND)
    CURRENT_WRITE_FILE = open(DIR_NAME_CURRENT+DIR_NAME_SCRIPTS+"auto_"+str(CURRENT_SCRIPT)+".bee", "w")
    CURRENT_COMMAND_FILE = open("./auto_x"+str(CURRENT_COMMAND)+".bee", "r")
    
    for CURRENT_LINE in CURRENT_COMMAND_FILE.readlines():
        CURRENT_LINE_NOPOS = CURRENT_LINE.replace("{pos}", str(CURRENT_POS))
        if CURRENT_LINE_NOPOS[0] == "[":
            CURRENT_POS_FILE_NAME = DIR_NAME_CURRENT+"\\"+CURRENT_LINE_NOPOS[2:len(CURRENT_LINE_NOPOS)-2]
            if os.path.exists(CURRENT_POS_FILE_NAME):
                print("Reading file "+CURRENT_LINE_NOPOS[2:len(CURRENT_LINE_NOPOS)-2])
                CURRENT_POS_FILE = open(CURRENT_POS_FILE_NAME, "r")
                for CURRENT_FROMFILE_LINE in CURRENT_POS_FILE.readlines():
                    CURRENT_WRITE_FILE.write(CURRENT_FROMFILE_LINE)
                CURRENT_WRITE_FILE.write("\n")
            else:
                print("File does not exist: "+CURRENT_LINE_NOPOS[2:len(CURRENT_LINE_NOPOS)-2])
                continue
        else:
            CURRENT_WRITE_FILE.write(CURRENT_LINE_NOPOS)
    CURRENT_WRITE_FILE.close()
    CURRENT_COMMAND_FILE.close()

CONST_ARGLENGTH = 1

if len(sys.argv) < CONST_ARGLENGTH:
    print("Invalid or missing arguments:")
    print("    build.py {number of positions}")

CONST_POSITIONS = int(sys.argv[1])

DIR_NAME_CURRENT = os.path.dirname(os.path.abspath(__file__))
DIR_NAME_SCRIPTS = "\\Scripts\\"

DIR_CONTENTS_CURRENT = os.listdir(DIR_NAME_CURRENT)
DIR_CONTENTS_SCRIPTS = os.listdir(DIR_NAME_CURRENT+DIR_NAME_SCRIPTS)

print("Reading ",CONST_POSITIONS," positions.")

for CURRENT_POS in range(1, CONST_POSITIONS):
    for CURRENT_COMMAND in range(0, 9):
        replaceScript(CURRENT_POS, CURRENT_COMMAND)