#!/bin/python3

import sys
import argparse
from rembg import remove
from PIL import Image
import os

def removeback(pinput, poutput):
    """Remove the background from the input image and save the result to the output path."""
    with Image.open(pinput) as img:
        img_without_back = remove(img)

        # Add a default extension if not provided
        root, ext = os.path.splitext(poutput)
        if not ext:
            ext = '.png'
            poutput = root + ext
        
        img_without_back.save(poutput)

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Remove background from an image.")
    
    # Add the input and output file arguments
    parser.add_argument('input', type=str, help='Path to the input image')
    parser.add_argument('output', type=str, help='Path to save the output image with background removed')

    # Parse the arguments
    args = parser.parse_args()

    # Call the remove background function with the provided arguments
    removeback(args.input, args.output)

if __name__ == "__main__":
    main()
