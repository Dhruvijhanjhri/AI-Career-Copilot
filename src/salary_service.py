def get_salary(role):

    role = role.lower()

    salary_data = {
        "data scientist": "12 LPA",
        "data analyst": "8 LPA",
        "software engineer": "10 LPA",
        "cloud engineer": "14 LPA",
        "machine learning engineer": "15 LPA"
    }

    return salary_data.get(role, "Salary data not available")