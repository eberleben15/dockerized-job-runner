# main.py
from scheduler import Scheduler

if __name__ == "__main__":
    scheduler = Scheduler()
    scheduler.setup_schedule()
    scheduler.run()