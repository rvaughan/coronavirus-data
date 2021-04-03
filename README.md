# Coronavirus Data

This repository contains all of the data that I can find about Coronavirus numbers from around the globe.

The repository is completely automated via [GitHub Actions](https://github.com/features/actions) as a bit
of an experiment, largely inspired by [Simon Williams](https://github.com/simonw/coronavirus-data-gov-archive)
repository, and with leveraging of [The Economists](https://www.economist.com) [Covid 19](https://www.economist.com/graphic-detail/2020/04/16/tracking-covid-19-excess-deaths-across-countries) story [datasets](https://github.com/TheEconomist/covid-19-excess-deaths-tracker).

## Apple Data

  * [Apple Mobility Data](https://www.apple.com/covid19/mobility)

## Australian Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20Australian%20data/badge.svg)

  * [Covid 19 Data](https://www.covid19data.com.au/)
  * [Covid Australia](https://www.covidaustralia.com)
  * [Covid Live](https://covidlive.com.au/)
  * [Matt Bolton](https://github.com/M3IT/COVID-19_Data)
  * [Juliette O'Brien](https://github.com/pappubahry/AU_COVID19)

## Belgian Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20Belgian%20data/badge.svg)

  * [Covid 19 Data](https://epistat.sciensano.be)

## French Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20French%20data/badge.svg)

  * [Covid 19 Data](https://github.com/opencovid19-fr/data)
  * [French Overview](https://dashboard.covid19.data.gouv.fr/vue-d-ensemble?location=FRA) A really informative information site. The underlying data for this is taken from the [French Open Data](https://www.data.gouv.fr/fr/datasets/donnees-hospitalieres-relatives-a-lepidemie-de-covid-19/)
  * [Testing Site Locations](https://www.data.gouv.fr/en/datasets/sites-de-prelevements-pour-les-tests-covid/)
  * [Indicators](https://www.data.gouv.fr/en/datasets/indicateurs-de-suivi-de-lepidemie-de-covid-19/)

## Google Mobility Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20Google%20Mobility%20data/badge.svg)

The Google mobility data is pulled from https://www.google.com/covid19/mobility/ once a day.

## Italian Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20Italian%20data/badge.svg)

  * [Covid 19 Data](https://github.com/pcm-dpc/COVID-19)

## Latin America Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20Latin%20America%20data/badge.svg)

  * [Covid 19 Data](https://https://github.com/DataScienceResearchPeru/covid-19_latinoamerica)

## Microsoft Bing!

Although we're not currently pulling this in - it's 200M - Microsoft do provide a Bing! Covid-19 dataset which can be found in their [Pandemic Data Lake](https://azure.microsoft.com/en-gb/services/open-datasets/catalog/covid-tracking/)

  * [Daily Data](https://pandemicdatalake.blob.core.windows.net/public/raw/covid-19/covid_tracking/latest/daily.json)
  * [Overall Data](https://pandemicdatalake.blob.core.windows.net/public/curated/covid-19/bing_covid-19_data/latest/bing_covid-19_data.json).

## Spanish Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20Spanish%20data/badge.svg)

  * [Covid 19 Data](https://github.com/datadista/datasets)

## Swedish Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20Swedish%20data/badge.svg)

  * [Covid 19 Data](xxx)

## UK Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20UK%20data/badge.svg)

The UK data is pulled twice an hour from the following sources:

  * [England and Wales Data](https://coronavirus.data.gov.uk/)
  * [Northern Ireland](https://www.nisra.gov.uk/publications/weekly-deaths)
  * [Scottish Data](https://www.nrscotland.gov.uk/covid19stats)
  * [Wales Data](https://public.tableau.com/profile/public.health.wales.health.protection#!/vizhome/RapidCOVID-19virology-Public/Headlinesummary)
  * [UK R Number](https://www.gov.uk/government/news/government-publishes-latest-r-number)
  * [SAGE Guidance](https://www.gov.uk/government/collections/scientific-evidence-supporting-the-government-response-to-coronavirus-covid-19)
  * [Independant SAGE Guidance](https://www.independentsage.org/)
  * [PHE National COVID-19 surveillance reports](https://www.gov.uk/government/publications/national-covid-19-surveillance-reports). Note: This data is no longer updated.
  * [PHE Deaths](https://www.gov.uk/government/publications/phe-data-series-on-deaths-in-people-with-covid-19-technical-summary)
  * [PHE Deaths Data](https://coronavirus.data.gov.uk/deaths)
    * Specifically the data files identified on [this](https://coronavirus.data.gov.uk/about-data) page.
  * [Scottish Coronavirus (COVID-19): trends in daily data](https://www.gov.scot/publications/coronavirus-covid-19-trends-in-daily-data/)
  * [Healthcare data](https://coronavirus-staging.data.gov.uk/healthcare)
  * [ZOE Covid App Data](https://covid.joinzoe.com/data)
  * [Hospital Admissions Data](https://www.england.nhs.uk/statistics/statistical-work-areas/covid-19-hospital-activity/)
  * Found an API'fy data source:
    * List of available data [url](https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true).
    * Latest UK data [url](https://api.apify.com/v2/key-value-stores/KWLojgM5r1JmMW4b4/records/LATEST?disableRedirect=true)
    * Latest overall UK data [url](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/bulletins/deathsregisteredweeklyinenglandandwalesprovisional/weekending19march2021)
  * NHS Pathways
    * https://digital.nhs.uk/dashboards/nhs-pathways
    * https://digital.nhs.uk/data-and-information/publications/statistical/mi-potential-covid-19-symptoms-reported-through-nhs-pathways-and-111-online/latest
    * https://digital.nhs.uk/data-and-information/publications/statistical/mi-potential-covid-19-symptoms-reported-through-nhs-pathways-and-111-online
  * [England Hospital Activity](https://www.england.nhs.uk/statistics/statistical-work-areas/covid-19-hospital-activity/)

## USA Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20USA%20data/badge.svg) ![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20USA%20(2)%20data/badge.svg)

The USA data is pulled from https://covidtracking.com/api once an hour.

## Worldwide Data
![Status](https://github.com/rvaughan/coronavirus-data/workflows/Fetch%20latest%20worldwide%20data/badge.svg)

The worldwide data is pulled every hour from:
  * [European Centre for Disease Prevention and Control](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)
  * [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)
