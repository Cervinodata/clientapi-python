# Cervinodata API Client
<div style='margin: 2em 0;'><p>Before you get going with the Cervinodata API, set up Cervinodata (read the support page here: <a href='https://support.cervinodata.com/hc/en-nl/articles/360004363237' target='_blank'>How to set up the Cervinodata API</a>).</p> <h2>To use the Cervinodata API, you need all of the following:</h2> <p> <ol> <li>An active Cervinodata account, you can start a free trial <a href='https://app.cervinodata.com/register' target='_blank'>here</a></li> <li>At least one connection to a platform (check <a href='https://app.cervinodata.com/pages/data-sources/connections' target='_blank'>here</a>)</li> <li>At least one account switched ON (check <a href='https://app.cervinodata.com/pages/data-sources/accounts' target='_blank'>here</a>)</li> <li>At least one data refresh executed (check <a href='https://app.cervinodata.com/pages/data-destinations-api/data-collection' target='_blank'>here</a>)</li> <li>An active API token (check <a href='https://app.cervinodata.com/settings#/api' target='_blank'>here</a>)</li> </ol> </p> </div>

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/cervinodata/clientapi-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/cervinodata/clientapi-python.git`)

Then import the package:
```python
import cervinodata_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cervinodata_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cervinodata_api
from cervinodata_api.rest import ApiException
from pprint import pprint

configuration = cervinodata_api.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://app.cervinodata.com/api/v1
configuration.host = "https://app.cervinodata.com/api/v1"
# Create an instance of the API class
api_instance = cervinodata_api.AdvertisingDataApi(cervinodata_api.ApiClient(configuration))
organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
format = 'format_example' # str | Output format (optional)

try:
    # Return ad accounts by organisation
    api_response = api_instance.get_ad_accounts(organisation_uuid, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdvertisingDataApi->get_ad_accounts: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://app.cervinodata.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdvertisingDataApi* | [**get_ad_accounts**](docs/AdvertisingDataApi.md#get_ad_accounts) | **GET** /data/ad-accounts/{organisationUuid} | Return ad accounts by organisation
*AdvertisingDataApi* | [**get_ad_campaign_report_per_day**](docs/AdvertisingDataApi.md#get_ad_campaign_report_per_day) | **GET** /data/ad-campaign-report-per-day/{organisationUuid} | Return ad campaign report per day by organisation
*AdvertisingDataApi* | [**get_ad_campaign_report_per_organisation_per_account_per_day**](docs/AdvertisingDataApi.md#get_ad_campaign_report_per_organisation_per_account_per_day) | **GET** /data/ad-campaign-report-per-organisation-per-account-per-day/{organisationUuids} | Return ad campaign report per organisation per account per day
*AdvertisingDataApi* | [**get_ad_campaigns**](docs/AdvertisingDataApi.md#get_ad_campaigns) | **GET** /data/ad-campaigns/{organisationUuid} | Return ad campaigns by organisation
*AnalyticsDataApi* | [**get_views**](docs/AnalyticsDataApi.md#get_views) | **GET** /data/views/{organisationUuid} | Return views by organisation
*AnalyticsDataDefaultMetricsApi* | [**get_analytics_report_per_campaign_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_campaign_per_day) | **GET** /data/analytics-report-per-campaign-per-day/{organisationUuid} | Return analytics report per campaign per day by organisation
*AnalyticsDataDefaultMetricsApi* | [**get_analytics_report_per_channel_group_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_channel_group_per_day) | **GET** /data/analytics-report-per-channel-group-per-day/{organisationUuid} | Return analytics report per channel group per day by organisation
*AnalyticsDataDefaultMetricsApi* | [**get_analytics_report_per_device_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_device_per_day) | **GET** /data/analytics-report-per-device-per-day/{organisationUuid} | Return analytics report per device per day by organisation
*AnalyticsDataDefaultMetricsApi* | [**get_analytics_report_per_source_medium_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_source_medium_per_day) | **GET** /data/analytics-report-per-source-medium-per-day/{organisationUuid} | Return analytics report per source medium per day by organisation
*AnalyticsDataGoalsApi* | [**get_analytics_goal_report_per_campaign_per_day**](docs/AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_campaign_per_day) | **GET** /data/analytics-goal-report-per-campaign-per-day/{organisationUuid} | Return analytics goal report per campaign per day by organisation
*AnalyticsDataGoalsApi* | [**get_analytics_goal_report_per_channel_group_per_day**](docs/AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_channel_group_per_day) | **GET** /data/analytics-goal-report-per-channel-group-per-day/{organisationUuid} | Return analytics goal report per channel group per day by organisation
*AnalyticsDataGoalsApi* | [**get_analytics_goal_report_per_device_per_day**](docs/AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_device_per_day) | **GET** /data/analytics-goal-report-per-device-per-day/{organisationUuid} | Return analytics goal report per device per day by organisation
*AnalyticsDataGoalsApi* | [**get_analytics_goal_report_per_source_medium_per_day**](docs/AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_source_medium_per_day) | **GET** /data/analytics-goal-report-per-source-medium-per-day/{organisationUuid} | Return analytics goal report per source medium per day by organisation
*GenericDataApi* | [**get_campaign_groups**](docs/GenericDataApi.md#get_campaign_groups) | **GET** /data/campaign-groups | Return campaign groups
*GenericDataApi* | [**get_organisations**](docs/GenericDataApi.md#get_organisations) | **GET** /data/organisations | Return organisations


## Documentation For Models



## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication


## Author

support@cervinodata.com


