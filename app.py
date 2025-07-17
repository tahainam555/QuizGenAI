import fitz  # PyMuPDF
import re
import os
from groq import Groq
import streamlit as st

os.environ["GROQ_API_KEY"] = "Your_Groq_API_Key_Here"  # Set your Groq API key

# ===== PDF Extraction =====
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    doc.close()
    return full_text

# ===== Text Cleaning =====
def clean_pdf_text(raw_text):
    text = re.sub(r'\n{2,}', '\n', raw_text)
    text = re.sub(r'Page\s*\d+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'[-_]{2,}', '', text)
    text = re.sub(r'[ ]{2,}', ' ', text)
    return text.strip()

# ===== Question Generation with Groq + LLaMA3 =====
def generate_quiz_with_groq(cleaned_text):
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    prompt = f"""
You are an AI assistant helping a course creator.

Based on the following course content, generate:
1. A 3-5 bullet point summary.
2. 5 multiple-choice questions (each with 4 options and the correct answer).
3. 3 short answer questions.

Course Content:
\"\"\"
{cleaned_text[:3000]}  # Limit to 3000 chars to avoid overload
\"\"\"
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content

# ===== Main Runner =====
# === Streamlit UI ===
st.set_page_config(page_title="QuizGen AI", layout="wide")
st.title("🧠 QuizGen AI")
st.markdown("""
Welcome to **QuizGen AI** — Upload your course content in PDF format and get:
- 📋 A summary
- ✅ MCQs
- ✍️ Short Answer Questions

Powered by LLaMA3 via Groq (completely free & fast!).
""")

uploaded_file = st.file_uploader("Upload Course PDF", type=["pdf"])

if uploaded_file:
    with st.spinner("📖 Reading and cleaning your PDF..."):
        with open("temp_uploaded.pdf", "wb") as f:
            f.write(uploaded_file.read())
        raw_text = extract_text_from_pdf("temp_uploaded.pdf")
        cleaned_text = clean_pdf_text(raw_text)

    if st.button("🚀 Generate Quiz Content"):
        with st.spinner("🧠 Generating content with AI..."):
            try:
                result = generate_quiz_with_groq(cleaned_text)
                st.success("✅ Quiz Generated!")
                st.text_area("📄 Output", result, height=600)
                st.download_button(
                    "⬇️ Download Quiz",
                    result,
                    file_name="QuizGen_AI_Output.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Error: {e}")

    st.markdown("---")
    st.caption("Developed by Taha | AI meets Education 🎓")
