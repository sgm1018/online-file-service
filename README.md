# File Service Project

## Overview
The File Service Project is a web application that allows users to securely upload, store, and download files. The application is built using Flask, a lightweight web framework for Python, and provides a simple and user-friendly interface for managing files.

## Features
- **Upload Files:** Users can easily upload files to the server using the "Upload" page. The application ensures that the filenames are secure and avoids overwriting existing files.

- **Download Files:** The "Download" page displays a list of available files on the server. Users can click on a file name to download the corresponding file.

## Setup and Installation
To run the File Service Project locally, follow these steps:

1. Make sure you have Python installed. This project was developed using Python 3.10.

2. Clone this repository to your local machine.

3. Install the required dependencies by running the following command in your terminal or command prompt:
```python
pip install -r requirements.txt
```

4. Start the Flask application by running the following command:
```python
python app.py
```

5. Open your web browser and navigate to `http://localhost:5000` to access the application.

## Project Structure
The project is organized as follows:

- `app.py`: This is the main Flask application file that contains the routes and logic for handling file uploads and downloads.

- `templates/`: This directory contains the HTML templates for the different pages of the application.

- `static/`: This directory contains the static files, including the CSS styles and image files.

- `uploads/`: This directory is used to store the uploaded files.

## Dependencies
The project relies on the following external libraries:

- Flask: A micro web framework for Python.

## Contributing
If you would like to contribute to the File Service Project, you can fork this repository and submit pull requests with your proposed changes. All contributions are welcome!

## Author
The File Service Project was developed by **sgm1018**.
