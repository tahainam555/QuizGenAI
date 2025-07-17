# 📘 QuizGen AI

> Automatically generate quizzes from course PDFs using AI — Summaries, MCQs, and Short Answers, all in one click.

![QuizGen Banner](https://via.placeholder.com/1200x300?text=QuizGen+AI+%7C+PDF+to+Quiz+Generator)

---

## 🚀 Overview

**QuizGen AI** is a smart quiz creation tool that reads your course PDFs and generates:

- ✅ A concise summary
- 📋 5 Multiple-Choice Questions (MCQs) with answers
- ✍️ 3 Short Answer Questions

Built using **Python**, **Streamlit**, and powered by **LLaMA3 via Groq API** — fully free and blazing fast.

---

## 🧠 Why Use It?

Whether you're:
- A **teacher** creating tests,
- A **student** preparing for exams,
- Or an **edtech startup** building smarter learning tools...

**QuizGen AI** simplifies quiz creation to **seconds**.

---

## 📂 Features

- 📄 Upload course PDFs
- 🧹 Automatic content cleaning
- 🤖 AI-based question generation (summary, MCQs, short answers)
- ⬇️ Downloadable output
- 💡 Clean, intuitive UI
- 🔌 No OpenAI or paid API required — uses **Groq’s free LLaMA3**

---

## 🛠️ Tech Stack

| Tech       | Description                |
|------------|----------------------------|
| `Python`   | Core backend logic         |
| `PyMuPDF`  | PDF text extraction        |
| `re`       | Cleaning and formatting    |
| `Groq API` | LLaMA3 model (for free AI) |
| `Streamlit`| Frontend + Interface       |

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/quizgen-ai.git
cd quizgen-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your Groq API key

Create a `.env` file or export manually:

```bash
export GROQ_API_KEY="your_groq_api_key"
```

(You can get one at [groq.com](https://groq.com))

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## ✨ Sample Output

```
Summary:
• Covers basics of Machine Learning
• Introduces supervised vs unsupervised learning
...

MCQ 1:
Which algorithm is used for classification?
A. Linear Regression
B. Decision Tree
...
Answer: B
```

---

## 📤 Demo Link

[🔗 Hosted on Streamlit Cloud](https://your-app-link.streamlit.app) *(if deployed)*

---

## 👤 Author

**M. Taha**  
AI Developer & Student — [LinkedIn](https://linkedin.com/in/your-profile)  
Building real-world AI tools for education and automation.

---

## 📝 License

This project is licensed under the MIT License.

---

## 💡 Ideas for Future Versions

- Support `.docx` and `.txt` files
- Custom number of questions
- Export as PDF or Word
- Multilingual support
