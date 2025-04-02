# AI-Powered Personalized News Aggregator

## Overview
This project is an AI-powered news aggregator that uses reinforcement learning (Multi-Armed Bandit) to personalize news recommendations based on user preferences. It fetches the latest news from different categories and adapts based on user feedback.

## Features
- Fetches real-time news from various categories using NewsAPI
- Uses reinforcement learning to adjust recommendations
- Learns user preferences based on feedback
- Saves and loads user preferences for better recommendations over time

## Installation

### Prerequisites
Ensure you have Python 3.7+ installed on your system.

### Install Dependencies
Run the following command to install required packages:
```bash
pip install requests
```

## Usage
1. Get a free API key from [NewsAPI](https://newsapi.org/).
2. Replace `your_news_api_key` in the script with your actual API key.
3. Run the script:
```bash
python ai_news_aggregator.py
```
4. The program will display news articles from a recommended category.
5. After reading, the user can provide feedback (`yes/no`), influencing future recommendations.

## How It Works
1. Initializes equal preference scores for each news category.
2. Uses a probability-weighted selection to choose a category.
3. Fetches top 5 articles from the selected category.
4. User provides feedback (`yes` = positive, `no` = neutral/negative).
5. Adjusts category preference based on feedback.
6. Saves user preferences to a JSON file for future sessions.

## Future Enhancements
- Improve recommendation accuracy using deep reinforcement learning.
- Add a web-based UI for better user interaction.
- Support multiple languages.
- Integrate with social media for trend analysis.
