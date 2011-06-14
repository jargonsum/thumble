#!/usr/bin/env python
""" [thumble.py 0.2]:
 Search through a given directory and create
 100px wide resized copies of all images found,
 then format into a thumbnail gallery (HTML/CSS), 
 with each thumbnail linked to its full-sized original.
 
 Copyright 2010, 2011 Dayo Adewunmi 100224
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

 TODO: - Pagination.
       - A panel at the top, with previous <--current-->next thumb."""

import os
import PIL
from PIL import Image
import re

# Create thumbnails from images
def createThumbs():
    """ """
    # Get current directory path
    absolutePath = os.getcwd()
    
    # Get the name of the current directory
    currentdir = os.path.basename(absolutePath)

    linebreak = 1

    newrow = '</div></div><div class="newrow">'
    samerow = '</div>'

    # Go through the filenames in the current directory...
    for dirname, subdirname, filenames in os.walk(absolutePath):
        for filename in filenames:
            # Find all images
            if isImageFile(filename):
                # ...and create thumbnails
                # Resize an image (somepic.jpg) using PIL (Python Imaging Library) 
                # to a width of 300 pixels and a height proportional to the new width. 
                # It does this by determining what percentage 300 pixels is of the 
                # original width (img.size[0]) and then multiplying the original height 
                # (img.size[1]) by that percentage. Change "basewidth" to any other 
                # number to change the default width of your images.
                basewidth = 100
                img = Image.open(filename)
                widthPercent = (basewidth/float(img.size[0]))
                height = int((float(img.size[1])*float(widthPercent)))

                img = img.resize((basewidth, height), PIL.Image.ANTIALIAS)
                thumbname = 'thumb_' + filename
                img.save(thumbname)

                if linebreak % 5 == 0:
                    createGallery(filename,thumbname,newrow)
                else:
                    createGallery(filename,thumbname,samerow)

                linebreak = linebreak + 1

def createGallery(filename,thumbname,divtype):
    """ """
    thumb = '<div class="thumb"><a href="%s"><img src="%s" /></a>%s' %(filename,thumbname,divtype)

    writeFile.write(thumb)

# Match files that are image files
def isImageFile(filename):
    """ """
    image_re = re.compile('\.gif$|\.jpe?g$|\.png$|\.svg$|\.tiff?$', re.I)
    return image_re.search(filename)

def endIndexHTML():
    """ """
    endDivs = '</div>'
    endBodyTag = '</div></body></html>'

    bottom = endDivs + footer + endBodyTag

    writeFile.write(bottom)

# Create a file in write mode
indexFile = "index.html"
writeFile = open(indexFile, "w")
   
titleTag = '<html><head><title>Thumble - Image gallery</title>'
includeCSS = '<link href="thumbstyles.css" rel="stylesheet" type="text/css" /></head>'
header = titleTag + includeCSS  

startBodyTag = '<body>'
howto = '<strong><h4></h4> To view full-size: click on image. To save a picture: right-click on image and click "Save Link As"</strong>'
startDivs = '<div id="container"><div class="newrow">'

footer = '<div id="footer">Thumbnail gallery generated with <a href="" target="_blank">Thumble</a></div>'

top = header + startBodyTag + howto + startDivs 

writeFile.write(top)

createThumbs()
endIndexHTML()

print ""
