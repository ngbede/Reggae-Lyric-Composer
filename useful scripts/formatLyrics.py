import os
import glob

# extract lyrics folder from lyrics.rar and place in current directory
file_dir = os.getcwd() + "\\lyrics" # lyrics folder directory

os.chdir(file_dir)
title = []
for song in os.listdir(): # append all song titles in a list
    title.append(song)

for song in title: # clean up song lyrics
    with open(song,"r") as f:
        file = f.readlines()[2:] # removing first two lines of lyrics
    
    with open(song, "w") as f:
        for line in file:
            if line != "\n":
                f.write(line)
        f.write("\n")

read_files = glob.glob("*.txt") # list of all txt files

with open("data.txt", "w") as outfile: # appends every song lyric into single txt file
    for f in read_files:
        with open(f, "r") as infile:
            outfile.write(infile.read())
            outfile.write("\n") # an empty line between each song
