import os
from agno.agent import Agent

# Helper to get the model instance dynamically
def get_model_instance(provider, model_id, api_key):
    if provider == "Google Gemini":
        from agno.models.google import Gemini
        os.environ["GOOGLE_API_KEY"] = api_key
        return Gemini(id=model_id, api_key=api_key)
    elif provider == "Groq":
        from agno.models.groq import Groq
        os.environ["GROQ_API_KEY"] = api_key
        return Groq(id=model_id, api_key=api_key)
    elif provider == "OpenAI":
        from agno.models.openai import OpenAIChat
        os.environ["OPENAI_API_KEY"] = api_key
        return OpenAIChat(id=model_id, api_key=api_key)
    else:
        raise ValueError(f"Unknown provider: {provider}")

# Helper to define the agents dynamically with the chosen model
def get_investment_agents(model_instance):
    market_analyst = Agent(
        model=model_instance,
        description="Analyzes and compares stock performance over time.",
        instructions=[
            "Retrieve and compare stock performance from Yahoo Finance.",
            "Calculate percentage change over a 6-month period.",
            "Rank stocks based on their relative performance.",
            "Do not output any programming code (such as Python or code blocks). Write in plain markdown text."
        ],
        markdown=True
    )

    company_researcher = Agent(
        model=model_instance,
        description="Fetches company profiles, financials, and latest news.",
        instructions=[
            "Retrieve company information from Yahoo Finance.",
            "Summarize latest company news relevant to investors.",
            "Provide sector, market cap, and business overview.",
            "Do not output any programming code (such as Python or code blocks). Write in plain markdown text."
        ],
        markdown=True
    )

    stock_strategist = Agent(
        model=model_instance,
        description="Provides investment insights and recommends top stocks.",
        instructions=[
            "Analyze stock performance trends and company fundamentals.",
            "Evaluate risk-reward potential and industry trends.",
            "Provide top stock recommendations for investors.",
            "Do not output any programming code (such as Python or code blocks). Write in plain markdown text."
        ],
        markdown=True
    )

    team_lead = Agent(
        model=model_instance,
        description="Aggregates stock analysis, company research, and investment strategy.",
        instructions=[
            "Compile stock performance, company analysis, and recommendations.",
            "Ensure all insights are structured in an investor-friendly report.",
            "Rank the top stocks based on combined analysis.",
            "Clearly specify which stock is the single best stock to buy.",
            "Provide the absolute best time/entry strategy to buy that stock (e.g. key indicators to watch, buy on dips, etc.).",
            "Do not output any programming code (such as Python or code blocks). Write purely in formatted markdown."
        ],
        markdown=True
    )
    
    return market_analyst, company_researcher, stock_strategist, team_lead

# News Sentiment Analysis agent function
def analyze_news_sentiment(symbol, news_items, model_instance):
    if not news_items:
        return 0, "Neutral", "No recent news found."
    
    prompt = (
        f"Analyze the market sentiment for {symbol} based on these news titles:\n"
    )
    for idx, item in enumerate(news_items):
        prompt += f"{idx+1}. {item.get('title', 'No Title')}\n"
    
    prompt += (
        "\nProvide a response in the following format:\n"
        "SCORE: <a number from -100 to 100>\n"
        "SENTIMENT: <Positive, Neutral, or Negative>\n"
        "SUMMARY: <one-sentence summary of the sentiment reasoning>\n"
        "Make sure to follow the format exactly. Do not output anything else."
    )
    
    sentiment_agent = Agent(
        model=model_instance,
        description=f"Performs financial news sentiment analysis for {symbol}.",
        instructions=[
            "Determine an overall sentiment score from -100 (extremely bearish) to +100 (extremely bullish).",
            "Classify the sentiment as Positive, Neutral, or Negative.",
            "Write a concise, single-sentence summary explaining why."
        ]
    )
    
    try:
        response = sentiment_agent.run(prompt)
        content = response.content
        
        score = 0
        sentiment = "Neutral"
        summary = "No reasoning provided."
        
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("SCORE:"):
                score = int(float(line.replace("SCORE:", "").strip()))
            elif line.startswith("SENTIMENT:"):
                sentiment = line.replace("SENTIMENT:", "").strip()
            elif line.startswith("SUMMARY:"):
                summary = line.replace("SUMMARY:", "").strip()
                
        score = max(-100, min(100, score))
        return score, sentiment, summary
    except Exception as e:
        print(f"Error analyzing news sentiment for {symbol}: {e}")
        return 0, "Neutral", "Failed to analyze news sentiment."
