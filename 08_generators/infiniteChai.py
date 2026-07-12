def infiniteChaiRefill():
    count = 1
    while True:
        yield f"Refill: #{count}"
        count += 1

refill = infiniteChaiRefill()
user2 = infiniteChaiRefill()

for _ in range(3):
    print(next(refill))

for _ in range(6):
    print(next(user2))