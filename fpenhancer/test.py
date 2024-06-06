from fingerprint_image_enhancer import FingerprintImageEnhancer
import cv2
image_enhancer = FingerprintImageEnhancer() 
img = cv2.imread("../images/1.jpg")
if len(img.shape) > 2:  # convert image into gray if necessary
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
out = image_enhancer.enhance(img)  # run image enhancer
image_enhancer.save_enhanced_image("result.png")