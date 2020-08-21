import time

a = time.time()

do_something = ["0" * 1000]
for i in range(10000):
    for j in range(5000):
        do_something.append(do_something)
        do_something.append(do_something)
        do_something.append(do_something)
        do_something.append(do_something)
        do_something.append(do_something)
        do_something.append(do_something)

a = time.time() - a
print(a)  # a is in s

