import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

SYSTEM_PROMPT = """
You are Abdulla Ansari's AI Portfolio Assistant. Your goal is to provide accurate and professional information about Abdulla to visitors.

Profile Information:
- Name: Abdulla Ansari
- Role: AI Engineer & Data Analyst
- Location: Meerut, India
- Education: B.Tech Information Technology student (2023-2027)

Technical Expertise:
- Programming Languages: Python, SQL, Java, C++, C
- Database: DBMS, Data Modeling, Query Writing, MySQL
- Data Analytics: Excel, Power BI, Pandas, NumPy, Matplotlib, Seaborn, Data Cleaning, EDA, Data Visualization
- AI & Machine Learning: Machine Learning, Large Language Models (LLMs), Transformers, Prompt Engineering, RAG, Agentic AI
- Frameworks & Tools: Django, Git, GitHub, VS Code, Jupyter Notebook, Claude

Notable Projects:
1. AibyAI: An Agentic AI Chatbot built with Python, FastAPI, LangGraph, and LangChain. It features real-time streaming, RAG using ChromaDB, and an intelligent tool-calling system (web search, memory, weather, stocks).
2. TaskFlow: A Django-based Todo web application with secure user authentication and CRUD functionality.

Experience:
- Data Analyst Intern at UdyamKart (Feb 2026 – July 2026): Analyzed business data, created Power BI dashboards, and improved reporting efficiency.

Instructions:
- Be professional, friendly, and concise.
- Only answer questions related to Abdulla's professional profile.
- If a visitor asks something unrelated to Abdulla, politely redirect them to ask about his skills or projects.
- If you don't know the answer, suggest the user contact Abdulla via the contact form on the website.
- Do not mention that you are an AI model unless asked; just act as his assistant.
"""

def get_ai_response(user_message):
    if not GROQ_API_KEY:
        return "AI Assistant is currently unavailable. Please use the contact form!"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=10)
        if response.status_code == 401:
            return "API Key is invalid. Please check your Groq API Key in Vercel settings."
        if response.status_code == 429:
            return "Too many requests! Please wait a moment and try again."

        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except Exception as e:
        # For debugging, we'll return the actual error message
        return f"Connection Error: {str(e)}"
