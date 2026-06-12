import random, time

def sensor_stream():
    while True:
        temperature = round(random.uniform(20.0, 40.0), 1)
        yield temperature
        
gen = sensor_stream()

for _ in range(10):
    print(next(gen))
    time.sleep(0.5)