from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from .config import load_config
from .pipeline import run_pipeline
from .logger import get_logger


def start_scheduler(cfg_path: str = "config.yaml") -> None:
    cfg = load_config(cfg_path)
    log = get_logger(log_dir=cfg["paths"]["logs"])

    sched = BlockingScheduler()
    cron = cfg["schedule"]["cron"]

    sched.add_job(
        lambda: run_pipeline(cfg_path),
        CronTrigger.from_crontab(cron),
        name="sales_pipeline",
    )

    log.info("Scheduler started with cron=%s. Press Ctrl+C to stop.", cron)

    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        log.info("Scheduler stopped.")