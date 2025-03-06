import threading
import time


def count_ascending(name):
    for i in range(1, 101):
        print(f"{name} finished Ascending. Final count:", i)


def count_descending(name):
    for i in range(100, 0, -1):
        print(f"{name} finished Descending. Final count:", i)


def single_thread_count():
    """Count to 10 million in a single thread"""
    start_time = time.time()

    count_ascending("Single thread")
    count_descending("Single thread")

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Single thread time: {elapsed:.4f} seconds")
    return elapsed


def multi_thread_count():
    """Count to 10 million using two threads"""
    start_time = time.time()

    # Create two threads
    thread1 = threading.Thread(target=count_ascending, args=("Thread 1",))
    thread2 = threading.Thread(target=count_descending, args=("Thread 2",))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Two threads time: {elapsed:.4f} seconds")
    return elapsed


if __name__ == "__main__":
    print("Starting test...")
    print("Running single thread test...")
    single_time = single_thread_count()

    print("\nRunning two threads test...")
    multi_time = multi_thread_count()

    print("\nResults comparison:")
    print(f"Single thread: {single_time:.4f} seconds")
    print(f"Two threads: {multi_time:.4f} seconds")

    if multi_time < single_time:
        improvement = (single_time - multi_time) / single_time * 100
        print(f"Two threads were faster by {improvement:.2f}%")
    else:
        slowdown = (multi_time - single_time) / single_time * 100
        print(f"Two threads were slower by {slowdown:.2f}%")
