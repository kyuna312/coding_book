"""
    This test code is implemented following a few assumptions:
        1) We store the initial frame of the PCB as a global reference image
        2) When we capture the current frame, it will be a subset of the reference image
        3) When generating the tempalte, we can programatically determine the expected region
        that our graphical components are being placed onto
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

def template_match(img, template):
    img2 = img.copy()
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
                'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        # Apply template Matching
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img,top_left, bottom_right, 255, 10)
        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()

if __name__ == "__main__":
    img1 = cv2.imread("assets/template_match_test/Ganglion-FRONT-2.jpg", 0)
    #global_image = cv2.cvtColor( img1, cv2.COLOR_BGR2GRAY )
    img2 = cv2.imread("assets/template_match_test/Ganglion-zoomed.jpg", 0)
    #sub_image =  cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY) 


    template_match(img1, img2)