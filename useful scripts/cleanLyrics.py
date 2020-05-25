import string

# convert text in lyrics to lower case and removes all punctuations
# e.g !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
with open("lyricsData.txt","x",encoding="UTF-8") as new:
    with open("lyrics.txt","r") as lines:
        for line in lines:
            line = line.lower() # convert words to lower case
            words = line.split() 
            strip = str.maketrans("","",string.punctuation) 
            stripped = [w.translate(strip) for w in words] # remove all punctuations
            # save lower case stripped words to new file
            new.writelines(" ".join(stripped))
            new.writelines("\n")       

