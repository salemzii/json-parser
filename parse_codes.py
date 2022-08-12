import csv

def Parse_codes(record: dict):
    value = {}
    values = []

    for k, v in record.items():
        
        if k == "negotiation_arrangement":
            value["negotiation_arrangement"] = v
        elif k == "billing_code_type_version":
            value ["billing_code_type_version"] = v
        elif k == "billing_code":
            value["billing_code"] = v
        elif k == "name":
            value["billing_code_name"] = v
        elif k == "billing_code_type":
            value["billing_code_type"] = v
        elif k == "description":
            value["billing_code_description"] = v
        values.append(value)
    return values

def codes_csvwriter(values: list):
    print(values)
    filename = "CodesCSV.csv"
    fields = ["billing_code","billing_code_type",
    "billing_code_type_version",
    "billing_code_description",
    "billing_code_name",
    "negotiation_arrangement"]
    with open(filename, "w") as rates:
        writer = csv.DictWriter(rates, fieldnames = fields) 
        writer.writeheader() 
        # writing data rows 
        writer.writerows(values)
    return
