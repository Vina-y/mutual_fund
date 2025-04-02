import asyncio
from apscheduler.schedulers.background import BackgroundScheduler
import time
from app.cron_job.task.nav_update_task import update_nav_hourly

scheduler = BackgroundScheduler()

def scheduled_task():
    asyncio.run(update_nav_hourly())
    print(f"Running scheduled task at {time.strftime('%Y-%m-%d %H:%M:%S')}")

# start the scheduler
def start_scheduler():
    scheduler.add_job(scheduled_task, "interval",hours=1)  # Runs every 1 hour
    # scheduler.add_job(scheduled_task, "interval",seconds=60)  # Runs every 60 sec
    scheduler.start()
    print("Cron has started!")

# stop the scheduler
def stop_scheduler():
    scheduler.shutdown()
    print("Cron has stopped!")