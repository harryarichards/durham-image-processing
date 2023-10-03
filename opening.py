import cv2 #Import cv2 so we can read and write images.
import sys #Import the sys package so we can deal with input from the command line.
from erosion import erode # Import the erode function from the erosion file.
from dilation import dilate # Import the dilate function from the dilation file.
# This is the open function which erodes the image, then dilates the eroded image.

def open(img, out):
    """
    'opens' an image and returns the opened image.
    'opening' involves eroding the image followed by dilating the image.
    also writes the opened image to a file as well as returning the opened image.

    :param img: the image to be opened.
    :param out: the path we're writing the opened image to.
    :return: return the opened image.
    """
    # Set the eroded image equal to the result of the erode function performed on the image passed into the function.
    eroded_img = erode(img, out)
    # Set the opened image equal to the result of the dilate function performed on the eroded image.
    opened_img = dilate(eroded_img, out)
    # Write the opened image file to the directory that was passed into the function.
    cv2.imwrite(out, opened_img)
    # Return the opened image.
    return opened_img

# If this program is being run as the main program, then do the following.
if __name__ == '__main__':
    # Path is set to the second string that is input in the command line.
    path = sys.argv[1]
    # The image is set the grayscale image read from the pathway specified in command line.
    img =  cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # The open function is called on the image, and provided a pathway to write the image out to, - this is the second string input via the command line.
    open(img, sys.argv[2])