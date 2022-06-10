import time
# https://www.youtube.com/watch?v=IEEhzQoKtQU&t=624s

start = time.perf_counter()


def send_email():
    print('Sending email...')
    time.sleep(1)
    print('Sended')


send_email()  # first time
send_email()  # second time
finish = time.perf_counter()
print(f"Summurize time in {round(finish - start, 2)} sec")
