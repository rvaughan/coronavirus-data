import json

from requests import get


def get_data(url: str, params):
    response = get(endpoint, params=params, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
    

if __name__ == '__main__':
    AREA_TYPE = "nation"
    for nation in ["wales", "scotland", "england", "northern ireland"]:
        endpoint = 'https://api.coronavirus.data.gov.uk/v1/data'

        filters = [
            f"areaType={ AREA_TYPE }",
            f"areaName={ nation }"
        ]

        structure = {
            "date": "date",
            "cases": "newCasesByPublishDate",
            "hospitalCases": "hospitalCases",
            "male": "maleCases",
            "female": "femaleCases",
            "deaths": "newDeaths28DaysByPublishDate",
            "pillarOne": "newPillarOneTestsByPublishDate",
            "pillarTwo": "newPillarTwoTestsByPublishDate",
            "pillarThree": "newPillarThreeTestsByPublishDate",
            "pillarFout": "newPillarFourTestsByPublishDate",
            "admissions": "newAdmissions"
        }

        api_params = {
            "filters": str.join(";", filters),
            "structure": json.dumps(structure, separators=(",", ":")),
            "format": "json"
        }
    
        try:
            data = get_data(endpoint, api_params)

            with open('../data/uk/{} new cases.json'.format(nation), 'w') as f:
                f.write(json.dumps(data))
        except:
            pass
