# 🤖 AI Mock Interviewer

> **Revolutionary AI-Powered Technical Interview Platform**

Transform your interview preparation with our cutting-edge AI system that automatically extracts skills from your resume and conducts personalized, senior-level technical interviews with real-time feedback.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-green.svg)](https://fastapi.tiangolo.com)
[![Mistral AI](https://img.shields.io/badge/Mistral%20AI-Small-orange.svg)](https://mistral.ai)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-4.1+-purple.svg)](https://tailwindcss.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![License](https://img.shields.io/badge/License-ISC-green.svg)](LICENSE)

---

## ✨ New Features in This Version

- 🎨 **Sleek New UI Design:** Modern, responsive, and user-friendly interface powered by Tailwind CSS
- 🚀 **Improved Performance:** Optimized backend and frontend for faster load times and smoother interactions
- 🧠 **Enhanced AI Feedback:** More detailed and actionable interview feedback powered by Mistral AI
- 🔄 **Seamless Interview Flow:** Intuitive navigation and progress tracking for a better user experience
- 🛠️ **Robust Error Handling:** Improved stability and error messages for smoother usage

---

## 🎯 What Makes This Special?

This isn't just another interview practice tool. Our AI Mock Interviewer leverages advanced language models to:

- **🔍 Intelligently parse your resume** and extract technical skills with surgical precision
- **🧠 Generate senior-level questions** that test deep understanding, not just surface knowledge
- **⚡ Provide instant, constructive feedback** that actually helps you improve
- **🎯 Focus on real-world scenarios** that mirror actual technical interviews

---

## 🚀 Lightning-Fast Deployment

### Option 1: Docker (Recommended) ⚡

The fastest way to get started - no setup required!

```bash
# Pull the latest image
docker pull iamabhinav2005/ai-mock-interviewer:latest

# Run the application
docker run -p 8000:8000 iamabhinav2005/ai-mock-interviewer
```

**That's it!** 🎉 Open your browser and navigate to `http://localhost:8000`

### Option 2: Local Development Setup

For developers who want to customize and contribute:

<details>
<summary><b>📋 Prerequisites</b></summary>

- Python 3.8 or higher
- Node.js (for Tailwind CSS compilation)
- Mistral AI API key

</details>

<details>
<summary><b>🔧 Installation Steps</b></summary>

1. **Clone the repository**
   ```bash
   git clone https://github.com/IamAbhinav01/ai-mock-interviewer.git
   cd ai-mock-interviewer
   ```

2. **Install dependencies**
   ```bash
   # Python dependencies
   pip install -r requirements.txt
   
   # Node.js dependencies
   npm install
   ```

3. **Configure environment**
   ```bash
   # Create .env file
   echo "MISTRAL_API_KEY=your_mistral_api_key_here" > .env
   ```

4. **Compile assets**
   ```bash
   npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
   ```

5. **Launch the application**
   ```bash
   uvicorn main:app --reload
   ```

</details>

---

## ✨ Core Features

### 🎯 **Intelligent Resume Analysis**
- **AI-Powered Skill Extraction**: Automatically identifies technical skills from uploaded resumes
- **Smart Filtering**: Focuses on AI-related and technical skills while excluding soft skills
- **Context-Aware Processing**: Deep understanding of resume content and skill relevance

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
- **Integrated Code Editor**: Interactive Monaco code editor for coding questions with real-time execution and output display

---

## 📋 How It Works

### 1. **Upload Your Resume** 📄
Upload your resume in PDF, DOCX, or TXT format. Our AI will analyze it and extract your technical skills.

### 2. **Select Your Focus** 🎯
Choose from the extracted skills displayed on your personalized dashboard.

### 3. **Ace Your Interview** 💪
Answer 5 challenging questions per skill with real-time AI feedback.

### 4. **Level Up** 📈
Review detailed feedback highlighting your strengths and areas for improvement.

---

## 🏗️ Architecture Overview

```
ai-mock-interviewer/
├── main.py                    # FastAPI application entry point
├── llm_parser.py             # Resume skill extraction using Mistral AI
├── llm_question_generator.py # Dynamic question generation
├── llm_feedback_generator.py # Real-time answer evaluation
├── templates/                # HTML templates
│   ├── file_uploader.html
│   ├── dashboard.html
│   └── interview.html
├── static/                  # Static assets
│   └── css/
│       ├── input.css        # Tailwind CSS source
│       └── output.css       # Compiled CSS
├── Dockerfile               # Docker configuration
└── requirements.txt         # Python dependencies
```

---

## 🔧 Configuration

### Environment Variables
```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

### API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Resume upload page |
| `/dashboard` | POST | Process resume and show skills |
| `/interview/{skill}` | GET | Start interview for specific skill |
| `/interview/{skill}` | POST | Submit answer and get feedback |

---

## 🛠️ Technology Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Backend** | FastAPI (Python) | High-performance web framework |
| **AI/ML** | Mistral AI (Mistral-Small) | Advanced language model |
| **Frontend** | HTML + Tailwind CSS | Modern, responsive UI |
| **LLM Integration** | LangChain | Seamless AI integration |
| **Template Engine** | Jinja2 | Dynamic HTML generation |
| **Development** | Uvicorn | ASGI server |
| **Containerization** | Docker | Easy deployment |

---

## 🚀 Deployment Options

### Docker Deployment
```bash
# Production deployment
docker run -d -p 8000:8000 --name ai-interviewer iamabhinav2005/ai-mock-interviewer:latest

# With custom environment variables
docker run -d -p 8000:8000 \
  -e MISTRAL_API_KEY=your_key_here \
  --name ai-interviewer \
  iamabhinav2005/ai-mock-interviewer:latest
```

### Docker Compose
```yaml
version: '3.8'
services:
  ai-interviewer:
    image: iamabhinav2005/ai-mock-interviewer:latest
    ports:
      - "8000:8000"
    environment:
      - MISTRAL_API_KEY=${MISTRAL_API_KEY}
    restart: unless-stopped
```

---

## 🤝 Contributing

We love contributions! Here's how you can help:

### 🐛 Bug Reports
Found a bug? Please [open an issue](https://github.com/IamAbhinav01/ai-mock-interviewer/issues) with:
- Detailed description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment details

### 💡 Feature Requests
Have an idea? We'd love to hear it! Open an issue and let's discuss.

### 🔧 Code Contributions
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/IamAbhinav01/ai-mock-interviewer)
![GitHub forks](https://img.shields.io/github/forks/IamAbhinav01/ai-mock-interviewer)
![GitHub issues](https://img.shields.io/github/issues/IamAbhinav01/ai-mock-interviewer)
![GitHub pull requests](https://img.shields.io/github/issues-pr/IamAbhinav01/ai-mock-interviewer)

---

## 📝 License

This project is licensed under the ISC License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Mistral AI** for providing the powerful language model
- **FastAPI** for the excellent web framework
- **Tailwind CSS** for the beautiful styling system
- **LangChain** for seamless LLM integration
- **Docker** for containerization support

---

## 📞 Support & Community

### Getting Help
- 📖 **Documentation**: Check this README first
- 🐛 **Issues**: [GitHub Issues](https://github.com/IamAbhinav01/ai-mock-interviewer/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/IamAbhinav01/ai-mock-interviewer/discussions)

### Connect With Us
- 🌐 **LinkedIn**: [Abhinav Sunil](https://www.linkedin.com/in/abhinav-sunil-870184279/)
- 📧 **Email**: Reach out through GitHub

---

<div align="center">

**🚀 Ready to ace your next technical interview?**

[![Deploy with Docker](https://img.shields.io/badge/Deploy%20with-Docker-blue?style=for-the-badge&logo=docker)](https://hub.docker.com/r/iamabhinav2005/ai-mock-interviewer)

*Made with ❤️ for developers preparing for technical interviews*

</div>
