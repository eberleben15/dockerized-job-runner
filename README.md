# dockerized-job-runner
A generic, dockerized Python application designed to run configurable jobs on a schedule, leveraging a scheduler and a flexible configuration system for any type of Python task. Jobs and their schedules are configured in the `config.py` file, and the application is designed to be run in a Docker container.

## Configuration

To configure jobs, edit the `config.py` file. The file contains two main components:

### 1. **JOBS**

Defines the jobs to be run and their associated tasks and schedule. 

Example:
```python
JOBS = {
    'job_1': {
        'task': ['task1', 'task2', 'task3'],  # List of tasks to run
        'schedule': 'every_minute'           # Schedule frequency
    },
    'job_2': {
        'task': ['task1', 'task2', 'task3'],  
        'schedule': 'every_other_hour'       
    }
}
```

- **`task`**: A list of tasks the job will execute.
- **`schedule`**: Defines how often the job should run. The schedule must match one of the keys in `FETCH_FREQUENCIES`.

### 2. **FETCH_FREQUENCIES**

Maps schedule keys to time intervals (in minutes).

Example:
```python
FETCH_FREQUENCIES = {
    'every_minute': 1,
    'hourly': 60,
    'every_other_hour': 120,
    'daily': 1440,
}
```

You can add or modify schedule keys and their associated intervals as needed.

---

## Build and Run the Docker Container

### Step 1: Build the Docker Image

Run the following command to build the Docker image:
```bash
docker build -t python-scheduler .
```

### Step 2: Run the Docker Container

Run the container with the following command:
```bash
docker run -d --name python-scheduler python-scheduler
```

- The `-d` flag runs the container in detached mode.
- Replace `python-scheduler` with your preferred container name.

---

## Example Workflow

1. Configure jobs in `config.py`.
2. Build the Docker image:  
   ```bash
   docker build -t python-scheduler .
   ```
3. Run the Docker container:  
   ```bash
   docker run -d --name python-scheduler python-scheduler
   ```
4. Check logs to confirm the scheduler is running jobs:  
   ```bash
   docker logs -f python-scheduler
   ```

---

## Extending the Scheduler

- Add new jobs to `JOBS` with appropriate tasks and schedule keys.
- Define new schedule intervals in `FETCH_FREQUENCIES` as needed.

Feel free to fork and customize this repository for your use case. Happy scheduling! 🎉