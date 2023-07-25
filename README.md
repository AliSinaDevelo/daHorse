# daHorse - Chessboard to FEN Converter

daHorse is a Python program that takes an image of a chessboard as input and converts its position to FEN (Forsyth-Edwards Notation) format. It uses Convolutional Neural Networks (CNNs) for chessboard recognition and the python-chess library for FEN conversion.

## Features

- Preprocesses the input image to find the chessboard contours.
- Extracts individual chessboard squares.
- Uses a trained CNN model to interpret the chessboard position.
- Converts the chessboard position to FEN format.
- Generates an SVG representation of the chessboard.

## Requirements

- Python 3.6 or higher
- OpenCV (cv2) library
- tensorflow library
- python-chess library
- Flask (for the optional web interface)

## Installation

1. Clone the repository:
    git clone https://github.com/AliSinaDevelo/daHorse.git
    cd daHorse


2. Install the required libraries:
    pip install -r requirements.txt


## Usage

To convert a chessboard image to FEN format, run the main script:

python src/main.py path/to/chessboard_image.jpg


The FEN position will be saved in the `data/fen_output.txt` file, and the SVG representation of the chessboard will be saved in `data/chessboard.svg`.

To use the web interface (optional), run the Flask app:

cd app
python app.py


Visit `http://127.0.0.1:5000/` in your web browser, upload a chessboard image, and get the FEN position and SVG representation.

## Dataset

The labeled dataset used for training the CNN model should be organized as follows:
data/labeled_dataset/
|-- empty/
| |-- square_0.jpg
| |-- square_1.jpg
| |-- ...
|-- pawn/
| |-- square_2.jpg
| |-- square_3.jpg
| |-- ...
|-- ...


## Training the CNN Model (Optional)

If you want to train your own CNN model for chessboard recognition:

1. Prepare the labeled dataset in the above format.
2. Run the training script:

python src/train_cnn_model.py


The trained model will be saved in the `data/trained_models/` directory.

## Testing

To test the entire "daHorse" program:
python tests/test_main.py


To run unit tests:
python tests/test_unit.py


## Contributing

Contributions are welcome! If you find any bugs or have ideas for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.




