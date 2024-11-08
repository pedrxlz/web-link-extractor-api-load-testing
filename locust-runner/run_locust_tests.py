import os
import subprocess

locust_file = os.getenv("LOCUST_FILE", "/mnt/locust/locustfile.py")
locust_host = os.getenv("LOCUST_HOST", "http://web:80")
run_time = os.getenv("RUN_TIME", "1m") 
api_service = os.getenv("API_SERVICE", "unknown-api")
use_cache = os.getenv("USE_CACHE", "false").lower() == "true"

user_amounts = [1, 50, 100]

cache_status = "cache" if use_cache else "no-cache"
base_results_dir = f"/mnt/locust/results/{api_service}/{cache_status}"
os.makedirs(base_results_dir, exist_ok=True)

def run_test(user_amount):
    results_dir = os.path.join(base_results_dir, str(user_amount))
    os.makedirs(results_dir, exist_ok=True)

    command = [
        "locust",
        "-f", locust_file,
        "--host", locust_host,
        "--users", str(user_amount),
        "--spawn-rate", str(user_amount),
        "--run-time", run_time,
        "--headless",
        "--csv", os.path.join(results_dir, "locust_results")
    ]

    subprocess.run(command)

for user_amount in user_amounts:
    run_test(user_amount)