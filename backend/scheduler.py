def generate_timetable(data):
    subjects = data["subjects"]
    total_hours = data["available_hours"]

    timetable = {}
    total_weight = sum(s["weight"] for s in subjects)

    for subject in subjects:
        hours = (subject["weight"] / total_weight) * total_hours
        timetable[subject["name"]] = round(hours, 2)

    return timetable
