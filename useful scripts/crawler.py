import os
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
class Crawl:
    """Scrapes song lyrics from https://www.azlyrics.com
    After creating Crawl object, run link_loader method first before store_song_lyrics method"""

    def __init__(self, link, folder_name):
        '''link: Pass in the full link to site containing the artist song list.
        e.g "https://www.azlyrics.com/l/luckydube.html"
        folder_name: Pass in the name of the folder where song lyrics will be saved
        Note: pass in inputs as string arguements'''
        self.link = link
        self.folder_name = folder_name
        self.site = "https://www.azlyrics.com" # main site
        if self.folder_name in os.listdir(): # check if folder exist in dir
            pass
        else:
           os.mkdir(self.folder_name)
        self.storage_path = os.getcwd() + "\\" + self.folder_name # path to folder
        self.links_location = self.storage_path +  "\\__links.txt"

    def link_loader(self):
        '''Function stores links to each song lyric in a txt file called __links.txt'''
        open_link = urlopen(self.link)
        read_link = open_link.read()
        open_link.close()
        parsed_link = soup(read_link, "html.parser") # parse link into soup as html format
        container = parsed_link.find_all("div", {"class":"listalbum-item"}) # contains links
        with open(self.links_location, "w") as f:
            for link in container:
                f.write("%s\n" % (self.site + link.a["href"][2:])) # full link to each song lyric

    def store_song_lyrics(self):
        """Note: Before Running this method, run the link_loader method first!
        This method stores song lyrics af artist in a folder."""
        with open(self.links_location) as f:
            links = f.readlines()

        os.chdir(self.storage_path) # change working directory
        for link in links: # loop through links and store each lyric in a txt file
            open_link = urlopen(link)
            read_link = open_link.read()
            open_link.close()
            # pass link as html object via beautifulSoup
            parse_link = soup(read_link, "html.parser")
            lyric = parse_link.find_all("div", {"class":None})
            song_title = parse_link.find_all("b", {"class":None})
            title = song_title[1].text.strip()[1:-1] + ".txt" # title of song
            try: #Catch any file not found error
                with open(title, "w") as f: # store each new song lyric into txt file
                    f.write("%s\n\n"%song_title[1].text.strip().upper())
                    f.write("%s"%lyric[0].text.strip())
            except:
                print(f"{title} not downloaded!") # error occured
        print("Done!") # lyrics loaded succesfully!

# sample code usage
face = Crawl("https://www.azlyrics.com/l/luckydube.html", "2Face")
face.link_loader()
face.store_song_lyrics()