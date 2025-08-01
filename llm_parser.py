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


def extract_skills_from_resume(text: str) -> list:
    prompt = f"""
            You are an expert resume parser specializing in AI and tools backed services. Your task is to extract the core AI-related technical skills from the given resume text, focusing on the content and projects section. Prioritize AI-related skills if present, but it is not mandatory to include only AI skills.

            Strict Guidelines:
            - Extract primarily AI-related technical skills (e.g., AI frameworks, machine learning libraries, AI tools, cloud AI services, APIs related to AI).
            - Exclude any soft skills, role titles, general terms, or skills not directly related to AI and tools backed services.
            - Do not hallucinate or invent skills not explicitly mentioned in the resume.
            - Output must be a valid Python list of strings (e.g., ['Python', 'TensorFlow', 'Docker']).
            - Include between 3 and 6 highly relevant technical skills based on the resume content.
            - Avoid repetition or variations of the same tool (e.g., don't include both 'Python' and 'python').

            Resume Text:
            \"\"\" 
            {text}
            \"\"\"

            Return:
            A Python list of strings.
            """
    messages = [
        SystemMessage(content="You are an expert resume parser."),
        HumanMessage(content=prompt)
    ]
    try:
        response = llm.invoke(messages)
        skills = eval(response.content)
        return skills
    except Exception as e:
        print("LLM parsing error:", e)
        return ["Python", "SQL", "Machine Learning"]
