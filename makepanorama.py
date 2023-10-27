import cv2
import numpy as np

def stitch_images(img1, img2):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Detect ORB keypoints and descriptors
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)
    
    # Use BruteForce Matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(descriptors1, descriptors2)
    
    # Sort matches based on their distances
    matches = sorted(matches, key = lambda x:x.distance)
    
    # Extract location of good matches
    points1 = np.zeros((len(matches), 2), dtype=np.float32)
    points2 = np.zeros((len(matches), 2), dtype=np.float32)
    
    for i, match in enumerate(matches):
        points1[i, :] = keypoints1[match.queryIdx].pt
        points2[i, :] = keypoints2[match.trainIdx].pt
    
    # Find homography
    h, mask = cv2.findHomography(points1, points2, cv2.RANSAC)
    
    # Use this matrix to transform the images
    height, width, channels = img2.shape
    panorama = cv2.warpPerspective(img1, h, (width * 2, height))
    panorama[0:height, 0:width] = img2
    
    return panorama

if __name__ == "__main__":
    img1 = cv2.imread('sogang4.jpg')
    img2 = cv2.imread('sogang3.jpg')
    resize_img1 = cv2.resize(img1, (1024, 1024))
    resize_img2 = cv2.resize(img2, (1024, 1024))

    panorama = stitch_images(resize_img1, resize_img2)

    cv2.imshow('Panorama', panorama)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('./sogang panorama2 1024x1024.jpg',panorama)