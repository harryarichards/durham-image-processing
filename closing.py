import cv2 #Import cv2 so we can read and write images.
import sys #Import the sys package so we can deal with input from the command line.
from erosion import erode # Import the erode function from the erosion file.
from dilation import dilate # Import the dilate function from the dilation file.

def close(img, out):
    """
    'closes' an image and returns the closed image.
    'closing' involves dilating the image followed by eroding the image.
    also writes the closed image to a file as well as returning the closed image.

    :param img: the image to be closed.
    :param out: the path we're writing the closed image to.
    :return: return the closed image.
    """
    # Set the dilated image equal to the result of the dilate function performed on the image passed into the function.
    dilated_img = dilate(img, out)
    # Set the closed image equal to the result of the erode function performed on the dilated image.
    closed_img = erode(dilated_img, out)
    # Write the close image file to the directory that was passed into the function.
    cv2.imwrite(out, closed_img)
    # Return the closed image.
    return closed_img

# If this program is being run as the main program, then do the following.
if __name__ == '__main__':
    # Path is set to the second string that is input in the command line.
    path = sys.argv[1]
    # The image is set the grayscale image read from the pathway specified in command line.
    img =  cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # The close function is called on the image, and provided a pathway to write the image out to, - this is the second string input via the command line.
    close(img, sys.argv[2])