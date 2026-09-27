def backward_chaining(goal, student, skill_requirements):

    required_skills = skill_requirements[goal]

    satisfied_skills = []
    skills_to_improve = []
    missing_skills = []

    for skill in required_skills:

        if skill not in student:
            missing_skills.append(skill)

        elif student[skill] == "Excellent" or student[skill] == "Good":
            satisfied_skills.append(skill)

        elif student[skill] == "Average" or student[skill] == "Weak":
            skills_to_improve.append(skill)

        elif student[skill] == "Not Known":
            missing_skills.append(skill)

    return satisfied_skills, skills_to_improve, missing_skills