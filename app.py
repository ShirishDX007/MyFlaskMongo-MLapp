import os
import boto3
import joblib
import pandas as pd
import config
from flask import Flask, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from MLmodel import rf_pipeline, mse


app = Flask(__name__)

app.config["MONGO_URI"] = config.MONGO_URI

mongo = PyMongo(app)

class ProjectMetadata:
    def __init__(self, csv_file_location, s3_model_location, model_evaluation_results):
        self.csv_file_location = csv_file_location
        self.s3_model_location = s3_model_location
        self.model_evaluation_results = model_evaluation_results

@app.route('/load_data')
def load_data():

    csv_file_path = config.CSV_FILE_PATH
    data = pd.read_csv(csv_file_path)
    
    data_dict = data.to_dict(orient="records")
    collection = mongo.db.bigmart 
    collection.insert_many(data_dict)

    
    bucket_name = 'aws-us-gov-tenant'
    model_key = 'models/model.pkl'

    project_metadata = ProjectMetadata(
        csv_file_location=csv_file_path,
        s3_model_location=f's3://{bucket_name}/{model_key}',
        model_evaluation_results=mse
    )
    metadata_collection = mongo.db.Project_Metadata
    metadata_collection.insert_one(project_metadata.__dict__)

    return jsonify({"message": "Data loaded into MongoDB."})

@app.route('/')
def home():
    return jsonify({"message": "Hello! Welcome to home page."})

def main():
    s3_model_location = upload_model_to_AWS(rf_pipeline)

    csv_file_path = config.CSV_FILE_PATH
    project_metadata = ProjectMetadata(
        csv_file_location=csv_file_path,
        model_evaluation_results=mse,
        s3_model_location=s3_model_location
    )

def upload_model_to_AWS(rf_pipeline):
    s3 = boto3.client('s3')
    bucket_name = 'aws-us-gov-tenant'
    model_key = 'models/model.pkl'
    with open('model.pkl', 'wb') as f:
        joblib.dump(rf_pipeline, f)
    s3.upload_file('model.pkl', bucket_name, model_key)
    s3_model_location = f's3://{bucket_name}/{model_key}'
    os.remove('model.pkl')

    return s3_model_location

if __name__ == '__main__':
    main()
    app.run(debug=True)
