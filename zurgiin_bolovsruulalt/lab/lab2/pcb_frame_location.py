'''
Test code
'''
import os
import cv2
import numpy as numpy
from matplotlib import pyplot as plt





def hist_eq(img, display):
    """
        Applys histogram equalization to the given image, returning the
        resultant image
        @param img ( opencv2.imread ) - opencv image object
    """
    # Open image
    img = cv2.imread(img, 0)
    # Equalize
    equ = cv2.equalizeHist(img)   
    # Generate output
    output = numpy.hstack((img, equ))
    if display:
        cv2.imwrite('output.png', output)
    #generate output image
    return output

def harris_corner_detection(img, display):
    # Open image and convert to grayscale
    img = cv2.imread(img)
    img_gs = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_gs = numpy.float32(img_gs)
    dst = cv2.cornerHarris(img_gs, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    img[dst>0.01*dst.max()] = [0, 0, 255]
    cv2.imshow('dst', img)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    
    return dst

def find_pcb_frame(img, display):
    # load image
    image = cv2.imread(img)
    original = image.copy()

    # convert the image to grayscale, blur it, and find edges
    # in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)
    #cv2.imshow('Result of Canny ED', edged)
    #if cv2.waitKey(0) & 0xff == 27:
    #    cv2.destroyAllWindows()
    
    # find contours in the edged image, keep only the largest
    # ones, and initialize our frame contour
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    frameCnt = None

    # loop over our contours
    for c in cnts:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    


    # approximate the contour
    #peri = cv2.arcLength(cnts[0], True)
    #approx = cv2.approxPolyDP(cnts[0], 0.02 * peri, True)
        frameCnt = approx

        cv2.drawContours(image, [frameCnt], -1, (255, 0, 0), 3)
        output = numpy.hstack((original, image))
        cv2.imshow("PCB highlighted in blue", output)
        if cv2.waitKey(0) & 0xff == 27:
            cv2.destroyAllWindows()


def find_frame_0(img_path):
    img = cv2.imread(img_path)
    original = img.copy()
    # Calc image dimensions
    height, width, channels = img.shape
    area = height*width

    ## (1) Convert to gray, and threshold
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    th, threshed = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

    ## (2) Morph-op to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
    morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

    cv2.imshow("morphed",morphed)

    ## (3) Find the max-area contour
    cnts, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea)
    # iterate over contours to find the largest contour that isnt the image envelope
    index = len(cnts) - 1
    cnt = None
    print("Found {} contours".format(len(cnts)))
    while index >= 0:
        print("Image area = {}, contour area = {}".format(area*0.90, cv2.contourArea( cnts[index] )))
        if cv2.contourArea( cnts[index] ) < (area*0.90):
            cnt = cnts[index]
            break
        print(index)
        index -= 1
    if cnt == None:
        print("Error finding largest contour")
        cnt = cnts[-1]

    cv2.drawContours(img, [cnt], -1, (255, 0, 0), 3)
    output = numpy.hstack((original, img))
    cv2.imshow("PCB highlighted in blue", output)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()


'''
Main control flow
'''
if __name__ == '__main__':
   
    # Iterate over test-files
    for filename in os.listdir('./assets/frame_location_test'):
        if filename.endswith('.jpg'):
            image_path = os.path.join('./assets', filename)
            find_frame_0(image_path)

    #img_eq = hist_eq('./assets/inverter-pcb-board-500x500.jpg', True)
    #img_corners = harris_corner_detection('./assets/inverter-pcb-board-500x500.jpg', True)