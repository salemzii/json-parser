from optparse import Values
import ijson,csv

def service_codes():
    values = []
    with open("Input_File.json", "rb") as input_file:
        for record in ijson.items(input_file, "in_network.item"):
            values.append(Parse_service_code(record=record))
        service_codes_csvwriter(values)

def Parse_service_code(record: dict):
    values = []
    for k, v in record.items():
        value = {}
        if k == "negotiated_rates":
            for i in v:
                value["service_code"] = i["negotiated_prices"][0]["service_code"]
        values.append(value)
    return value

def service_codes_csvwriter(values: list):

    filename = "Service_code_groupsCSV.csv"
    fields = ["service_code", "service_code_group"]
    with open(filename, "a+") as rates:
        writer = csv.DictWriter(rates, fieldnames = fields) 
        writer.writeheader()
        # writing data rows 
        scg = 1
        for value in values:
            for _, v in value.items():
                for i in range(len(v)):
                    writer.writerow({"service_code": v[i], "service_code_group": scg})
            scg += 1
    return
