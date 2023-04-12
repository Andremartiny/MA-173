import requests

# Replace these with your own values
canvas_base_url = "https://uia.instructure.com"
access_token = "10742~BVyt0MYvbYdR4dzoGLNXZriL7wfmwKmYwzj1jyVFwd19i585uILGA4sVmsIJ9hrX"
course_id = 12547
quiz_id = 11000

# Set up headers with the API access token
headers = {"Authorization": f"Bearer {access_token}"}


# Get the quiz submissions
quiz_submissions_url = f"{canvas_base_url}/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions"
quiz_submissions_response = requests.get(quiz_submissions_url, headers=headers, params={"per_page": 100})
quiz_submissions = quiz_submissions_response.json()["quiz_submissions"]

# Collect all question submissions
all_question_submissions = []

for quiz_submission in quiz_submissions:
    submission_id = quiz_submission["id"]
    user_id = quiz_submission["user_id"]

    # Get the quiz submission details
    submission_details_url = f"{canvas_base_url}/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{submission_id}"
    submission_details_response = requests.get(submission_details_url, headers=headers)
    submission_details = submission_details_response.json()["quiz_submission"]

    # Extract question submissions from submission details
    question_submissions = submission_details.get("submission_data", [])

    for question_submission in question_submissions:
        question_submission["user_id"] = user_id
        all_question_submissions.append(question_submission)

print(all_question_submissions)