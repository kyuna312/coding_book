
import sys
import cv2
import numpy as np

def find_overlay_region(img, display = False):
    """
        Locates the PCB in the given image frame.

        @param img (cv2.image) - Pointer to an openCV2 image object, returned from imread().
        @param display (bool) - If set to true, the image will be displayed as the code runs, for debug usage.

        @returns [(cv2.contour), [(int, int)] - Returns a tuple containing 1) the contour object returned by opencv & 2)
            the x,y co-ordinates of the centre point of the contour
    """
    # Make a copy of image if we're going to display
    if display:
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

    ## (3) Find the max-area contour, which should be the PCB
    im, cnts, hierarachy = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea)
    index = len(cnts) - 1
    cnt = False
    print("Found {} contours".format(len(cnts)))
    while index >= 0:
        print("Image area = {}, contour area = {}".format(area*0.90, cv2.contourArea( cnts[index] )))
        if cv2.contourArea( cnts[index] ) < (area*0.90):
            cnt = cnts[index]
            break
        index -= 1
    if isinstance(cnt, (int, float)) and cnt == False:
        print("Error finding largest contour, setting to default")
        cnt = cnts[-1]

    # Calculate center of contour
    moment = cv2.moments(cnt)
    x = int( moment["m10"] / moment['m00'] )
    y = int( moment['m01'] / moment['m00'] )

    # Draw the contour onto the original image
    if display:
        cv2.drawContours(img, [cnt], -1, (255, 0, 0), 3)
        output = np.hstack((original, img))
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('image', 800,800)
        cv2.imshow("image", output)
        if cv2.waitKey(0) & 0xff == 27:
            cv2.destroyAllWindows()
    
    # Return the contour & centre coordinates
    return [cnt, [x,y] ]

def overlay_image_alpha(img, img_overlay, pos, alpha_mask):
    """Overlay img_overlay on top of img at the position specified by
    pos and blend using alpha_mask.

    Alpha mask must contain values within the range [0, 1] and be the
    same size as img_overlay.
    """

    x, y = pos

    # Image ranges
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    # Overlay ranges
    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if nothing to do
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    channels = img.shape[2]

    alpha = alpha_mask[y1o:y2o, x1o:x2o]
    alpha_inv = 1.0 - alpha

    for c in range(channels):
        img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] +
                                alpha_inv * img[y1:y2, x1:x2, c])

if __name__ == '__main__':
    # Load full-frame image
    frame = cv2.imread("assets/overlay_test/Ganglion-FRONT-2.jpg")
    backup = frame.copy()
    # Load overlay image
    overlay = cv2.imread("assets/overlay_test/Ganglion-test-overlay.png")
    # Detect PCB contour in frame
    pcb_contour, center  = find_overlay_region(frame)
    # Determine offset of contour in frame
    x_offset, y_offset = center

    # While generating the overlay, we'll have some information with regards to where within
    # the PCB the various graphical components are located. The input data type can vary, but 
    # we need a way of knowing where to place it with respect to the center of the major PCB contour

    # Draw overlay onto frame and display
    overlay_image_alpha(frame,
                        overlay[:, :, 0:3],
                        (0,0),
                        overlay[:,:,2] / 255.0  )
    
    # Display new frame
    output = np.hstack((frame, backup ))
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 800,800)
    cv2.imshow("image", output)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()