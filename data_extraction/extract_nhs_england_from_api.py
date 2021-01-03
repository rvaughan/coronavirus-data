import csv
import json

from urllib.parse import urlencode
from requests import get


def get_data(url: str, params):
    response = get(endpoint, params=params, timeout=10)
    
    if response.status_code >= 400:
        raise Exception(f'Request failed: { response.text }')
        
    return response.json()
    

if __name__ == '__main__':
    AREA_TYPE = "nhsRegion"

    with open('../data/uk/nhs_england_regions.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        first = True
        for row in reader:
            if first:
                first = False
                continue

            region = row[0].strip()

            endpoint = 'https://api.coronavirus.data.gov.uk/v1/data'

            filters = [
                f"areaType={ AREA_TYPE }",
                f"areaCode={ region }"
            ]

            structure = {
                "date": "date",
                "cases": "newCasesByPublishDate",
                "male": "maleCases",
                "female": "femaleCases",
                "deaths": "newCasesBySpecimenDate",
                "pillarOne": "newPillarOneTestsByPublishDate",
                "pillarTwo": "newPillarTwoTestsByPublishDate",
                "pillarThree": "newPillarThreeTestsByPublishDate",
                "pillarFout": "newPillarFourTestsByPublishDate",
                "admissions": "newAdmissions",
                "covidBeds": "covidOccupiedMVBeds"
            }
    
            api_params = {
                "filters": str.join(";", filters),
                "structure": json.dumps(structure, separators=(",", ":")),
                "format": "json"
            }

            try:
                data = get_data(endpoint, urlencode(api_params))

                with open('../data/uk/nhs/{}.json'.format(region), 'w') as f:
                    f.write(json.dumps(data))
            except Exception as e:
                print(e)
                pass
