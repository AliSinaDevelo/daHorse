import os
import cv2
from image_processing import preprocess_image, find_chessboard_contours, extract_chessboard_squares

def main():
    image_path = 'data/raw_images/chessboard.jpg'

    preprocessed_image = preprocess_image(image_path)

    chessboard_contours = find_chessboard_contours(preprocessed_image)

    squares = extract_chessboard_squares(preprocessed_image, chessboard_contours)

    for idx, square in enumerate(squares):
        output_path = os.path.join('data/processed_images/', f'square_{idx}.jpg')
        cv2.imwrite(output_path, square)

if __name__ == '__main__':
    main()
