# Todoist to Motion Task Transfer

## Overview

This program allows users to transfer all active tasks from Todoist into Motion's default workspace. The project strictly transfers the name and description of Todoist tasks into Motion.  This is intended as a **one-time transfer** to kickstart your journey with Motion. Users who wish to sync Todoist and Motion in real time can use tools like Zapier after completing this transfer.

### Features

- **Seamless Transfer:** Transfers tasks from Todoist to Motion's default workspace.
- **Progress Tracking:** Includes a progress bar to visualize task transfer status.
- **Error Handling:** Provides detailed messages in case of failures.

### Who Is This For?

This program is perfect for users who:

- Are migrating from Todoist to Motion.
- Want to organize their tasks in Motion.
- Need a one-time tool to jumpstart their workflow.

---

## Prerequisites

1. **Python**: Ensure you have Python 3.7+ installed.

2. **API Keys**:

   - **Todoist API Key**: Get yours from [Todoist Developer API](https://developer.todoist.com/appconsole).
   - **Motion API Key**: Obtain from the Motion platform.

3. **Dependencies**:
   Install required libraries using the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/precious318/Todoist2Motion.git
   cd todoist-to-motion-transfer
   ```

2. **Create a `.env` File**:
   Add your API keys to a `.env` file in the following format:
   ```env
   TODOIST_API_KEY=your_todoist_api_key
   MOTION_API_KEY=your_motion_api_key
   ```

3. **Run the Program**:
   Execute the script to start the transfer:
   ```bash
   python main.py
   ```

4. **Monitor Progress**:
   The program displays a progress bar as tasks are transferred.


3. **Follow Prompts**:
   The script will guide you to input your Todoist and Motion API keys and handle the rest of the setup process.

4. **Monitor Progress**:
   The program displays a progress bar as tasks are transferred.

---

## File Structure

```
Todoist2Motion/
├── main.py             # Main execution script
├── requirements.txt    # Project dependencies
├── .env                # Environment variables (API keys)
├── README.md           # Documentation
```

---

## How It Works

### 1. Fetching Tasks from Todoist

The program uses the `todoist-api-python` library to retrieve all active tasks from Todoist. Each task contains:

- Task name (`content`)
- Description (`description`)
-

### 2. Mapping to Motion Tasks

Each Todoist task is converted into a Motion task. Key fields include:

- **Name:** The Todoist task name.
- **Description:** The Todoist task description.
-

### 3. Transferring to Motion

Using the Motion API, tasks are added to Motion's default workspace. A rate limit of 10 tasks per minute is respected to avoid API restrictions.

### 4. Progress Tracking

A `tqdm` progress bar updates in real time, showing the transfer status.

---

## Customization

### Adjusting the Workspace

To change the target workspace in Motion:

- Modify the `workspaceId` in the `create_motion_task` function.
- Use the `get_motion_workspace_id` function to find other workspace IDs.

### Adding New Features

Feel free to extend the program with additional features, such as:

- Filtering tasks by priority.
- Syncing instead of transferring tasks.

---

## Credits

This project was developed by **Precious O. Akujor** with guidance and support from ChatGPT by OpenAI. Special thanks to the developers of the following libraries:

- [`todoist-api-python`](https://pypi.org/project/todoist-api-python/)
- [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [`tqdm`](https://pypi.org/project/tqdm/)

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Feedback and Contributions

Feel free to fork this repository, suggest improvements, or submit issues on GitHub. Contributions are always welcome!

Users will need to create their own `.env` file to input and edit API keys as needed, allowing for flexibility in configuration.

