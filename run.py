import argparse
import json

from src.sales_pipeline.pipeline import run_pipeline
from src.sales_pipeline.scheduler import start_scheduler


def main() -> None:
    p = argparse.ArgumentParser(description="Sales Automation Pipeline")
    p.add_argument("--config", default="config.yaml")
    p.add_argument("--once", action="store_true", help="Run once and exit")
    p.add_argument("--schedule", action="store_true", help="Run on schedule")
    args = p.parse_args()

    if args.schedule:
        start_scheduler(args.config)
    else:
        result = run_pipeline(args.config)
        print(json.dumps(result, indent=2, default=str))


if __name__ == "__main__":
    main()
    