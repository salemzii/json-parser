import ijson,csv


def rates():
    values = []
    with open("Input_File.json", "rb") as input_file:
        for record in ijson.items(input_file, "in_network.item"):
            values += Parse_rates(record=record)
        rates_csvwriter(values=values)


def Parse_rates(record: dict):
    value = {}
    values = []
    for k, v in record.items():
        
        if k == "billing_code":
            value["billing_code"] = v
        elif k == "billing_code_type_version":
            value ["billing_code_type_version"] = v
        elif k == "negotiated_rates":
            code = 1
            for i in v:
                value["provider_references"] = i["provider_references"][0]
                value["negotiated_rate"] = i["negotiated_prices"][0]["negotiated_rate"]
                value["billing_class"] = i["negotiated_prices"][0]["billing_class"]
                value["expiration_date"] = i["negotiated_prices"][0]["expiration_date"]
                value["negotiated_type"] = i["negotiated_prices"][0]["negotiated_type"]
                value["service_code_group"] = code
                code += 1
                try:
                    value["billing_code_modifier"] = i["negotiated_prices"][0]["billing_code_modifier"][0]
                except Exception as err:
                    pass
                print(value)
                values.append(value)
    
    return values

def rates_csvwriter(values: list):
  
    filename = "RatesCSV.csv"
    fields = ["billing_code","billing_code_modifier",
    "billing_code_type_version",
    "provider_references","negotiated_rate",
    "billing_class","expiration_date",
    "negotiated_type","service_code_group"]
    with open(filename, "w") as rates:
        writer = csv.DictWriter(rates, fieldnames = fields) 
        writer.writeheader() 
        # writing data rows 
        writer.writerows(values)
    return



'''
t1 = time.time()
rates()
print("Total time taken: ", time.time()-t1)
'''