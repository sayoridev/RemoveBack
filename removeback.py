#!/bin/python3

import sys
from rembg import remove
from PIL import Image

def removeback(pinput, poutput):
    with Image.open(pinput) as img:
        img_without_back = remove(img)
        img_without_back.save(poutput)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: removeback <imagine input> <imagine output>")
        sys.exit(1)
    
    pinput = sys.argv[1]
    poutput = sys.argv[2]

    removeback(pinput, poutput)
