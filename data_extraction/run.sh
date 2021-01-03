#!/usr/bin/env bash

if [ ! -d venv ]
then
    virtualenv venv
    source ./venv/bin/activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    deactivate
fi

source ./venv/bin/activate

python extract_wales.py

python extract_national_from_api.py
python extract_utla_from_api.py
python extract_ltla_from_api.py

python extract_nhs_england_from_api.py
