# 🤖 AI Mock Interviewer - Data Scientist Role

An intelligent mock interview application powered by Google's Gemini AI and CrewAI framework. This interactive tool helps aspiring Data Scientists practice technical interviews with real-time AI-powered feedback.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Interview Questions](#interview-questions)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Contributing](#contributing)


## 🎯 Overview

AI Mock Interviewer is a Streamlit-based web application that simulates a technical interview for Data Scientist positions. It asks role-specific questions, evaluates your answers using Google's Gemini AI, and provides constructive feedback to help you improve your interview skills.

## ✨ Features

- **Interactive Interview Experience**: Clean, user-friendly interface built with Streamlit
- **AI-Powered Feedback**: Utilizes Google Gemini 2.5 Flash model for intelligent answer evaluation
- **Progress Tracking**: Visual progress bar showing your interview completion status
- **6 Targeted Questions**: Carefully curated questions covering key Data Science concepts
- **Constructive Feedback**: Receive 2-3 sentence feedback highlighting strengths and areas for improvement
- **Complete Session Summary**: Review all questions, answers, and feedback at the end
- **Restart Capability**: Practice multiple times to improve your responses
- **STAR Method Tips**: Built-in interview tips in the sidebar
- **Secure API Key Handling**: Support for environment variables or secure input

## 🛠️ Technology Stack

- **Frontend**: Streamlit 1.32.0
- **AI Framework**: CrewAI 0.28.8
- **LLM**: Google Gemini 2.5 Flash (via google-generativeai)
- **Environment Management**: python-dotenv 1.0.1
- **Language**: Python 3.x

## 📁 Project Structure

```
AI-mock-interviewer/
│
├── app.py              # Main Streamlit application
├── agents.py           # CrewAI agent definitions
├── tasks.py            # Interview questions and task creation
├── crew.py             # Gemini API integration for feedback generation
├── requirements.txt    # Python dependencies
├── .env                # Environment variables (API keys)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

### File Descriptions

- **app.py**: The main application file that handles the Streamlit UI, session state management, and user interaction flow
- **agents.py**: Defines CrewAI agents (Question Generator and Interview Coach)
- **tasks.py**: Contains the list of interview questions and task creation logic
- **crew.py**: Implements direct Gemini API calls for generating feedback
- **requirements.txt**: Lists all Python package dependencies

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- A Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI-mock-interviewer.git
   cd AI-mock-interviewer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

### Option 1: Using .env File (Recommended)

1. Create a `.env` file in the project root:
   ```bash
   touch .env
   ```

2. Add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### Option 2: Enter at Runtime

Simply run the application, and you'll be prompted to enter your API key securely in the web interface.

## 💻 Usage

1. **Start the application**
   ```bash
   streamlit run app.py
   ```

2. **Access the web interface**
   - The application will automatically open in your default browser
   - If not, navigate to `http://localhost:8501`

3. **Enter your API key** (if not using .env)
   - Enter your Gemini API key in the provided field

4. **Answer interview questions**
   - Read each question carefully
   - Type your answer in the text area
   - Click "Submit Answer" to receive feedback

5. **Review feedback**
   - Read the AI-generated feedback
   - Click "Next Question" to proceed
   - After all questions, review your complete session summary

6. **Restart if needed**
   - Click "Restart Interview" to practice again

## 📝 Interview Questions

The application covers 6 essential Data Science topics:

1. **Overfitting**: Prevention strategies and detection
2. **Supervised vs Unsupervised Learning**: Key differences and examples
3. **Cross-Validation**: Importance in model evaluation
4. **Bias-Variance Trade-off**: Impact on model performance
5. **Regression vs Classification**: Real-world applications
6. **Missing Data Handling**: Preprocessing techniques

## 🔍 How It Works

### Architecture

1. **User Interface Layer** (app.py)
   - Streamlit handles the web interface
   - Session state tracks progress and answers
   - Form submission triggers feedback generation

2. **AI Agent Layer** (agents.py)
   - CrewAI agents define roles and goals
   - Question Generator agent (not actively used)
   - Interview Coach agent provides feedback persona

3. **Task Management** (tasks.py)
   - Stores predefined interview questions
   - Creates feedback evaluation tasks

4. **AI Integration** (crew.py)
   - Direct Gemini API integration
   - Generates personalized feedback (2-3 sentences)
   - Uses gemini-2.5-flash model for fast responses

### Feedback Generation Process

```
User Answer → Gemini API → Prompt Engineering → AI Feedback → Display
```

The feedback prompt instructs the AI to:
- Acknowledge correct points
- Identify missing details or misconceptions
- Suggest improvements
- Maintain an encouraging, professional tone

## 📦 Requirements

```
crewai==0.28.8
streamlit==1.32.0
google-generativeai
python-dotenv==1.0.1
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Ideas for Contribution

- Add more interview questions
- Support for multiple job roles (ML Engineer, Data Analyst, etc.)
- Voice-based interview mode
- Timer for timed responses
- Difficulty levels (Junior, Mid, Senior)
- Export interview results as PDF
- Multi-language support

