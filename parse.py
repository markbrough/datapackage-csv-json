#!/usr/bin/env python

import json
import unicodecsv
import os

"""Converts a datapackage JSON file plus CSV file to JSON as if it were served from the CKAN data store API"""

def nameid(row):
    row["id"] = row["name"]
    return row

def fields(fields_data):
    return list(map(lambda x: nameid(x), fields_data))

def run(dirname, datapackage, resource_name=None):
    """Provide a datapackage JSON file and (optionally) specify the resource name"""
    dp_f = open(os.path.join(dirname, datapackage), "r")
    dp_d = json.load(dp_f)
    
    out = {
        "help": "",
        "success": True,
        "result": {
            "resource_id": resource_name
        },
        "records": []
    }
    for resource in dp_d["resources"]:
        if resource["name"] == "eiti_normalised":
            out["result"]["fields"] = fields(resource["schema"]["fields"])
            
            csv_f = open(os.path.join(dirname, resource["path"]), "r")
            csv_d = unicodecsv.DictReader(csv_f)
            for row in csv_d:
                out["records"].append(row)
                
    return json.dumps(out, indent=2)
    
if __name__ == '__main__':
    print run("../NRGI/eiti-parser/", "datapackage.json", "eiti_normalised")