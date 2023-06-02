import os
import pytesseract
from PIL import Image
from flask import Flask, render_template, request

app = Flask(__name__)

# Configure the upload folder
app.config["UPLOAD_FOLDER"] = f"{os.getcwd()}/temp"

# Create the upload folder if it doesn't exist
if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])
    os.chmod(app.config["UPLOAD_FOLDER"], 755)


def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as image:
        # Apply OCR to the image and retrieve the text
        text = pytesseract.image_to_string(image)
        return text


def allowed_file(filename):
    # Check if the file has an allowed extension
    allowed_extensions = {"png", "jpg", "jpeg", "gif"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Check if a file was uploaded
        if "image" not in request.files:
            return render_template("index.html", error="No file uploaded.")

        image = request.files["image"]

        # Check if a file was selected
        if image.filename == "":
            return render_template("index.html", error="No file selected.")

        # Check if the file is valid
        if image and allowed_file(image.filename):
            # Save the uploaded image to a temporary folder
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], image.filename)
            image.save(image_path)
            os.chmod(image_path, 755)

            # Extract text from the uploaded image
            extracted_text = extract_text_from_image(image_path)

            # Remove the temporary image file
            os.remove(image_path)

            return render_template("index.html", text=extracted_text)
        else:
            return render_template("index.html", error="Invalid file format.")

    return render_template("index.html")


if __name__ == "__main__":
    # Run the Flask app
    app.run()
