import json
import os

DATA_PATH = "data/students.json"
COURSES_PATH = "data/courses.json"

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def view_schedule(student_id):
    if not os.path.exists(DATA_PATH) or not os.path.exists(COURSES_PATH):
        print("Error: data files not found.")
        return

    students = load_json(DATA_PATH)
    courses = load_json(COURSES_PATH)

    student = next((s for s in students if s["id"] == student_id), None)
    if student is None:
        print(f"Student ID '{student_id}' not found.")
        return

    enrolled_codes = student.get("enrolledCourses", [])
    enrolled_courses = [c for c in courses if c["code"] in enrolled_codes]

    print("=" * 70)
    print(f"  SCHEDULE FOR: {student['name']} [{student['id']}]")
    print("=" * 70)

    if not enrolled_courses:
        print("  You are not enrolled in any courses.")
        return

    print(f"  {'Code':<10} {'Title':<35} {'Credits':<8} {'Time'}")
    print("  " + "-" * 68)

    total_credits = 0
    for course in enrolled_courses:
        slot = course.get("timeSlot", {})
        time_str = f"{slot.get('days','')} {slot.get('startTime','')}–{slot.get('endTime','')}"
        print(f"  {course['code']:<10} {course['title']:<35} {course['credits']:<8} {time_str}")
        total_credits += course["credits"]

    print("  " + "-" * 68)
    print(f"  Total Credits Enrolled: {total_credits}")
    print("=" * 70)

def main():
    student_id = input("Enter your Student ID: ").strip()
    view_schedule(student_id)

if __name__ == "__main__":
    main()