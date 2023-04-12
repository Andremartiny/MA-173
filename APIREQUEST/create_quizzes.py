import requests
import openpyxl

workbook = openpyxl.load_workbook("C:\\Users\\andrem\\OneDrive - Universitetet i Agder\\Undervisning\\MA-173\\Ukeplan med oppgaver og vedlegg\\Datamateriale\\Kandidat1Mal.xlsx")

# Replace with your own access token and Canvas domain
API_KEY = "10742~BVyt0MYvbYdR4dzoGLNXZriL7wfmwKmYwzj1jyVFwd19i585uILGA4sVmsIJ9hrX"
CANVAS_DOMAIN = "uia.instructure.com"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# Replace with your desired course ID
# course_id = 9847
course_id = 12547 # MA-173-ID: 12547



def get_assignments():
    response = requests.get(
        f"https://{CANVAS_DOMAIN}/api/v1/courses/{course_id}/assignments?per_page=100",
        headers=headers,
    )
    return {assignment["name"]: assignment["id"] for assignment in response.json()}

def get_quizzes():
    response = requests.get(f"https://{CANVAS_DOMAIN}/api/v1/courses/{course_id}/quizzes?per_page=100",
        headers=headers,
    )
    
    return {quizzes["title"]: quizzes["id"] for quizzes in response.json()}

def create_assignment(name, group_id=None):
    assignment_data = {
        "quiz": {
            "title": name,
            "submission_types": "none",
            "allowed_extensions": ["docx", "pdf", "jpeg", "jpg", "png"],
            "points_possible": 3,
            "grading_type": "points",
            "lock_at": None,
            "allowed_attempts": -1,
            "quiz_type": "assignment",
            "scoring_policy": "keep_highest",
            "published": True,
        }
    }

    if group_id:
        assignment_data["quiz"]["assignment_group_id"] = group_id

    response = requests.post(
        f"https://{CANVAS_DOMAIN}/api/v1/courses/{course_id}/quizzes",
        json=assignment_data,
        headers=headers,
    )
    return response.json()

def get_assignment_groups():
    url = f"https://{CANVAS_DOMAIN}/api/v1/courses/{course_id}/assignment_groups"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def create_quiz_question(quiz_id, question_name, max_score=3, allowed_file_types=None):
    if allowed_file_types is None:
        allowed_file_types = ["pdf", "docx", "jpeg", "jpg"]

    url = f"https://{CANVAS_DOMAIN}/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions"
    payload = {
        "question": {
            "question_text": question_name,
            "question_type": "file_upload_question",
            "points_possible": max_score,
            "file_upload_config": {
                "allowed_extensions": allowed_file_types,
            },
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.content}")
    return response.json()

tema_læringsmål_dict = {}

for row in workbook["Datamateriale"].iter_rows(min_row=2, values_only=True):
    if row[0] == None or row[0] == "Didaktikk":
        continue
    if row[0] not in tema_læringsmål_dict:
        tema_læringsmål_dict[row[0]] = []
    tema_læringsmål_dict[row[0]].append(row[6])


for tema in tema_læringsmål_dict:
    new_quiz = create_assignment(tema)
    quiz_id = new_quiz["id"]
    for quiz_name in tema_læringsmål_dict[tema]:
        create_quiz_question(quiz_id, quiz_name)
    