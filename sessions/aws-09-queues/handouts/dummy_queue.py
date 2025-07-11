orders_queue = []

def produce(new_order):
  orders_queue.append(new_order)

def consume():
  next_order = orders_queue.pop()
  print(f'Order ready! {next_order}')

produce("Coffee for Mark")
produce("Sprite for Rodihat")

print(f'Orders queue = {orders_queue}')

consume()
consume()
