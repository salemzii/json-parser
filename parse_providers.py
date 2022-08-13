import csv


# parse value from each yielded record
def Parse_provider(record: dict):
    value = {}
    values = []

    for k, v in record.items():
        if not k == "provider_groups":
            value["provider_group_id"] = v
        if k == "provider_groups":
            for i in v:
                try:
                    value["npi"] = i["npi"][0]
                    value["tin_type"] = i["tin"]["type"].upper()
                    value["tin"] = i["tin"]["value"]
                    values.append(value)
                except Exception as err:
                    print("Encountered empty npi list, moving to next record")
                    pass
    return values

# Writes to CSV
def providers_csvwriter(values: list):
    print(values)
    filename = "Providers.csv"
    fields = ["provider_group_id","tin","tin_type","npi"]
    with open(filename, "w") as providers:
        writer = csv.DictWriter(providers, fieldnames = fields) 
        writer.writeheader() 
        # writing data rows 
        writer.writerows(values)
    return
