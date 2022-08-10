from parse_codes import codes, Parse_codes
from parse_providers import providers, Parse_provider
from parse_rates import rates, Parse_rates
import threading, ijson




# register threads
th1 = threading.Thread(target=codes)
th2 = threading.Thread(target=providers)
th3 = threading.Thread(target=rates)

# start the thread
th1.start()
th2.start()
th3.start()

# wait for threads to complete
th1.join()
th2.join()
th3.join()


    
