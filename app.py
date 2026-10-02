import streamlit as st
from knowledge_base import career_rules, skill_requirements, level_value
from forward_chaining import forward_chaining
from backward_chaining import backward_chaining
from academic_analysis import analyze_cgpa, analyze_subjects

#gives suggestions for sujects if the student is weak or average
suggestions = {
    "DSA": "Practice basic data structures and algorithms regularly.",
    "Programming": "Practice coding problems to improve programming skills.",
    "DBMS": "Revise database concepts and practice SQL queries.",
    "SQL": "Practice SQL queries and database operations.",
    "Mathematics": "Practice important mathematical concepts and problems.",
    "Statistics": "Practice basic statistical concepts and problem solving.",
    "Python": "Practice Python programming and solve beginner-level problems.",
    "Web Development": "Practice HTML, CSS and basic web development concepts.",
    "JavaScript": "Practice JavaScript fundamentals and small programs.",
    "Data Analysis": "Practice data analysis concepts and working with datasets.",
    "Problem Solving": "Solve coding and logical problems regularly."
}

st.title("🎓 Smart Student Academic Advisor")
st.write(
    "Enter your academic details and skill levels to receive "
    "academic insights, skill recommendations, and career suggestions."
)

# takes input cgpa
cgpa = st.number_input(
    "Enter your CGPA",
    min_value=0.0,
    max_value=10.0,
    value=0.0,
    step=0.1
)
# takes input career goal
goal = st.selectbox(
    "Select your Area of Interest",
    [
        "AI/ML",
        "Software Development",
        "Web Development",
        "Backend Development",
        "Data Science",
        "Data Analytics"
    ]
)

# takes input of student skill level in each subject
st.subheader("Skill Levels")
skill_names = [
    "DSA",
    "Programming",
    "DBMS",
    "SQL",
    "Python",
    "Mathematics",
    "Statistics",
    "Web Development",
    "JavaScript",
    "Data Analysis",
    "Problem Solving"
]

student = {}
col1, col2 = st.columns(2)
for i, skill in enumerate(skill_names):
    if i % 2 == 0:
        with col1:
            student[skill] = st.selectbox(
                skill,
                ["Not Known", "Excellent", "Good", "Average", "Weak"]
            )
    else:
        with col2:
            student[skill] = st.selectbox(
                skill,
                ["Not Known", "Excellent", "Good", "Average", "Weak"]
            )


if st.button("🔍 Analyze My Profile"):
    performance = analyze_cgpa(cgpa)
    strong, needs_improvement = analyze_subjects(student)
    st.subheader("📊 Academic Performance")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("CGPA", cgpa)
    with col2:
        st.metric("Overall Performance", performance)

    st.write("Strong Areas:") # gives student strong subjects
    for subject in strong:
        st.write("•", subject)

    st.write("Areas Needing Improvement:") # gives subjects where student need to improve
    for subject in needs_improvement:
        st.write("•", subject)

    st.subheader("💡 Improvement Suggestions") # gives suggestions
    if needs_improvement:
        for subject in needs_improvement:
            st.write("•", suggestions[subject])
    else:
        st.write("Your current skill levels are good. Keep practicing to maintain them.")


    #career recomendation based on student skill level
    recommendations = forward_chaining(student, career_rules, level_value)
    st.subheader("🎯 Career Recommendations")
    st.write("Based on your current skill levels:")
    if recommendations:
        career_reasons = {}
        for rule in recommendations:
            career = rule["career"]
            if career not in career_reasons:
                career_reasons[career] = []
            for subject, required_level in rule["conditions"].items():
                reason = subject + ": " + student[subject]
                if reason not in career_reasons[career]:
                    career_reasons[career].append(reason)

        for career, reasons in career_reasons.items():
            st.success("🎯 " + career)
            st.write("Why this recommendation?")
            for reason in reasons:
                st.write("•", reason)
    else:
        st.write("No direct career recommendation based on the current skill levels.")


    #skill recommendation based on selected area on interest
    st.subheader("🔄 Skill Recommendation")
    st.write("Based on your selected area of interest:")

    satisfied, skills_to_improve, missing = backward_chaining(
        goal, student, skill_requirements
    )

    st.info("🎯 Area of Interest: " + goal) # displays student selected area on interest

    st.write("Required Skills:")
    for skill in skill_requirements[goal]:
        st.write("•", skill)

    st.write("Skills Already Satisfied:")
    if satisfied:
        for skill in satisfied:
            st.success("✅ " + skill)
    else:
        st.info("No required skills are currently satisfied.")
    
    st.write("Skills to Improve:")
    if skills_to_improve:
        for skill in skills_to_improve:
            st.warning("⚠️ " + skill)
    else:
        st.success("✅ No skills currently need improvement.")

    st.write("Missing Skills:")
    if missing:
        for skill in missing:
            st.error("❌ " + skill)
    else:
        st.success("✅ No required skills are missing.")