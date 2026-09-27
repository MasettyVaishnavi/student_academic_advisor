# Knowledge Base
# Contains career rules and required skills

level_value = {
    "Not Known": 0,
    "Weak": 1,
    "Average": 2,
    "Good": 3,
    "Excellent": 4
}

# Rules for Career Recommendation
career_rules = [

    {
        "career": "Software Development",
        "conditions": {
            "DSA": "Good",
            "Programming": "Good",
            "Problem Solving": "Good"
        }
    },

    {
        "career": "Web Development",
        "conditions": {
            "Web Development": "Good",
            "JavaScript": "Good",
            "Programming": "Good"
        }
    },

    {
        "career": "Backend Development",
        "conditions": {
            "Programming": "Good",
            "DBMS": "Good",
            "SQL": "Good",
            "Problem Solving": "Good"
        }
    },

    {
        "career": "AI/ML",
        "conditions": {
            "Python": "Good",
            "Mathematics": "Good",
            "Statistics": "Good"
        }
    },

    {
        "career": "Data Science",
        "conditions": {
            "Python": "Good",
            "Mathematics": "Good",
            "Statistics": "Good"
        }
    },

    {
        "career": "Data Analytics",
        "conditions": {
            "SQL": "Good",
            "Statistics": "Good",
            "Data Analysis": "Good"
        }
    }
]


# Skills required for each area of interest
skill_requirements = {

    "AI/ML": [
        "Python",
        "Mathematics",
        "Statistics",
        "Problem Solving"
    ],

    "Software Development": [
        "DSA",
        "Programming",
        "Problem Solving"
    ],

    "Web Development": [
        "Web Development",
        "JavaScript",
        "Programming"
    ],

    "Backend Development": [
        "Programming",
        "DBMS",
        "SQL",
        "Problem Solving"
    ],

    "Data Science": [
        "Python",
        "Mathematics",
        "Statistics",
        "Problem Solving"
    ],

    "Data Analytics": [
        "SQL",
        "Statistics",
        "DBMS",
        "Data Analysis"
    ]
}