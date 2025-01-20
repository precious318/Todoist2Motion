import requests
import os  # used to load api keys from .env file
from dotenv import load_dotenv  # used to load api keys from .env file
from todoist_api_python.api import TodoistAPI  # used in importing todoist tasks in fetch_todoist_tasks function
import json  # used in mapping todoist tasks into motion in create_motion_task function
import http.client  # used for api request in create_motion_task function
import time  # used in delaying
from tqdm import tqdm  # used for progress bar

# Load API keys from .env
load_dotenv()
TODOIST_API_KEY = os.getenv("TODOIST_API_KEY")
MOTION_API_KEY = os.getenv("MOTION_API_KEY")

# Todoist API URL
TODOIST_TASKS_URL = "https://api.todoist.com/rest/v1/tasks"

# Motion API URL
MOTION_TASKS_URL = "https://api.usemotion.com/v1/tasks"


# Fetch tasks from Todoist
def fetch_todoist_tasks() -> list:
    """
    Fetches Todoist tasks from Todoist API.
    :return: List of Todoist tasks.
    :rtype: List of Object Task (see more here: https://developer.todoist.com/rest/v2/#tasks)
    """
    api = TodoistAPI(TODOIST_API_KEY)
    try:
        tasks = api.get_tasks()
        return tasks
    except Exception as error:
        print(f"Error fetching Todoist tasks: {error}")
        return []


# Create task in Motion
def create_motion_task(task):
    """
    Creates a motion task.
    :param task: Todoist task.
    :type task: Task Object (see more here: https://developer.todoist.com/rest/v2/#tasks)
    :return: Nothing
    :rtype: None
    """
    # Basic mapping from Todoist task to Motion task
    payload = json.dumps({
        "name": task.content,
        'description': task.description,
        "workspaceId": get_motion_workspace_id()
    }).encode('utf-8')

    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'X-API-Key': MOTION_API_KEY
    }
    try:
        conn = http.client.HTTPSConnection("api.usemotion.com")  # sets up api connection
        conn.request("POST", "/v1/tasks", payload, headers)
        response = conn.getresponse()
        if response.status != 201:  # Motion API success response
            print(f"Failed to create task: {task.content} - {response.status}")
        time.sleep(6)  # Respect Motion's rate limit
    except Exception as e:
        print(f"Error creating task: {task.content} - {e}")


def get_motion_workspace_id():
    """
    Gets Motion's "My Tasks (Private)" workspace id.
    :return: "My Tasks (Private)" workspace id
    :rtype: str
    """

    headers = {
        'Accept': "application/json",
        'X-API-Key': MOTION_API_KEY
    }
    try:
        conn = http.client.HTTPSConnection("api.usemotion.com")
        conn.request("GET", "/v1/workspaces", headers=headers)

        res = conn.getresponse()
        data = res.read()
        workspace_json = json.loads(data.decode("utf-8"))

        for workspace in workspace_json["workspaces"]:
            if workspace["name"] == "My Tasks (Private)":
                return workspace["id"]
    except Exception as e:
        print(f"Error obtaining 'My Tasks (Private)' workspace id: {e}")


# Main function to handle the transfer
def main():
    """
    Main function. This function will take all active Todoist tasks and transfer Name and Description to Motion's "My Tasks (Private)" workspace.
    :return: Nothing
    :rtype: None
    """
    todoist_tasks = fetch_todoist_tasks()
    if not todoist_tasks:
        print("No tasks found or error occurred!")
        return

    print(f"Starting transfer of {len(todoist_tasks)} tasks...")

    for task in tqdm(todoist_tasks, desc="Transferring tasks", unit="task"):
        create_motion_task(task)

    print("Task transfer complete!")


if __name__ == "__main__":
    main()
