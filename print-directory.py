# import os

# os.walk() returns a list of three items. It contains the name of the root directory, a list of the names of the subdirectories, and a list of the filenames in the current directory.

# for root, dirs, files in os.walk("./Desktop"):
#     for filename in files:
#         print(filename)

# import subprocess
#
# # define the ls command
# ls = subprocess.Popen(["ls", "-p", "."],
#                       stdout=subprocess.PIPE,
#                      )
#
# # define the grep command
# grep = subprocess.Popen(["grep", "-v", "/$"],
#                         stdin=ls.stdout,
#                         stdout=subprocess.PIPE,
#                        )
#
# # read from the end of the pipe (stdout)
# endOfPipe = grep.stdout
#
# # output the files line by line
# for line in endOfPipe:
#     print (line)




# import os
# import fnmatch
#
# listOfFiles = os.listdir('.')
# pattern = "*.py"
#
# for entry in listOfFiles:
#     if fnmatch.fnmatch(entry, pattern):
#         print (entry)

# import os
#
# def files(path):
#     for file in os.listdir(path):
#         if os.path.isfile(os.path.join(path, file)):
#             yield file
#
# for file in files("."):
#     print(file)


# import pathlib
#
# # define the path
# currentDirectory = pathlib.Path('../../../Desktop/z_Run-off')
#
# for currentFile in currentDirectory.iterdir():
#     print(currentFile)


# # Use Glob to target specific filetypes
# import pathlib
#
# currentDirectory = pathlib.Path('.')
#
# currentPattern = "*.md"
#
# for currentFile in currentDirectory.glob(currentPattern):
#     print(currentFile)






import os

path = os.getcwd()

with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        if entry.is_file():
            print(entry.name)
