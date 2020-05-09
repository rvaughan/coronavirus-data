# Coronavirus Data

This repository contains all of the data that I can find about Coronavirus numbers from around the globe.

The repository is completely automated via [GitHub Actions](https://github.com/features/actions) as a bit
of an experiment, largely inspired by [Simon Williams](https://github.com/simonw/coronavirus-data-gov-archive) repository.

## Google Mobility Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20Google%20Mobility%20data/badge.svg)

The Google mobility data is pulled from https://www.google.com/covid19/mobility/ once a day.

## UK Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20UK%20data/badge.svg)

The UK data is pulled from https://coronavirus.data.gov.uk/ twice an hour.

## USA Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20USA%20data/badge.svg)

The USA data is pulled from https://covidtracking.com/api once an hour.

## Worldwide Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20worldwide%20data/badge.svg)

The worldwide data is pulled every hour from:
  * [European Centre for Disease Prevention and Control](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)
  * [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)
