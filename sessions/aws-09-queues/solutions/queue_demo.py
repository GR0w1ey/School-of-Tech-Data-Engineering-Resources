# Define the queue as an empty list
# Global queue var is an anti-pattern, only for queue demo purposes
queue = []


def produce(message):
    queue.append(message)
    print(f"Produced message: {message}")


def consume():
    if queue:
        message = queue.pop(0)
        print(f"Consumed message: {message}")
        return message
    else:
        print("No message to consume.")


# Messages are often json, but equally can be text or xml
produce("Sold a coffee")
produce("Sold a latte")
print("...")
consume()  # "Sold a coffee"
consume()  # "Sold a latte"
consume()  # "No message to consume."
