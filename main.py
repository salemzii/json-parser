import ijson
import parse_codes
import parse_providers
import parse_rates

if __name__ == "main":
    with open("Input_File.json", "rb") as input_file:
        for record in ijson.items(input_file, "in_network.item"):
            parse_providers.Parse_provider(record= record)
            parse_codes.Parse_codes(record=record)
            parse_rates.Parse_rates(record)
        


