import multiprocessing
import time


def count_ascending(name, return_dict=None):
    counter = 0
    for i in range(1, 101):
        counter += 1
        print(f"{name} finished Ascending. Final count:", i)

    if return_dict is not None:
        return_dict[name] = counter


def count_descending(name, return_dict=None):
    counter = 0
    for i in range(100, 0, -1):
        counter += 1
        print(f"{name} finished Descending. Final count:", i)

    if return_dict is not None:
        return_dict[name] = counter


def single_process_count():
    """Count to 10 million in a single process"""
    start_time = time.time()

    count_ascending("Single process")
    count_descending("Single process")

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Single process time: {elapsed:.4f} seconds")
    return elapsed


def multi_process_count():
    """Count to 10 million using two processes"""
    start_time = time.time()

    # Create a manager to share data between processes
    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    # Create two processes
    process1 = multiprocessing.Process(
        target=count_ascending,
        args=("Process 1", return_dict)
    )
    process2 = multiprocessing.Process(
        target=count_descending,
        args=("Process 2", return_dict)
    )

    # Start both threads
    process1.start()
    process2.start()

    # Wait for both threads to complete
    process1.join()
    process2.join()

    end_time = time.time()
    elapsed = end_time - start_time
    print(f"Two processes time: {elapsed:.4f} seconds")

    # Verify results
    total_count = sum(return_dict.values())
    print(f"Total count from multiprocessing: {total_count}")

    print(return_dict)

    return elapsed



if __name__ == "__main__":
    print("Starting test...")
    print("Running single process test...")
    single_time = single_process_count()

    print("\nRunning two processes test...")
    multi_time = multi_process_count()

    print("\nResults comparison:")
    print(f"Single process: {single_time:.4f} seconds")
    print(f"Two processes: {multi_time:.4f} seconds")

    if multi_time < single_time:
        improvement = (single_time - multi_time) / single_time * 100
        print(f"Two processes were faster by {improvement:.2f}%")
    else:
        slowdown = (multi_time - single_time) / single_time * 100
        print(f"Two processes were slower by {slowdown:.2f}%")
