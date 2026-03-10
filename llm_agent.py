from groq import Groq
import os

client = Groq(
    api_key="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"
)

def generate_response(question, analysis_result):

    prompt = f"""
You are a business intelligence assistant for company founders.

User Question:
{question}

Data Analysis Result:
{analysis_result}

Provide:
1. Clear answer
2. Business insights
3. Any data quality warnings
"""

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return completion.choices[0].message.content