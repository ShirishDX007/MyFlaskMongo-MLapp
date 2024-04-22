## Flask MongoDB ML Model Deployment

This project demonstrates how to deploy a machine learning model trained on CSV data to a MongoDB database using a Flask application. The deployed application exposes endpoints to load CSV data into MongoDB.

## Introduction
The project consists of a Flask application that serves as an API for loading CSV data into MongoDB and saves project meta data. The application uses Flask-PyMongo to interact with the MongoDB database and joblib to serialize and deserialize the machine learning model.and further to upload ML model to S3.

## Installation
To install the required dependencies, run the following command:

pip install -r requirements.txt

## Usage
To start the Flask application, run the following command:

python app.py

This will start the Flask development server, and the API endpoints will be accessible at 
http://localhost:5000.

## Endpoints
/load_data: POST endpoint to load CSV data into MongoDB database.
/: On home page you can the ML model evaluation result and s3 file location, csv_file_location

## Project Structure
The project structure is organized as follows:

* .
* ├── app.py                 # Main Flask application
* ├── config.py              # Configuration file
* ├── MLmodel.py             # Contains machine learning model and evaluation code
* ├── requirements.txt       # Dependencies
* ├── README.md              # Project documentation
* └── tests/                 # Unit tests
    └── test_app.py          # Test cases for the Flask application

## Dependencies

The project dependencies are listed in the requirements.txt file. You can install them using pip:

pip install -r requirements.txt