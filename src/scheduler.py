# scheduler.py
import schedule
import time
from config import JOBS, FETCH_FREQUENCIES
from logger import logger

class Scheduler:
    def __init__(self):
        self.scheduler = schedule.Scheduler()

    def job(self, job):
        logger.info(f"Hello From {job}!")

    def setup_schedule(self):
            for job, config in JOBS.items():
                frequency = FETCH_FREQUENCIES.get(config['schedule'])
                if frequency:
                    # Schedule the job
                    self.scheduler.every(frequency).minutes.do(self.job, job=job)
                    logger.info(f"Scheduled job for {job} every {frequency} minutes.")

                    # Run the job immediately
                    logger.info(f"Running {job} immediately...")
                    self.job(job)
                else:
                    logger.error(f"Frequency configuration for {job} is missing or incorrect.")

    def run(self):
        logger.info("Scheduler started. Waiting for the next scheduled job...")
        while True:
            self.scheduler.run_pending()
            time.sleep(1)