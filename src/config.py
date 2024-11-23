import os

# Sports to fetch
JOBS = {
    'job_1': {
        'task': ['task1', 'task2', 'task3'],    # List of tasks to run
        'schedule': 'every_minute'                      # Schedule frequency
    },
    'job_2': {
        'task': ['task1', 'task2', 'task3'],  # List of tasks to run
        'schedule': 'every_other_hour'                     # Schedule frequency
    }
    # Add more sports and configurations as needed
}

# Fetch frequency settings (in minutes)
FETCH_FREQUENCIES = {
    'every_minute': 1,
    'hourly': 60,  # Fetch every hour
    'every_other_hour': 120,
    'daily': 1440, # Fetch every day
}