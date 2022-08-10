from parse_codes import codes, Parse_codes
from parse_providers import providers, Parse_provider
from parse_rates import rates, Parse_rates
import threading, ijson





th1 = threading.Thread(target=codes)
th2 = threading.Thread(target=providers)
th3 = threading.Thread(target=rates)


th1.start()
th2.start()
th3.start()

th1.join()
th2.join()
th3.join()


    
