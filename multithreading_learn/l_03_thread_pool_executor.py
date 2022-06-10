import time
import concurrent.futures

# https://www.youtube.com/watch?v=IEEhzQoKtQU&t=624s

start = time.perf_counter()


def send_email(sec):
    print(f'Sending email...{sec} \n')
    time.sleep(sec)
    return f'Sended  in {sec=}\n'


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(send_email, sec) for sec in secs]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    results = executor.map(send_email, secs)
    for result in results:
        print(result)
finish = time.perf_counter()
print(f"Summurize time in {round(finish - start, 2)} sec")
