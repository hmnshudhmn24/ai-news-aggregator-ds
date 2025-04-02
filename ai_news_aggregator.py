import requests
import random
import json

# News API configuration
NEWS_API_KEY = "your_news_api_key"
NEWS_API_URL = "https://newsapi.org/v2/top-headlines?country=us&category={}&apiKey=" + NEWS_API_KEY

# Categories of news to personalize
NEWS_CATEGORIES = ["business", "entertainment", "health", "science", "sports", "technology"]

# Reinforcement Learning Model (Multi-Armed Bandit)
class NewsRecommender:
    def __init__(self):
        self.preferences = {category: 1 for category in NEWS_CATEGORIES}  # Initialize equal preference scores
        self.rewards = {category: 0 for category in NEWS_CATEGORIES}  # Track user engagement
    
    def choose_category(self):
        total = sum(self.preferences.values())
        probabilities = {category: self.preferences[category] / total for category in NEWS_CATEGORIES}
        return random.choices(list(probabilities.keys()), weights=probabilities.values(), k=1)[0]
    
    def update_preferences(self, category, reward):
        self.rewards[category] += reward
        self.preferences[category] += reward  # Increase preference for engaged categories
    
    def save_model(self, filename="preferences.json"):
        with open(filename, "w") as f:
            json.dump(self.preferences, f)
    
    def load_model(self, filename="preferences.json"):
        try:
            with open(filename, "r") as f:
                self.preferences = json.load(f)
        except FileNotFoundError:
            pass

# Fetch news based on recommended category
def get_news(category):
    response = requests.get(NEWS_API_URL.format(category))
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get("articles", [])
        return articles[:5]  # Get top 5 articles
    return []

# Main function
def main():
    recommender = NewsRecommender()
    recommender.load_model()
    
    category = recommender.choose_category()
    print(f"Fetching news from category: {category}")
    news_articles = get_news(category)
    
    if not news_articles:
        print("No news found.")
        return
    
    for idx, article in enumerate(news_articles):
        print(f"\nNews {idx + 1}: {article['title']}")
        user_feedback = input("Did you like this news? (yes/no): ").strip().lower()
        reward = 1 if user_feedback == "yes" else 0
        recommender.update_preferences(category, reward)
    
    recommender.save_model()

if __name__ == "__main__":
    main()
