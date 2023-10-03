import cv2
import numpy as np

def matrices_equal_2d(m1, m2):
    try:
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                if m1[i][j] != m2[i][j]:
                    print (str(i)+' '+ str(j)+ ' ' +'error')
        print('as expected.')

    except:
        print("Could not properly compare matrices")
        return False
    return True

lena = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5,5),np.uint8)


erosion_created = cv2.imread("lena_erosion.png", cv2.IMREAD_GRAYSCALE)
erosion_expected = cv2.erode(lena, kernel)

dilation_created = cv2.imread("lena_dilation.png", cv2.IMREAD_GRAYSCALE)
dilation_expected = cv2.dilate(lena, kernel)

opening_created = cv2.imread("lena_opening.png", cv2.IMREAD_GRAYSCALE)
opening_expected = cv2.morphologyEx(lena, cv2.MORPH_OPEN, kernel)

closing_created = cv2.imread("lena_closing.png", cv2.IMREAD_GRAYSCALE)
closing_expected = cv2.morphologyEx(lena, cv2.MORPH_CLOSE, kernel)

matrices_equal_2d(erosion_created, erosion_expected)
matrices_equal_2d(dilation_created, dilation_expected)
matrices_equal_2d(opening_created, opening_expected)
matrices_equal_2d(closing_created, closing_expected)
