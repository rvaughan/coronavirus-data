import csv
import json

from requests import get


def get_data(url: str):
    response = get(endpoint, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
    

if __name__ == '__main__':
    with open('../data/uk/ltla_to_utla_lookup.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            utla = row[3]

            endpoint = (
                'https://api.coronavirus.data.gov.uk/v1/data?'
                'filters=areaType=utla;areaCode=' + utla + '&'
                'structure={"date":"date","newCases":"newCasesByPublishDate","newCasesBySpecimenDate":"newCasesBySpecimenDate"}'
            )
        
            try:
                data = get_data(endpoint)

                with open('../data/uk/utla/{}.json'.format(utla), 'w') as f:
                    f.write(json.dumps(data))
            except:
                pass
