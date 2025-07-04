# 📄 Resume Scanner (Keyword-Based) — PDFMiner Version

This project scans actual resume PDFs and compares their content against a job description using keyword matching. It's built using basic Python and PDFMiner for text extraction, making it lightweight and beginner-friendly.

---

## 🚀 Project Objective

Hiring managers often review dozens or even hundreds of resumes manually. This resume scanner helps automate that process by reading resume files, extracting plain text, and scoring how closely each resume matches the required job description based on keyword overlap.

It’s ideal for small-scale resume filtering, educational demos, or quick match prototypes where keyword presence is a strong indicator of relevance.

---


---

## 🧠 How It Works

### 🔹 Step 1: Text Extraction
Resume PDFs are processed using [`pdfminer.six`](https://pypi.org/project/pdfminer.six/) to extract clean, searchable text from their contents.

### 🔹 Step 2: Keyword Processing
The job description is tokenized into a keyword set (e.g., `"Python"`, `"machine learning"`, `"SQL"`). These are compared against words found in each resume.

### 🔹 Step 3: Match Scoring
Each resume receives a score based on how many job-related keywords it contains.

### 🔹 Step 4: Detailed Summary
For each resume, the following are printed:
- Total match score (based on keyword overlap)
- Strength indicator (Excellent / Good / Low)
- Matched skills (which keywords were found)
- Missing skills (which keywords were not found)

--
## Results :
![abhishek pro 3](https://github.com/user-attachments/assets/01044590-716f-4192-a3ae-1763ff943b38)


## 🔧 Setup Instructions

### 1. 📦 Install Dependencies

First, create and activate your virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
Then install the required packages:

bash
pip install -r requirements.txt


##
