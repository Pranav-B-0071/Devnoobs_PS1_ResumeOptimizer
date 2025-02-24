import datetime

def generate_learning_roadmap(missing_skills, prep_time_weeks):
    roadmap = {}
    weeks = list(range(1, prep_time_weeks + 1))
    
    if not missing_skills:
        return {"Week 1": ["No missing skills. You're ready!"]}

    # Assign skills to each week in a balanced way
    for i, skill in enumerate(missing_skills):
        week_num = weeks[i % len(weeks)]  # Distribute evenly across weeks
        if f"Week {week_num}" not in roadmap:
            roadmap[f"Week {week_num}"] = []
        roadmap[f"Week {week_num}"].append(f"Learn {skill}")

    return roadmap



if __name__ == "__main__":
    # Example usage
    missing_skills = ["Machine Learning", "Python", "SQL"]
    prep_days = 30
    print("Learning Roadmap:", generate_learning_roadmap(missing_skills, prep_days))
