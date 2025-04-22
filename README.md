# 💻 Code Generator Chatbot using Seq2Seq Transformer & Flask

## 📖 Overview

Turn your ideas into code through conversation. This AI-powered chatbot allows users to describe programming tasks in plain language and receive working code in return. Whether it's “How to delete a row in SQL?”, “Write a Python loop”, or “JavaScript function to validate email”, the system uses a fine-tuned Seq2Seq Transformer model to generate the appropriate code snippet in real time. 

---

## 📂 Features

- 🤖 **Natural Language to Code Generation**  
  Converts programming-related questions or prompts into relevant code snippets.

- 🧠 **Seq2Seq Transformer Architecture**  
  Fine-tuned for code generation using Hugging Face's Transformers.

- 💬 **Flask Web Interface**  
  Lightweight interface for submitting queries and receiving code.

- 🚀 **Real-Time Code Responses**  
  Generates responses on-the-fly for dynamic interaction.

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask** – for the web interface
- **Hugging Face Transformers** – for Seq2Seq modeling
- **Torch / TensorFlow** – backend framework for training/inference
- **Jupyter Notebook** – for training, fine-tuning, and testing

---

## 🚀 Installation & Setup

### 📦 Prerequisites

- Python 3.7 or higher
- Pretrained/fine-tuned Seq2Seq model for code generation

### 🔧 Setup

```bash
git clone https://github.com/your-username/codegen-chatbot-flask.git
cd codegen-chatbot-flask
pip install flask transformers torch
```

> ⚠️ Make sure to include the fine-tuned model directory or path in the notebook or app.

---

## ▶️ Running the Flask App

```bash
python app.py
```

Then open in your browser:  
`http://127.0.0.1:5000/`

---

## 💬 Example Queries

- `"Generate a Python function to reverse a list"`  
- `"Write a JavaScript function to validate an email"`  
- `"Give me HTML for a contact form"`  

And get code snippets instantly.

---

## 📌 Future Enhancements

- 📚 **Add Language Toggle** (Python, JS, Java, etc.)
- 🧠 **Fine-Tune on Larger Code Datasets**
- 🔍 **Syntax Highlighting for Output Code**
- 🌍 **Multilingual Query Support**

---

🚀 **Transforming ideas into code—instantly.**
