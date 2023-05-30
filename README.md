# Image OCR Web Application

A web application that extracts text from images using OCR (Optical Character Recognition) technology.

## Prerequisites

- Python 3.x
- Tesseract OCR library
- Flask

## Getting Started

1. Clone the repository:

   ```shell
   git clone https://github.com/tuannguyen-TN/image-ocr-web-app.git
   ```

2. Install the dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Run the application:

   ```shell
   flask --app app --debug run
   ```

4. Open your web browser and visit http://localhost:5000.

## Usage

1. On the web page, click on the "Choose File" button and select an image file (.png, .jpg, .jpeg, or .gif).

2. Click the "Extract Text" button.

3. The application will extract the text from the uploaded image and display it on the web page.

## Customization

- To customize the UI, you can modify the HTML code in the templates/index.html file.

- To extend the OCR capabilities or add additional features, you can modify the Python code in the app.py file.

## Limitations

- The accuracy of text extraction may vary depending on the quality of the image and the clarity of the text, as well as the intended language of the input.

- Performance may be affected by the size and complexity of the image.

- This application is intended for extracting text from images and may not be suitable for other OCR use cases.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/)
