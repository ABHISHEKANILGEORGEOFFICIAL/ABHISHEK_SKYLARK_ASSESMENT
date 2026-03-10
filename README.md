# Monday.com Business Intelligence Agent

This project implements an AI-powered Business Intelligence agent that answers founder-level questions using monday.com data.
#Setup Instructions for Evaluator

Open the deployed app.

Enter the following board IDs:

Deals Board ID: 5027109850
Work Orders Board ID: 5027111015

Ask questions such as:

How is our pipeline?
Show leadership update
## Features

- Monday.com API integration
- Handles messy real-world data
- Pipeline analysis
- Leadership update generator
- Interactive charts
- Conversational interface

## Architecture

User Query → Streamlit Agent → Monday API → Data Cleaning → Analytics Engine → Insights

## Tech Stack

- Python
- Streamlit
- Pandas
- Monday.com API
- Plotly

## Running

1. Add Monday API key

export MONDAY_API_KEY=your_api_key

2. Run


streamlit run app.py
