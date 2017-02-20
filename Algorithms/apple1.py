"""
Given a folder of build files that might look like this:
/Build-1.dmg
/Build-2.dmg
/Build-2.1.dmg
/Build-2.1.1.dmg
/Build-3.dmg
/Build-3.2.dmg
/Build-3.19.dmg
...
Write a script in the language of your choosing that takes a path to the folder as an argument, and prints the highest build number (just the number, i.e. 2.1.1)
Note:  The first digit can go up to 999 and should always be present, but the second and third can only go up to 99, and might not be included.
"""
import os

def main(argv):
    highest_build(argv)

def highest_build(path):
    # peak into dir
    # put files within a list

    for file in list:
        largest = file.firstsub
        if file.firstsub >= largest:
            largest = file.firstsub

    # print the largest first sub which would be 3 in this case
    print file.firstsub

    pass

if '__name__' == '__main__':
    main(argv)
3.3
3.1
3.2

return 3.2 but i want 3.3