import os
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.messages import HumanMessage,SystemMessage
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

llm = ChatMistralAI(
    api_key=api_key,
    model="mistral-small",
    temperature=0.3
)
def evaluate_answer(question: str, answer: str, skill: str) -> str:
    prompt = f"""
            You are a senior technical interviewer with deep expertise in {skill}. 

Your task is to evaluate a candidate's answer to a technical interview question.

Strict Instructions:
- Provide **concise, constructive feedback in no more than 2 sentences**.
- Clearly mention **one strength** in the answer.
- Clearly mention **one specific area for improvement**.
- Do **not** restate the question or the answer.
- Be **professional, objective, and actionable** in tone.

Question:
\"\"\"{question}\"\"\"

Candidate's Answer:
\"\"\"{answer}\"\"\"

            Your feedback (max 2 sentences):
            """
    messages = [
        {"role": "user", "content": prompt}
    ]

    try:
        response = llm.invoke(messages)
        return response.content if hasattr(response, "content") else str(response)
    except Exception as e:
        print("❌ LLM feedback error:", e)
        return "⚠️ Feedback generation failed."