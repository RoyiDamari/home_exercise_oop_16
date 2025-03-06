import threading
import random

lock = threading.Lock()


def print_various_things(thread_name):
    print(f"\n----- Thread {thread_name} starting -----\n")

    # 1. Numbers 1-100
    print(f"Thread {thread_name} printing numbers 1-100:")
    for i in range(1, 101, 10):  # Print in groups of 10 to save space
        print(f"{i}-{i + 9}", end=" ")
    print("\n")

    # 2. Random inspirational quotes
    quotes = [
        "The only way to do great work is to love what you do.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Believe you can and you're halfway there.",
        "Don't watch the clock; do what it does. Keep going.",
        "The best way to predict the future is to create it."
    ]
    print(f"Thread {thread_name} sharing an inspirational quote:")
    print(f'"{random.choice(quotes)}"\n')

    # 3. Interesting facts about space
    space_facts = [
        "One million Earths could fit inside the Sun.",
        "A year on Venus is shorter than a day on Venus.",
        "There are more stars in the universe than grains of sand on Earth.",
        "A neutron star is so dense that a teaspoon would weigh 6 billion tons.",
        "The footprints on the Moon will stay there for at least 100 million years."
    ]
    print(f"Thread {thread_name} sharing a space fact:")
    print(f"{random.choice(space_facts)}\n")

    # 4. List of capital cities
    capitals = [
        "Tokyo, Japan", "New Delhi, India", "Beijing, China",
        "Washington D.C., USA", "Brasília, Brazil", "Moscow, Russia",
        "London, UK", "Paris, France", "Berlin, Germany", "Rome, Italy"
    ]
    print(f"Thread {thread_name} listing some capital cities:")

    with lock:
        for city in capitals[:5]:  # Just show 5 capitals
            print(f"- {city}")
        print("")

    # 5. Programming language creation years
    languages = [
        "Python (1991)", "JavaScript (1995)", "Java (1995)",
        "C# (2000)", "Ruby (1995)", "Go (2009)",
        "Swift (2014)", "Kotlin (2011)", "TypeScript (2012)"
    ]
    print(f"Thread {thread_name} sharing programming language creation years:")
    for lang in random.sample(languages, 5):  # Random 5 languages
        print(f"- {lang}")

    print(f"\n----- Thread {thread_name} finished -----\n")


# Create two threads
thread1 = threading.Thread(target=print_various_things, args=("A",))
thread2 = threading.Thread(target=print_various_things, args=("B",))

# Start both threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have completed execution.")
