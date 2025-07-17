# Sentiment Analysis of Tweets  
## (Task 0 of Prodigy Data Science Internship)

Welcome! This repository contains a **complete sentiment analysis workflow** for social media posts (tweets). It is the first task (*task_0*) of my Prodigy Data Science Internship. The project helps you **analyze public sentiment** about any topic or brand using Twitter data, and provides code and visualizations to extract deep insights.

## Table of Contents

- [About the Project](#about-the-project)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Key Results](#key-results)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)
- [License](#license)

## About the Project

This project is a practical step-by-step guide to **analyzing and visualizing the sentiment of tweets**. It cleans raw social media data, detects sentiment (positive, negative, neutral, etc.), uncovers top keywords, and creates insightful graphics. This can help brands or individuals quickly understand public opinion and the main reasons behind it.

## Project Structure

| File/Folder            | Description                                                |
|------------------------|------------------------------------------------------------|
| `twitter_training.csv` | Raw Twitter dataset (input for analysis)                   |
| `sentiment_analysis.py`| Main Python script for cleaning, analyzing, and visualizing|
| `README.md`            | Project documentation (this file)                          |
| `charts/`              | Output folder for generated visualizations (after running the script) |

## Features

- **Data Cleaning**: Handles missing or empty tweets, standardizes input.
- **Sentiment Analysis**: Classifies tweets into Positive, Negative, Neutral, etc.
- **Keyword Extraction**: Identifies most frequent words per sentiment.
- **Visualization**: Generates easy-to-understand bar charts for sentiment distribution and top keywords.
- **Reusable Script**: All steps automated in a single script.

## Installation & Setup

### Requirements

| Package      | Version (or higher) | Purpose                   |
|--------------|---------------------|---------------------------|
| Python       | 3.7+                | Programming language      |
| pandas       | 1.0+                | Data handling             |
| matplotlib   | 3.0+                | Data visualization        |
| seaborn      | 0.10+               | Advanced visualization    |
| nltk         | 3.5+                | Natural Language Toolkit  |

### Setup Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/your-repo-name.git
   cd your-repo-name
   ```

2. **Install required libraries**:
   ```bash
   pip install pandas matplotlib seaborn nltk
   ```

3. **Download NLTK resources** (only run once):
   ```python
   import nltk
   nltk.download('stopwords')
   ```

4. **Put your CSV data** (`twitter_training.csv`) in the root directory.

## Usage Guide

1. **Run the Main Script**:
   ```bash
   python sentiment_analysis.py
   ```
   - The script will:
     - Clean and preprocess the tweets
     - Analyze sentiment for each tweet
     - Extract top keywords for each sentiment
     - Generate visualizations as PNG files in `charts/`

2. **Interpreting the Output**:
   - **Sentiment Distribution Bar Chart**: See the proportion of positive, negative, and neutral tweets.
   - **Top Keywords Charts**: Understand which topics drive the most emotions for each sentiment category.

## Key Results

| Insight                    | Description                                                                                                                |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Sentiment Distribution     | The most common sentiment is Negative, followed by Positive.                                                               |
| Top Positive Keywords      | Words like "love", "good", "great" signal what people appreciate.                                                           |
| Top Negative Keywords      | Words like "bad", "fix", "problem" help identify areas of concern or frustration.                                           |

## Technologies Used

- **Python:** Fast, flexible programming language for data science.
- **Pandas:** Data manipulation and cleaning.
- **Matplotlib/Seaborn:** Modern data visualization libraries.
- **NLTK:** Professional toolkit for language and sentiment analysis.

## Contributors

- **[Your Name]**
  - Prodigy Data Science Intern
  - []

## License

This project is licensed under the MIT License.

> For questions or suggestions, feel free to open an issue or contact me via email.  
> Happy analyzing!

[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/51244028/4ce6ff09-4b1f-4092-bf26-a9dc7cc77982/Task-4-Twitter.pdf