\# 🎓 Smart Student Academic Advisor



A beginner-friendly rule-based AI system that analyzes a student's academic performance and skill levels to provide career and skill recommendations.



\## 📌 Project Overview



The Smart Student Academic Advisor helps students understand their academic strengths, areas that need improvement, suitable career paths, and skills they should develop.



The system uses a Knowledge Base and rule-based inference instead of Machine Learning or Deep Learning.



\## 🎯 Objectives



\- Analyze the student's CGPA and academic performance.

\- Identify strong and weak skill areas.

\- Recommend suitable career domains.

\- Identify skills already satisfied by the student.

\- Suggest skills that need improvement.

\- Identify missing skills.

\- Provide personalized academic suggestions.



\## 🧠 AI Concepts Used



\### Knowledge Base



The system stores career rules and required skills in a knowledge base.



\### Forward Chaining



Forward chaining is used for career recommendation.



The system starts with the student's known skill levels and checks the career rules to determine which careers match.



\### Backward Chaining



Backward chaining is used for skill recommendation.



The system starts with the selected career or area of interest and works backward to identify the required skills.



The skills are classified as:



\- Satisfied

\- Needs Improvement

\- Missing



\## 💼 Career Domains



The system currently provides recommendations for:



\- Software Development

\- Web Development

\- Backend Development

\- AI/ML

\- Data Science

\- Data Analytics



\## 🛠️ Technologies Used



\- Python

\- Streamlit

\- Rule-Based AI

\- Knowledge-Based System



\## 📂 Project Structure



```text

student\_academic\_advisor/

│

├── app.py

├── knowledge\_base.py

├── forward\_chaining.py

├── backward\_chaining.py

├── academic\_analysis.py

├── requirements.txt

├── README.md

└── .gitignore

