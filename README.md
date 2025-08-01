# 🤖 AI Mock Interviewer

> **Intelligent Resume-Based Technical Interviews Powered by AI**

An advanced web application that automatically extracts skills from resumes and conducts personalized technical interviews using AI-powered question generation and real-time feedback.

## 🎬 Demo

**Live Demo & Portfolio**: [LinkedIn Profile](https://www.linkedin.com/in/abhinav-sunil-870184279/)

*Connect with me on LinkedIn to see this project in action and explore more of my work!*

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-green.svg)
![Mistral AI](https://img.shields.io/badge/Mistral%20AI-Small-orange.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-4.1+-purple.svg)

## ✨ Features

### 🎯 **Smart Resume Parsing**
- **AI-Powered Skill Extraction**: Automatically identifies technical skills from uploaded resumes
- **Intelligent Filtering**: Focuses on AI-related and technical skills while excluding soft skills
- **Context-Aware Analysis**: Processes resume content to extract relevant technical competencies

### 🧠 **Dynamic Question Generation**
- **Skill-Specific Questions**: Generates 5 unique, challenging technical questions per skill
- **Senior-Level Difficulty**: Questions designed to test deep understanding and practical knowledge
- **Real-World Scenarios**: Focuses on practical application rather than theoretical concepts

### 💬 **Real-Time AI Feedback**
- **Instant Evaluation**: Provides immediate feedback on each answer
- **Constructive Criticism**: Highlights strengths and specific areas for improvement
- **Professional Tone**: Maintains objective, actionable feedback throughout the interview

### 🎨 **Modern Web Interface**
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Intuitive UX**: Clean, professional interface with smooth navigation
- **Progress Tracking**: Visual indicators showing interview progress

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Node.js (for Tailwind CSS compilation)
- Mistral AI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-mock-interviewer.git
   cd ai-mock-interviewer
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies**
   ```bash
   npm install
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file
   echo "MISTRAL_API_KEY=your_mistral_api_key_here" > .env
   ```

5. **Compile Tailwind CSS**
   ```bash
   npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
   ```

6. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

7. **Open your browser**
   Navigate to `http://localhost:8000`

## 📋 Usage Guide

### 1. **Upload Resume**
- Visit the homepage and upload your resume (PDF, DOCX, or TXT format)
- The AI will automatically extract your technical skills

### 2. **Select Skill for Interview**
- Choose from the extracted skills displayed on the dashboard
- Each skill will generate a unique set of interview questions

### 3. **Complete the Interview**
- Answer each question thoughtfully
- Receive instant AI-powered feedback after each response
- Track your progress through the 5-question interview

### 4. **Review Feedback**
- Get constructive feedback highlighting your strengths
- Identify specific areas for improvement
- Use insights to enhance your technical knowledge

## 🏗️ Architecture

```
ai-mock-interviewer/
├── main.py                 # FastAPI application entry point
├── llm_parser.py          # Resume skill extraction using Mistral AI
├── llm_question_generator.py  # Dynamic question generation
├── llm_feedback_generator.py  # Real-time answer evaluation
├── templates/             # HTML templates
│   ├── file_uploader.html
│   ├── dashboard.html
│   └── interview.html
├── static/               # Static assets
│   └── css/
│       ├── input.css     # Tailwind CSS source
│       └── output.css    # Compiled CSS
└── requirements.txt      # Python dependencies
```

## 🔧 Configuration

### Environment Variables
```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

### API Endpoints
- `GET /` - Resume upload page
- `POST /dashboard` - Process resume and show skills
- `GET /interview/{skill}` - Start interview for specific skill
- `POST /interview/{skill}` - Submit answer and get feedback

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **AI/ML**: Mistral AI (Mistral-Small model)
- **Frontend**: HTML, Tailwind CSS
- **LLM Integration**: LangChain
- **Template Engine**: Jinja2
- **Development**: Uvicorn

## 🤝 Contributing

We welcome contributions! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the ISC License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Mistral AI** for providing the powerful language model
- **FastAPI** for the excellent web framework
- **Tailwind CSS** for the beautiful styling system
- **LangChain** for seamless LLM integration

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/yourusername/ai-mock-interviewer/issues) page
2. Create a new issue with detailed information
3. Include your Python version, error messages, and steps to reproduce

---

**Made with ❤️ for developers preparing for technical interviews**
