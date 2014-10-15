import urllib.request
import re

class Downloader():
    '''
    Class to retreive HTML code and binary files from a specific website
    '''

    def __init__(self,url):
        self.url = url
        self.contents = ''

            

    def download(self):
        browser = urllib.request.urlopen(self.url)
        response = browser.getcode()
        if response == 200:
            self.contents = browser.read().decode("utf-8")



class redditParser(Downloader):
    '''
    Class for parsing usernames from xkcd.com
    '''


    def __init__(self,url):
        Downloader.__init__(self,url)
        self.users = []
    def get_last_username(self):
        try:
            #self.last_username = re.search(r'"http://www.reddit.com/user/(\w+)"', self.contents).group(1)
            self.users = re.findall(r'"http://www.reddit.com/user/(\w+)"', self.contents)
        except:
            self.users = "-5"
            
    def get_current_user(self):
        self.download()
        self.get_last_username()


            

if __name__ == '__main__':
    url = "http://www.reddit.com/"
    reddit_parser = redditParser(url)
    reddit_parser.get_current_user()
    print(reddit_parser.users)

