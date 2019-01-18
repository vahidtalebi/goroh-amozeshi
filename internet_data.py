import urllib

def main():
    #open connection to URL using urllib
    weburl = urllib.urlopen("http://joemarini.com")

    #get the result code and print it
    print "result code: " + str(weburl.getcode())

    # read the data from the url and print it
    data = weburl.read()
    print data

if __name__ == "__main__":
    main()
