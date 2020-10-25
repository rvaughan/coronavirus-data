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
