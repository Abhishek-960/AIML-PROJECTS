import os
import re
from pdfminer.high_level import extract_text

# Job Description
job_desc = "Looking for a data scientist skilled in Python, machine learning, SQL and data analysis."
job_keywords = set(re.findall(r'\w+', job_desc.lower()))

# Function to read PDF text
def read_pdf(file_path):
    try:
        return extract_text(file_path).lower()
    except:
        return ""

# Folder where resumes are stored
resume_folder = r"E:\project\AIML project showcase\Resume Scanner using Keyword\sample resumes"
scores = []

# Loop through PDF resumes
for file in os.listdir(resume_folder):
    if file.endswith(".pdf"):
        path = os.path.join(resume_folder, file)
        text = read_pdf(path)
        resume_words = set(re.findall(r'\w+', text))
        matched_keywords = job_keywords.intersection(resume_words)
        missing_keywords = job_keywords - resume_words
        score = len(matched_keywords)

        # Strength Indicator
        if score >= 8:
            strength = " Excellent match"
        elif score >= 5:
            strength = " Good match"
        else:
            strength = " Low match"

        scores.append({
            "name": file,
            "score": score,
            "matched": matched_keywords,
            "missing": missing_keywords,
            "strength": strength
        })

# results
print(" Resume Match Results:\n")

for result in sorted(scores, key=lambda x: x["score"], reverse=True):
    print(f" Resume: {result['name']}")
    print(f" Match Score: {result['score']}")
    print(f" Strength Level: {result['strength']}")
    print(f" Matched Skills: {', '.join(sorted(result['matched'])) if result['matched'] else 'None'}")
    print(f" Missing Skills: {', '.join(sorted(result['missing'])) if result['missing'] else 'None'}")
    print("-" * 50)
