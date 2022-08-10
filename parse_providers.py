import ijson, time, csv


def providers():
    values = []
    with open("Input_File.json", "rb") as input_file:
        for record in ijson.items(input_file, "provider_references.item"):
            values += Parse_provider(record=record)
    csvwriter(values)

# parse value from each yielded record
def Parse_provider(record: dict):
    value = {}
    values = []

    for k, v in record.items():
        if not k == "provider_groups":
            value["provider_group_id"] = v
        if k == "provider_groups":
            for i in v:
                value["npi"] = i["npi"][0]
                value["tin_type"] = i["tin"]["type"].upper()
                value["tin"] = i["tin"]["value"]
                values.append(value)
    csvwriter(values=values)
    return values

# Writes to CSV
def csvwriter(values: list):
    print(values)
    filename = "Providers.csv"
    fields = ["provider_group_id","tin","tin_type","npi"]
    with open(filename, "w") as providers:
        writer = csv.DictWriter(providers, fieldnames = fields) 
        writer.writeheader() 
        # writing data rows 
        writer.writerows(values)
    return

'''
t1 = time.time()
providers()
print("Total time taken: ", time.time()-t1)
'''
