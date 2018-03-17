from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def convert(path):
    img = Image.open(path)
    width, height = img.size

    if width > height:
        new_width = height
        new_height = height
    else:
        new_width = width
        new_height = width

    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    img2 = img.crop((left, top, right, bottom))
    newpath = path.replace('.jpeg', '-sq.jpeg')
    img2.save(newpath)

    return newpath

    

if __name__ == '__main__':
    convert(path='./img/2018-03-16T161159.193068.jpeg')
    convert(path='./img/2018-03-16T161259.114118.jpeg')
    