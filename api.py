import requests
import os

def fillImageLinks(mediaID, pagenum):
    _list = list()
    _list.append("https://t.nhentai.net/galleries/"+str(mediaID)+"/cover.jpg") # Cover

    #Pages
    for i in range(pagenum): # Loop and populate
        print("Doing "+str(i))
        _list.append("https://i.nhentai.net/galleries/{0}/{1}.jpg".format(mediaID, i))

    # Debug
    print(str(_list))
    return _list



def downloadImageLinks(_list, _path):
    # Loop and download
    for i in range(len(_list)):
        link = _list[i]
        # req get
        image = requests.get(link).content
        # save
        with open(_path+os.sep+str(i)+".jpg") as dl:
            # Write to path
            dl.write(image)



