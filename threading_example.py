import threading
import time

def robot_task(name, duration):
    print(f'{name} starting task.')
    time.sleep(duration)
    print(f'{name} has completed its task')

# Creating threads
thread1 = threading.Thread(target=robot_task, args=('Robot 1', 2))
thread2 = threading.Thread(target=robot_task, args=('Robot 2', 3))

thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print('Both robots have completed their tasks.')

