import csv
import json

from requests import get


def get_data(url: str, params):
    response = get(endpoint, params=params, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
    

if __name__ == '__main__':
    AREA_TYPE = "ltla"

    with open('../data/uk/ltla_to_utla_lookup.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ltla = row[2]

            endpoint = 'https://api.coronavirus.data.gov.uk/v1/data'

            filters = [
                f"areaType={ AREA_TYPE }",
                f"areaName={ ltla }"
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
                data = get_data(endpoint, api_params)

                with open('../data/uk/ltla/{}.json'.format(ltla), 'w') as f:
                    f.write(json.dumps(data))
            except:
                pass
