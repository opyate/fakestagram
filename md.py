import random
import string
from shutil import copyfile
import os

mdentry = """---
thumbnail: {thumbs}{imgpath}
layout: home
title: "{rand}"
date: {dformatted}
img: {imgpath}
---

Uploaded by [Fakestagram](https://github.com/opyate/fakestagram).

<small>{dformatted}</small>

![Uploaded by Fakestagram]({imgpath})
"""

jekylldir = '/Users/juanuys/Documents/websites/opyate.github.io'
mddir = '/_doodles/'
thumbs = '/assets/doodles/thumbs/'

def blog(path, dfmt, dfmt_short):
    N = 8
    rand = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(N))

    newname = dfmt_short + '-fakestagram-' + rand
    mdname = jekylldir + mddir + newname

    copyfile(path, mdname + '.jpeg')
    copyfile(path, jekylldir + thumbs + newname + '.jpeg')

    with open(mdname + '.md', "w") as text_file:
        post = mdentry.format(thumbs=thumbs, imgpath=newname+'.jpeg', dformatted=dfmt, rand=rand)
        text_file.write(post)


if __name__ == '__main__':
    from convert import convert
    from photofilter import filter
    import datetime as dt

    dnow = dt.datetime.now()
    dformattedshort = dnow.strftime('%Y-%m-%d')
    dformatted = dnow.strftime('%Y-%m-%dT%H:%M:%SZ')

    imgs = ['./img/2018-03-16T161159.193068.jpeg', './img/2018-03-16T161259.114118.jpeg']
    for img in imgs:
        blog(filter(convert(img)), dformatted, dformattedshort)