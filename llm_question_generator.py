import os
import ast
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")

def generate_questions(skill: str, language: str = "Python") -> list:
    prompt = f"""
You are a highly experienced senior technical interviewer.

Your task:
- Generate **5 unique, relevant, and non-trivial interview questions** for a candidate skilled in **{skill}**.
- Out of the 5, include **at least 2 coding questions** that must be solved in **{language}**.
- The remaining questions should test deep understanding, real-world problem solving, or architecture-related knowledge.
- Avoid generic or overly basic questions.

**Output Format (must be a valid Python list of dicts like below)**:
[
    {{"type": "coding", "question": "Write a function in {language} to reverse a linked list."}},
    {{"type": "theory", "question": "Explain how garbage collection works in {skill}."}},
    ...
]

Do not include explanations. Only return the valid JSON-like Python list of question dictionaries.
"""

    llm = init_chat_model(
        model="mistral-small",
        model_provider="mistralai",
        temperature=0.7,
    )

    messages = [{"role": "user", "content": prompt}]

    try:
        response = llm.invoke(messages)
        content = response.content if hasattr(response, "content") else str(response)
        questions = ast.literal_eval(content)
        if isinstance(questions, list):
            return questions
    except Exception as e:
        print("❌ LLM error:", e)

    return []
