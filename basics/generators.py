# Generators => lazy evalution, you don't want the result immidiately, save memory 
# yield keyword is used in generators

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) # gives error


# infinite generator => no memory saving
def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))


# send data to generator
def chai_customer():
    print("Welcome ! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala Chai")
stall.send("Lemon Chai")


# yield from and close generator
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai")


stall = chai_stall()
print(next(stall))
stall.close() #cleanup

# test
"""
    Infinite generator that simulates a token dispenser.
    
    - Yields incrementing token numbers starting from `start`.
    - Accepts input via `send()` to optionally reset the counter to a new value.
    - Gracefully stops if `close()` is called.
"""
def token_dispenser(start=1):
    current = start
    try:
        while True:
            # Yield current token and receive any value sent via .send()
            received = yield current
            if received is not None:
                current = received
            else:
                current += 1
    except GeneratorExit:
        print("Dispenser closed.")

stall = token_dispenser()
print(next(stall))
print(next(stall))
print(next(stall))
stall.send(20)
print(next(stall))
print(next(stall))
print(next(stall))
print(next(stall))
print(next(stall))