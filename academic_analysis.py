def analyze_cgpa(cgpa):

    if cgpa >= 8.5:
        return "Excellent"

    elif cgpa >= 7.0:
        return "Good"

    elif cgpa >= 5.0:
        return "Average"

    else:
        return "Weak"


def analyze_subjects(student):

    strong = []
    needs_improvement = []

    for subject, level in student.items():

        if level == "Excellent" or level == "Good":
            strong.append(subject)

        elif level == "Average" or level == "Weak":
            needs_improvement.append(subject)

    return strong, needs_improvement