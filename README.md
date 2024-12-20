# Movie Sentiment Prediction App

## Overview
This is a web application that predicts the sentiment behind movie reviews using the DistilBERT model.

## Installation

### Prerequisites
- Python 3.7+
- Flask
- transformers library
- Amazon EC2 instance

### Steps to Set Up Locally
1. Clone the repository:
    ```bash
    git clone https://github.com/jaishmau39/MoviePrediction_App.git
    cd MoviePrediction_App
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. The app will be running locally at `http://127.0.0.1:5000/`.

## Deployment

The app is deployed on Amazon EC2. Follow these steps to deploy it to your own EC2 instance:

1. Set up an EC2 instance on AWS.
2. SSH into the EC2 instance:
    ```bash
    ssh -i <your-key-pair.pem> ec2-user@<your-ec2-ip>
    ```

3. Install Python, Flask, and other dependencies on the EC2 instance.
4. Clone the repository and follow the local installation instructions.
5. Open the necessary ports on the EC2 security group for external access.

### Results:
In this project, both BERT and DistilBERT were trained and evaluated on the IMDb Movie Review dataset to predict the sentiment of movie reviews.
- **BERT** achieved a higher accuracy but had slower inference times and higher memory usage.
- **DistilBERT** provided a slightly lower accuracy but with significantly faster inference times and lower memory usage, making it a more efficient choice for real-time sentiment prediction in the web application.

Based on these results, **DistilBERT** was chosen for deployment in this project due to its better trade-off between performance and efficiency.

