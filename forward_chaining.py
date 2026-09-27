def forward_chaining(student, career_rules, level_value):

    recommendations = []

    for rule in career_rules:

        conditions_match = True

        for subject, required_level in rule["conditions"].items():

            student_level = student.get(subject)

            if level_value[student_level] < level_value[required_level]:
                conditions_match = False
                break

        if conditions_match:
            recommendations.append(rule)

    return recommendations