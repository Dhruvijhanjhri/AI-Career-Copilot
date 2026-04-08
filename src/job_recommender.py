def recommend_job(skills):

    skills = skills.lower()

    if "python" in skills and "machine learning" in skills:
        return "Data Scientist"

    elif "sql" in skills and "excel" in skills:
        return "Data Analyst"

    elif "java" in skills:
        return "Software Engineer"

    elif "cloud" in skills:
        return "Cloud Engineer"

    else:
        return "General IT Role"