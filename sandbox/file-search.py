import os

for root, dirs, files in os.walk("/Users/manhart/Desktop/z_Run-off"):
    for filename in files:
        print(filename)
