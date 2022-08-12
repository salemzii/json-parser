from parse_codes import Parse_codes, codes_csvwriter
from parse_providers import providers_csvwriter, Parse_provider
from parse_rates import Parse_rates, rates_csvwriter
from parse_service_code import Parse_service_code, service_codes_csvwriter
import threading, time, ijson, sys

json_file_path = sys.argv[-1]

def providers(path: str):
    values = []
    with open(path, "rb") as input_file:
        for record in ijson.items(input_file, "provider_references.item"):
            values += Parse_provider(record=record)
    providers_csvwriter(values)

def in_networks(path: str):
    service_code_values = []
    codes_value = []
    rates_value = []
    with open(path, "rb") as input_file:
        for record in ijson.items(input_file, "in_network.item"):
            service_code_values.append((Parse_service_code(record=record)))
            codes_value += Parse_codes(record=record)
            rates_value += Parse_rates(record=record)

        service_codes_csvwriter(service_code_values)
        rates_csvwriter(rates_value)
        codes_csvwriter(codes_value)

timer = time.time()

th1 = threading.Thread(target=providers, args=(json_file_path,))
th2 = threading.Thread(target=in_networks, args=(json_file_path,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Total time take: {time.time() - timer }")
