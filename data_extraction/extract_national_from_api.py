import json

from requests import get


def get_data(url: str):
    response = get(endpoint, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
    

if __name__ == '__main__':
    for nation in ["wales", "scotland", "england", "northern ireland"]:
        endpoint = (
            'https://api.coronavirus.data.gov.uk/v1/data?'
            'filters=areaType=nation;areaName=' + nation + '&'
            'structure={"date":"date","newCases":"newCasesByPublishDate","newDeaths28DaysByPublishDate":"newDeaths28DaysByPublishDate"}'
        )
    
        try:
            data = get_data(endpoint)

            with open('../data/uk/{} new cases.json'.format(nation), 'w') as f:
                f.write(json.dumps(data))
        except:
            pass
