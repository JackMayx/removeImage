from PIL import  Image

imageDirectory = "/Users/godox/Resources/pythonfIle/icon/image"
imageSize = [40,58,60,80,87,120,180,1024]


def createImage(size):
    im = Image.open(imageDirectory+"/icon_1024.png")
    im.resize((size,size), Image.ANTIALIAS).save(imageDirectory+"icon%dx%d.png"%(size,size))

def start():
    for size in imageSize:
       createImage(size)

if __name__ == "__main__":
    start()
