# AI Investment Strategist

AI-powered Stock Market Analysis Agent is a robust, modular application designed to instantly analyze multiple stocks using the AGNO Agentic AI library and leading language models (Google Gemini, Groq, OpenAI).

The project is cleanly separated into two main components:
- **`app.py`**: The Streamlit frontend, interactive KPI dashboard, news sentiment indicators, and portfolio allocation visualization.
- **`investment.py`**: The backend logic containing the specialized AGNO AI Agents (Market Analyst, Company Researcher, Stock Strategist, Team Lead).

## Key Features

- **Multi-Model Support**: Dynamically switch between Gemini, Groq, and OpenAI models via the sidebar.
- **Live KPI Dashboard**: Real-time stock prices, PE ratios, and dividend yields.
- **News Sentiment Gauge**: Instant sentiment scoring and summary based on recent company news.
- **Portfolio Simulator**: Input a budget and risk tolerance to get an AI-recommended asset breakdown.
- **Interactive Technical Charts**: Visualize up to 5 years of historical performance with optional Simple Moving Averages (SMA).
- **Downloadable Reports**: Export your personalized investment report directly to Markdown.

## The Agentic AI Team

1. **Market Analyst Agent**: Analyzes recent stock history and ranks stocks based on percentage change.
2. **Company Researcher Agent**: Gathers business profiles, market cap, and latest news sentiment.
3. **Stock Strategist Agent**: Takes market and company research to generate portfolio allocations tailored to your risk appetite.
4. **Team Lead Agent**: Compiles the data from all agents, making a definitive "Buy" decision and producing the final comprehensive report.

## Requirements

- Python 3.10+
- At least one API key: Google AI Studio, Groq, or OpenAI

## Setup

1. **Clone the repository and enter the directory**:
   ```bash
   git clone https://github.com/Jimikapz-18/StockMarketAgenticAI.git
   cd StockMarketAgenticAI
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # macOS/Linux
   source .venv/bin/activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **(Optional) Configure default environment variables**:
   ```bash
   cp .env.example .env
   ```
   *Add your API keys to `.env` to avoid typing them into the UI every time.*

## How to Run

Launch the Streamlit dashboard by running the main app file:
```bash
streamlit run app.py
```

Open the provided local URL (usually `http://localhost:8501`) in your browser to start your AI Investment Strategist!

