import os
import ast
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")

def generate_questions(skill: str) -> list:
    prompt = f"""
You are a highly experienced senior technical interviewer. Your task is to generate 5 unique, challenging, and highly relevant technical interview questions for the skill: **{skill}**.

Each question should test deep understanding, practical knowledge, and problem-solving ability related to the skill. Avoid generic or trivial questions.

Format your response strictly as a valid Python list of strings, for example:
[
    "Explain the concept of X and how it applies in real-world scenarios.",
    "Describe how you would solve Y problem using {skill}.",
    ...
]

Do not include any explanations or additional text, only the list of questions.
"""

    llm = init_chat_model(
        model="mistral-small",  
        model_provider="mistralai",
        temperature=0.7,
    )

    messages = [
        {"role": "user", "content": prompt}
    ]

    try:
        response = llm.invoke(messages)
        content = response.content if hasattr(response, "content") else str(response)
        questions = ast.literal_eval(content)
        if isinstance(questions, list):
            return questions
    except Exception as e:
        print("❌ LLM error:", e)
    return []
