from parse_codes import codes
from parse_providers import providers
from parse_rates import rates
from parse_service_code import service_codes
import threading, time



timer = time.time()
# register threads
th1 = threading.Thread(target=codes)
th2 = threading.Thread(target=providers)
th3 = threading.Thread(target=rates)
th4 = threading.Thread(target=service_codes)

# start the thread
th1.start()
th2.start()
th3.start()
th4.start()

# wait for threads to complete
th1.join()
th2.join()
th3.join()
th4.join()

print(f"Total time take: {time.time() - timer }")