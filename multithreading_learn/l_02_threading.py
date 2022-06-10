import time
import threading
# https://www.youtube.com/watch?v=IEEhzQoKtQU&t=624s

start = time.perf_counter()


def send_email(sec):
    print(f'Sending email...{sec} \n')
    time.sleep(sec)
    print('Sended \n')


threads = []

for _ in range(10):

    t = threading.Thread(target=send_email, args=[3])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()


finish = time.perf_counter()
print(f"Summurize time in {round(finish - start, 2)} sec")
