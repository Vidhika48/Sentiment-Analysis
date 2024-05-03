# Sentiment Analysis Web Application

Welcome to the Sentiment Analysis Web Application repository! This project allows users to analyze the sentiment of text data through a simple web interface. Whether you're interested in understanding the sentiment of customer reviews, social media comments, or any other text data, this application provides a convenient solution.

## Overview

Sentiment analysis, also known as opinion mining, involves determining the emotional tone behind a series of words. It's a valuable tool for understanding attitudes, opinions, and emotions expressed within online content. This web application harnesses the power of machine learning to predict sentiment based on user-provided text data.

## How It Works

1. **Input Text**: Users input text data into the web application.
2. **Prediction**: The application utilizes pre-trained machine learning models to analyze the sentiment of the input text.
3. **Result**: Users receive the sentiment analysis prediction, providing insight into the emotional tone of the text.

## Usage

1. **Clone the Repository**: `git clone https://github.com/Vidhika48/Sentiment-Analysis`
2. **Navigate to the Directory**: `cd Sentiment-Analysis`
3. **Install Dependencies**: `pip install -r requirements.txt`
4. **Run the Application**: `python app.py`
5. **Access the Web Interface**: Open a web browser and go to `http://localhost:5000`

## Features

- User-friendly interface for easy text input and analysis.
- Pre-trained machine learning models for accurate sentiment prediction.
- Integration with Flask framework for web application development.

## File Structure
Sentiment-Analysis/
│
├── app.py
├── templates/
│   ├── home.html
│   └── prediction.html
├── static/
│   └── style.css
├── lr_bow.pkl
├── vectorizer.pkl
└── data.csv

## Credits

- **Vidhika48**: Project creator and developer.
- **Scikit-learn**: Machine learning library for model training and prediction.
- **Flask**: Web application framework for Python.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Feedback

Feedback, suggestions, and contributions are welcome! Feel free to open an issue or submit a pull request if you have any ideas for improving this project.

Enjoy analyzing sentiments with ease using the Sentiment Analysis Web Application!
