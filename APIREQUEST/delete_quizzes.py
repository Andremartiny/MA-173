import requests

API_KEY = "10742~bKwu47TRaxvDybBOex52yNcghKRWDtT7gNRxjzXIk4iRWH7WhmAUWRuv0Y9M23UT" # Kommentert ut 
CANVAS_DOMAIN = "uia.instructure.com"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

course_id = 9847




############################## DELETE ALL ASSIGNMENTS ######################################
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

def delete_assignment(assignment_id):
    response = requests.delete(
        f"https://{CANVAS_DOMAIN}/api/v1/courses/{course_id}/quizzes/{assignment_id}",
        headers=headers,
    )
    if response.status_code == 200:
        return True
    else:
        print(f"Failed to delete quiz with ID {assignment_id}, status code: {response.status_code}, response: {response.text}")
        return False


#### Kommentert ut i tilfelle scriptet er kjørt ved uhell!
# Fetch all assignments for the course
assignments = get_quizzes()

print(assignments)
# Iterate through the list of assignment names and delete each one
for assignment_ID in assignments:
    assignment_name = assignments[assignment_ID]
    if assignment_ID:
        success = delete_assignment(assignment_name)
        if success:
            print(f"Deleted assignment '{assignment_name}'")
        else:
            print(f"Failed to delete assignment '{assignment_name}'")
    else:
        print(f"Assignment '{assignment_name}' not found")
