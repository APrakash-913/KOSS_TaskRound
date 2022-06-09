import time

start = time.time()
def foo():
    time.sleep(12) 
    # Assume Server take 12 secs to respond
    return "ap\n"

def foo1():
    time.sleep(6) 
    # Assume Our computation takes 6 secs.
    # Independent of foo().
    return "ap1\n"

print(foo())
print(foo1())
print("Done :)")

end = time.time()
print(f"Time Taken = {end - start}")