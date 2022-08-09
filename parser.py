import csv, ijson


class Parser():

    def __init__(self, input_json: str) -> None:
        self.input_json = input_json

    @staticmethod
    def Parse_provider(self, record: dict) -> list:
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
        return values 

    @staticmethod
    def Parse_codes(self, record: dict) -> list:
        value = {}
        values = []

        for k, v in record.items():
            #print(k, v)
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
            print(value)
            values.append(value)
        return values

    @staticmethod
    def Parse_rates(self, record: dict) -> list:
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

    @staticmethod
    def csvwriter(self, values: list):
        print(values)
        filename = "Providers.csv"
        fields = ["provider_group_id","tin","tin_type","npi"]
        with open(filename, "w") as providers:
            writer = csv.DictWriter(providers, fieldnames = fields) 
            writer.writeheader() 
            # writing data rows 
            writer.writerows(values)
        return