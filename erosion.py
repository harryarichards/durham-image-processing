import cv2 #Import cv2 so we can read and write images.
import sys #Import the sys package so we can deal with input from the command line.
# The is the neighbours function which returns a list of the neighbours of the pixel with coordinates x,y.
def neighbours(x, y, img):
    """
    formulates and returns a list of the values of the pixels neighbouring the current pixel in question.
    neighbouring pixels are within 2 pixels in any direction of the current pixel in question.

    :param x: the x-coordinate of the current pixel in question.
    :param y: the y-coordinate of the current pixel in question.
    :param img: the image we're eroding.
    :return: a list of the values of the pixels that neighbour (are within 2 pixels in any direction of) the current pixel.
    """
    # Set h (height) equal to the number of rows in the image that's been passed in.
    # Set w (width) equal to the number of columns in the image that's been passed in.
    h, w = img.shape
    # Instantiate the neighbours array as 0.
    neighbours_array = []
    # Consider the x coordinate 2 left of the x-coordinate and 2 right of the x-coordinate.
    # If the x coordinate exceeds the width of the image use the width of the image as the x-coordinate.
    # If the x coordinate is less than 0 use 0 as the x-coordinate.
    for i in range(max(0, x-2), min(w, x + 3)):
        # Consider the y coordinate 2 down from the y-coordinate and 2 upwards of the y-coordinate.
        # If the y coordinate exceeds the height of the image use the height of the image as the x-coordinate.
        # If the y coordinate is less than 0 use 0 as the y-coordinate.
        for j in range(max(0, y - 2), min(h, y + 3)):
            # Add the pixel with coordinates [i, j] to the neighbours array.
            neighbours_array.append(img[i][j])
    # Return the neighbours array, this will be the set of pixels that are with 2 rows and 2 columns from the pixel in question.
    return neighbours_array

def erode(img, out):
    """
    erodes the image provided.
    eroding involves setting a pixels value to the minimum of it and its neighbouring pixels values.
    neighbouring pixels are any pixel within 2 pixels of the pixel in question.
    also writes the eroded image to a file as well as returning the eroded image.

    :param img: the image we're eroding.
    :param out: the path we're writing the eroded image to.
    :return: the eroded image.
    """
    # Set h (height) equal to the number of rows in the image.
    # Set w (width) equal to the number of columns in the image.
    h, w = img.shape
    # Set the eroded image to a copy of the image that's been passed in.
    eroded_img = img.copy()
    # Consider every possible x (horizontal) coordinate in the image.
    for x in range(0, w):
        # Consider every possible y (vertical) coordinate in the image.
        for y in range(0, h):
            #Set the neighbours array equal to all the pixels within 2 rows and 2 columns of the pixel in question for the image passed in.
            neighbours_array = neighbours(x, y, img)
            #Set the pixel in the eroded image with coordinates [x,y] equal to the minimum of the pixels in the neighbours array.
            eroded_img[x][y] = min(neighbours_array)
    # Write the eroded image file to the directory that was passed into the function.
    cv2.imwrite(out, eroded_img)
    # Return the eroded image.
    return eroded_img

# If this program is being run as the main program, then do the following.
if __name__ == '__main__':
    # Path is set to the second string that is input in the command line.
    path = sys.argv[1]
    # The image is set the grayscale image read from the pathway specified in command line.
    img =  cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # The erode function is called on the image, and provided a pathway to write the image out to, - this is the second string input via the command line.
    erode(img, sys.argv[2])