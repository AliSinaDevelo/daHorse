import cv2
import numpy as np

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    return blurred_image

def find_chessboard_contours(image):
    edges = cv2.Canny(image, 50, 150)
    contours, _= cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    chessboard_contours = []
    for contour in contours:
        epsilon: 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            chessboard_contours.append(approx)

    return chessboard_contours

def extract_chessboard_squares(image, chessboard_contours):
    squares = []
    for contour in chessboard_contours:
        
        contour = np.squeeze(contour)
        contour = contour[np.argsort(contour[:, 0])]

        width = int(np.linalg.norm(contour[1] - contour[0]))
        height = int(np.linalg.norm(contour[3] - contour[0]))

        dst_rect = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)

        M = cv2.getPerspectiveTransform(contour.astype(np.float32), dst_rect)
        square = cv2.warpPerspective(image, M, (width, height))

        squares.append(square)

    return squares