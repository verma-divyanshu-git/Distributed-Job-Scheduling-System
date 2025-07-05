import requests
import time
import threading

BASE_URL = 'http://localhost:8080/jobs'
SIMPLE_JOBS_COUNT = 20
LONG_RUNNING_JOBS_COUNT = 10

def enqueue_simple_job(job_num):
    """Sends a single request to enqueue a simple job."""
    try:
        url = f'{BASE_URL}/simple-job'
        params = {'name': f'LoadTestSimple-{job_num}'}
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            print(f"Successfully enqueued simple job {job_num}: {response.text}")
        else:
            print(f"Error enqueuing simple job {job_num}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect for simple job {job_num}: {e}")

def enqueue_long_running_job(job_num):
    """Sends a single request to enqueue a long-running job."""
    try:
        url = f'{BASE_URL}/long-running-job'
        params = {'name': f'LoadTestLong-{job_num}'}
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            print(f"Successfully enqueued long-running job {job_num}: {response.text}")
        else:
            print(f"Error enqueuing long-running job {job_num}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect for long-running job {job_num}: {e}")

def run_load_test():
    """Runs the full load test using threads to send requests concurrently."""
    threads = []
    print(f"--- Starting Load Test: Enqueuing {SIMPLE_JOBS_COUNT} simple jobs and {LONG_RUNNING_JOBS_COUNT} long-running jobs ---")

    # Create threads for simple jobs
    for i in range(SIMPLE_JOBS_COUNT):
        thread = threading.Thread(target=enqueue_simple_job, args=(i,))
        threads.append(thread)
        thread.start()
        time.sleep(0.05) # Stagger the start slightly

    # Create threads for long-running jobs
    for i in range(LONG_RUNNING_JOBS_COUNT):
        thread = threading.Thread(target=enqueue_long_running_job, args=(i,))
        threads.append(thread)
        thread.start()
        time.sleep(0.05) # Stagger the start slightly

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print("--- Load Test Finished ---")

if __name__ == "__main__":
    # Ensure your Docker containers are running before executing this script
    print("Make sure your docker-compose stack is up and running...")
    time.sleep(1) # Brief pause for user to read message
    run_load_test()
