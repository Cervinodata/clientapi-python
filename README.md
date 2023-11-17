# Cervinodata API Client
<div style='margin: 2em 0;'>
<p>
Before you get going with the Cervinodata API, set up Cervinodata (read the support page here: <a href='https://support.cervinodata.com/hc/en-nl/articles/360004363237' target='_blank'>How to set up the Cervinodata API</a>).
</p>
<h3>To use the Cervinodata API, you need all of the following:</h3>
<p>
<ol>
<li>An active Cervinodata account, you can start a free trial <a href='https://app.cervinodata.com/register' target='_blank'>here</a></li>
<li>At least one connection to a platform (check <a href='https://app.cervinodata.com/data-sources-connections' target='_blank'>here</a>)</li>
<li>At least one account switched ON (check <a href='https://app.cervinodata.com/accounts' target='_blank'>here</a>)</li>
<li>At least one data refresh executed (check <a href='https://app.cervinodata.com/manual-data-refresh' target='_blank'>here</a>)</li>
<li>An active API token (check <a href='https://app.cervinodata.com/settings#/api' target='_blank'>here</a>)</li>
</ol>
</p>
<p>
Note that limits apply for <a href='https://support.cervinodata.com/hc/articles/360014265139' target='_blank'>Free plan users</a>.
</p>
<p>
If you wish to automate your Cervinodata API connection, check out the list of client API's at <a href='https://github.com/Cervinodata' target='_blank'>https://github.com/Cervinodata</a>.
</p>
</div>

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 0.1.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/cervinodata/python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/cervinodata/python.git`)

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

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import cervinodata_api
from cervinodata_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.cervinodata.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = cervinodata_api.Configuration(
    host = "https://app.cervinodata.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = cervinodata_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # List[str] | Organisation uuids
    from_date = '2013-10-20' # date | From date (optional)
    date_format = 'date_format_example' # str | Outputted date format (optional)
    format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return ad account report per organisation per day
        api_response = api_instance.get_ad_account_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        print("The response of AdvertisingDataApi->get_ad_account_report_per_organisation_per_day:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_ad_account_report_per_organisation_per_day: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://app.cervinodata.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdvertisingDataApi* | [**get_ad_account_report_per_organisation_per_day**](docs/AdvertisingDataApi.md#get_ad_account_report_per_organisation_per_day) | **GET** /data/ad-account-report-per-organisation-per-day/{organisationUuids} | Return ad account report per organisation per day
*AdvertisingDataApi* | [**get_ad_accounts**](docs/AdvertisingDataApi.md#get_ad_accounts) | **GET** /data/ad-accounts/{organisationUuid} | Return ad accounts by organisation
*AdvertisingDataApi* | [**get_ad_campaign_report_per_day**](docs/AdvertisingDataApi.md#get_ad_campaign_report_per_day) | **GET** /data/ad-campaign-report-per-day/{organisationUuid} | Return ad campaign report per day by organisation
*AdvertisingDataApi* | [**get_ad_campaign_report_per_organisation_per_account_per_campaign_per_device_per_day**](docs/AdvertisingDataApi.md#get_ad_campaign_report_per_organisation_per_account_per_campaign_per_device_per_day) | **GET** /data/ad-campaign-report-per-organisation-per-account-per-campaign-per-device-per-day/{organisationUuids} | Return ad campaign report per organisation per account per campaign per device per day
*AdvertisingDataApi* | [**get_ad_campaign_report_per_organisation_per_account_per_day**](docs/AdvertisingDataApi.md#get_ad_campaign_report_per_organisation_per_account_per_day) | **GET** /data/ad-campaign-report-per-organisation-per-account-per-day/{organisationUuids} | Return ad campaign report per organisation per account per day
*AdvertisingDataApi* | [**get_ad_campaigns**](docs/AdvertisingDataApi.md#get_ad_campaigns) | **GET** /data/ad-campaigns/{organisationUuid} | Return ad campaigns by organisation
*AdvertisingDataApi* | [**get_ad_groups**](docs/AdvertisingDataApi.md#get_ad_groups) | **GET** /data/ad-groups/{organisationUuid} | Return ad groups by organisation
*AdvertisingDataApi* | [**get_adform_extended_report_per_organisation_per_account_per_campaign_per_creative_per_day**](docs/AdvertisingDataApi.md#get_adform_extended_report_per_organisation_per_account_per_campaign_per_creative_per_day) | **GET** /data/adform-extended-report-per-organisation-per-account-per-campaign-per-creative-per-day/{organisationUuids} | Return adform extended report per organisation per account per campaign per creative per day
*AdvertisingDataApi* | [**get_adform_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/AdvertisingDataApi.md#get_adform_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/adform-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return adform extended report per organisation per account per campaign per day
*AdvertisingDataApi* | [**get_adform_extended_report_per_organisation_per_account_per_campaign_per_line_item_per_day**](docs/AdvertisingDataApi.md#get_adform_extended_report_per_organisation_per_account_per_campaign_per_line_item_per_day) | **GET** /data/adform-extended-report-per-organisation-per-account-per-campaign-per-line-item-per-day/{organisationUuids} | Return adform extended report per organisation per account per campaign per line item per day
*AdvertisingDataApi* | [**get_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/AdvertisingDataApi.md#get_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/bing-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return bing ads extended report per organisation per account per campaign per day
*AdvertisingDataApi* | [**get_facebook_ad_custom_conversion_report_per_organisation_per_account_per_campaign_per_day**](docs/AdvertisingDataApi.md#get_facebook_ad_custom_conversion_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/facebook-ad-custom-conversion-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return facebook ad custom conversion report per organisation per account per campaign per day
*AdvertisingDataApi* | [**get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_group_per_day**](docs/AdvertisingDataApi.md#get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_group_per_day) | **GET** /data/facebook-ad-extended-report-per-organisation-per-account-per-campaign-per-ad-group-per-day/{organisationUuids} | Return facebook ad extended report per organisation per account per campaign per ad group per day
*AdvertisingDataApi* | [**get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_group_per_day_plus**](docs/AdvertisingDataApi.md#get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_group_per_day_plus) | **GET** /data/facebook-ad-extended-report-per-organisation-per-account-per-campaign-per-ad-group-per-day-plus/{organisationUuids} | Return facebook ad extended report per organisation per account per campaign per ad group per day plus
*AdvertisingDataApi* | [**get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_per_day**](docs/AdvertisingDataApi.md#get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_per_day) | **GET** /data/facebook-ad-extended-report-per-organisation-per-account-per-campaign-per-ad-per-day/{organisationUuids} | Return facebook ad extended report per organisation per account per campaign per ad per day
*AdvertisingDataApi* | [**get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/AdvertisingDataApi.md#get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/facebook-ad-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return facebook ad extended report per organisation per account per campaign per day
*AdvertisingDataApi* | [**get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_day_plus**](docs/AdvertisingDataApi.md#get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_day_plus) | **GET** /data/facebook-ad-extended-report-per-organisation-per-account-per-campaign-per-day-plus/{organisationUuids} | Return facebook ad extended report per organisation per account per campaign per day plus
*AdvertisingDataApi* | [**get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_device_per_day**](docs/AdvertisingDataApi.md#get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_device_per_day) | **GET** /data/facebook-ad-extended-report-per-organisation-per-account-per-campaign-per-device-per-day/{organisationUuids} | Return facebook ad extended report per organisation per account per campaign per device per day
*AdvertisingDataApi* | [**get_google_ads_report_per_organisation_per_account_per_campaign_per_device_per_day**](docs/AdvertisingDataApi.md#get_google_ads_report_per_organisation_per_account_per_campaign_per_device_per_day) | **GET** /data/google-ads-report-per-organisation-per-account-per-campaign-per-device-per-day/{organisationUuids} | Return google ads report per organisation per account per campaign per device per day
*AdvertisingDataApi* | [**get_hashed_ad_campaign_report_per_organisation_per_account_per_day**](docs/AdvertisingDataApi.md#get_hashed_ad_campaign_report_per_organisation_per_account_per_day) | **GET** /data/hashed-ad-campaign-report-per-organisation-per-account-per-day/{organisationUuids} | Return hashed ad campaign report per organisation per account per day
*AdvertisingDataApi* | [**get_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/AdvertisingDataApi.md#get_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/linkedin-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return linkedin ads extended report per organisation per account per campaign per day
*AdvertisingDataApi* | [**get_pinterest_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/AdvertisingDataApi.md#get_pinterest_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/pinterest-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return pinterest ads extended report per organisation per account per campaign per day
*AdvertisingDataApi* | [**get_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/AdvertisingDataApi.md#get_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/snapchat-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return snapchat ads extended report per organisation per account per campaign per day
*AdvertisingDataApi* | [**get_tik_tok_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/AdvertisingDataApi.md#get_tik_tok_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/tiktok-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return tiktok ads extended report per organisation per account per campaign per day
*AdvertisingDataApi* | [**get_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/AdvertisingDataApi.md#get_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/twitter-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return twitter ads extended report per organisation per account per campaign per day
*AnalyticsDataApi* | [**get_ga4_report_per_channel_group_per_organisation_per_property**](docs/AnalyticsDataApi.md#get_ga4_report_per_channel_group_per_organisation_per_property) | **GET** /data/ga4-report-per-channel-group-per-organisation-per-property/{organisationUuids} | Return GA4 report per channel group per organisation per property
*AnalyticsDataApi* | [**get_ga4_report_per_channel_group_per_organisation_per_property_per_month**](docs/AnalyticsDataApi.md#get_ga4_report_per_channel_group_per_organisation_per_property_per_month) | **GET** /data/ga4-report-per-channel-group-per-organisation-per-property-per-month/{organisationUuids} | Return GA4 report per channel group per organisation per property per month
*AnalyticsDataApi* | [**get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month**](docs/AnalyticsDataApi.md#get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month) | **GET** /data/ga4-report-per-channel-group-per-product-name-per-organisation-per-property-per-month/{organisationUuids} | Return GA4 report per channel group per product name per organisation per property per month
*AnalyticsDataApi* | [**get_ga4_report_per_channel_group_per_source_medium_per_organisation_per_property_per_month**](docs/AnalyticsDataApi.md#get_ga4_report_per_channel_group_per_source_medium_per_organisation_per_property_per_month) | **GET** /data/ga4-report-per-channel-group-per-source-medium-per-organisation-per-property-per-month/{organisationUuids} | Return GA4 report per channel group per source medium per organisation per property per month
*AnalyticsDataApi* | [**get_views**](docs/AnalyticsDataApi.md#get_views) | **GET** /data/views/{organisationUuid} | Return views by organisation
*AnalyticsDataDefaultMetricsApi* | [**get_analytics_report_per_campaign_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_campaign_per_day) | **GET** /data/analytics-report-per-campaign-per-day/{organisationUuid} | Return analytics report per campaign per day by organisation
*AnalyticsDataDefaultMetricsApi* | [**get_analytics_report_per_channel_group_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_channel_group_per_day) | **GET** /data/analytics-report-per-channel-group-per-day/{organisationUuid} | Return analytics report per channel group per day by organisation
*AnalyticsDataDefaultMetricsApi* | [**get_analytics_report_per_device_per_channel_group_per_organisation_per_view_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_device_per_channel_group_per_organisation_per_view_per_day) | **GET** /data/analytics-report-per-device-per-channel-group-per-organisation-per-view-per-day/{organisationUuids} | Return analytics report per device per channel group per organisation per view per day
*AnalyticsDataDefaultMetricsApi* | [**get_analytics_report_per_device_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_device_per_day) | **GET** /data/analytics-report-per-device-per-day/{organisationUuid} | Return analytics report per device per day by organisation
*AnalyticsDataDefaultMetricsApi* | [**get_analytics_report_per_source_medium_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_source_medium_per_day) | **GET** /data/analytics-report-per-source-medium-per-day/{organisationUuid} | Return analytics report per source medium per day by organisation
*AnalyticsDataDefaultMetricsApi* | [**get_ga4_report_per_device_per_channel_group_per_organisation_per_property_per_day**](docs/AnalyticsDataDefaultMetricsApi.md#get_ga4_report_per_device_per_channel_group_per_organisation_per_property_per_day) | **GET** /data/ga4-report-per-device-per-channel-group-per-organisation-per-property-per-day/{organisationUuids} | Return GA4 report per device per channel group per organisation per property per day
*AnalyticsDataGoalsApi* | [**get_analytics_goal_report_per_campaign_per_day**](docs/AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_campaign_per_day) | **GET** /data/analytics-goal-report-per-campaign-per-day/{organisationUuid} | Return analytics goal report per campaign per day by organisation
*AnalyticsDataGoalsApi* | [**get_analytics_goal_report_per_channel_group_per_day**](docs/AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_channel_group_per_day) | **GET** /data/analytics-goal-report-per-channel-group-per-day/{organisationUuid} | Return analytics goal report per channel group per day by organisation
*AnalyticsDataGoalsApi* | [**get_analytics_goal_report_per_device_per_day**](docs/AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_device_per_day) | **GET** /data/analytics-goal-report-per-device-per-day/{organisationUuid} | Return analytics goal report per device per day by organisation
*AnalyticsDataGoalsApi* | [**get_analytics_goal_report_per_source_medium_per_day**](docs/AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_source_medium_per_day) | **GET** /data/analytics-goal-report-per-source-medium-per-day/{organisationUuid} | Return analytics goal report per source medium per day by organisation
*AnalyticsDataProductMetricsApi* | [**get_ga4_report_per_product_name_per_organisation_per_property_per_week**](docs/AnalyticsDataProductMetricsApi.md#get_ga4_report_per_product_name_per_organisation_per_property_per_week) | **GET** /data/ga4-report-per-product-name-per-organisation-per-property-per-week/{organisationUuids} | Return GA4 report per product name per organisation per property per week
*AnalyticsDataProductMetricsApi* | [**get_ga4_report_per_product_sku_per_organisation_per_property_per_week**](docs/AnalyticsDataProductMetricsApi.md#get_ga4_report_per_product_sku_per_organisation_per_property_per_week) | **GET** /data/ga4-report-per-product-sku-per-organisation-per-property-per-week/{organisationUuids} | Return GA4 report per product sku per organisation per property per week
*AnalyticsDataTransactionMetricsApi* | [**get_ga4_report_per_campaign_per_organisation_per_property**](docs/AnalyticsDataTransactionMetricsApi.md#get_ga4_report_per_campaign_per_organisation_per_property) | **GET** /data/ga4-report-per-campaign-per-organisation-per-property/{organisationUuids} | Return GA4 report per campaign per organisation per property
*AnalyticsDataTransactionMetricsApi* | [**get_ga4_report_per_campaign_per_organisation_per_property_per_month**](docs/AnalyticsDataTransactionMetricsApi.md#get_ga4_report_per_campaign_per_organisation_per_property_per_month) | **GET** /data/ga4-report-per-campaign-per-organisation-per-property-per-month/{organisationUuids} | Return GA4 report per campaign per organisation per property per month
*CampaignGroupApi* | [**get_campaign_group_ad_report_per_organisation_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_ad_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-ad-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group ad report per organisation per campaign per day
*CampaignGroupApi* | [**get_campaign_group_ad_report_per_organisation_per_campaign_per_week**](docs/CampaignGroupApi.md#get_campaign_group_ad_report_per_organisation_per_campaign_per_week) | **GET** /data/campaign-group-ad-report-per-organisation-per-campaign-per-week/{organisationUuids} | Return campaign group ad report per organisation per campaign per week
*CampaignGroupApi* | [**get_campaign_group_ad_report_per_organisation_per_day**](docs/CampaignGroupApi.md#get_campaign_group_ad_report_per_organisation_per_day) | **GET** /data/campaign-group-ad-report-per-organisation-per-day/{organisationUuids} | Return campaign group ad report per organisation per day
*CampaignGroupApi* | [**get_campaign_group_adform_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_adform_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-adform-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group adform extended report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_adform_report_per_organisation_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_adform_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-adform-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group adform report per organisation per campaign per day
*CampaignGroupApi* | [**get_campaign_group_adform_report_per_organisation_per_campaign_per_line_item_per_day**](docs/CampaignGroupApi.md#get_campaign_group_adform_report_per_organisation_per_campaign_per_line_item_per_day) | **GET** /data/campaign-group-adform-report-per-organisation-per-campaign-per-line-item-per-day/{organisationUuids} | Return campaign group adform report per organisation per campaign per line-item per day
*CampaignGroupApi* | [**get_campaign_group_analytics_report_per_organisation_per_day**](docs/CampaignGroupApi.md#get_campaign_group_analytics_report_per_organisation_per_day) | **GET** /data/campaign-group-analytics-report-per-organisation-per-day/{organisationUuids} | Return campaign group analytics report per organisation per day
*CampaignGroupApi* | [**get_campaign_group_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-bing-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group bing ads extended report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_double_click_bid_manager_report_per_organisation_per_account_per_campaign_per_creative_per_day**](docs/CampaignGroupApi.md#get_campaign_group_double_click_bid_manager_report_per_organisation_per_account_per_campaign_per_creative_per_day) | **GET** /data/campaign-group-doubleclick-bid-manager-report-per-organisation-per-account-per-campaign-per-creative-per-day/{organisationUuids} | Return campaign group doubleclick bid manager report per organisation per account per campaign per creative per day
*CampaignGroupApi* | [**get_campaign_group_double_click_bid_manager_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_double_click_bid_manager_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-doubleclick-bid-manager-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group doubleclick bid manager report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_double_click_campaign_manager_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_double_click_campaign_manager_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-doubleclick-campaign-manager-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group doubleclick campaign manager report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_facebook_ad_custom_conversion_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_facebook_ad_custom_conversion_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-facebook-ad-custom-conversion-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group facebook ad custom conversion report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_group_per_day**](docs/CampaignGroupApi.md#get_campaign_group_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_group_per_day) | **GET** /data/campaign-group-facebook-ad-extended-report-per-organisation-per-account-per-campaign-per-ad-group-per-day/{organisationUuids} | Return campaign group facebook ad extended report per organisation per account per campaign per ad group per day
*CampaignGroupApi* | [**get_campaign_group_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_per_day**](docs/CampaignGroupApi.md#get_campaign_group_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_ad_per_day) | **GET** /data/campaign-group-facebook-ad-extended-report-per-organisation-per-account-per-campaign-per-ad-per-day/{organisationUuids} | Return campaign group facebook ad extended report per organisation per account per campaign per ad per day
*CampaignGroupApi* | [**get_campaign_group_facebook_ad_extended_report_per_organisation_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_facebook_ad_extended_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-facebook-ad-extended-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group facebook ad extended report per organisation per campaign per day
*CampaignGroupApi* | [**get_campaign_group_facebook_ad_report_per_organisation_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_facebook_ad_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-facebook-ad-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group facebook ad report per organisation per campaign per day
*CampaignGroupApi* | [**get_campaign_group_goal_report_per_organisation_per_day**](docs/CampaignGroupApi.md#get_campaign_group_goal_report_per_organisation_per_day) | **GET** /data/campaign-group-goal-report-per-organisation-per-day/{organisationUuids} | Return campaign group goal report per organisation per day
*CampaignGroupApi* | [**get_campaign_group_google_ads_extended_report_per_organisation_per_account_per_campaign_per_ad_group_per_day**](docs/CampaignGroupApi.md#get_campaign_group_google_ads_extended_report_per_organisation_per_account_per_campaign_per_ad_group_per_day) | **GET** /data/campaign-group-google-ads-extended-report-per-organisation-per-account-per-campaign-per-ad-group-per-day/{organisationUuids} | Return campaign group google ads extended report per organisation per account per campaign per ad group per day
*CampaignGroupApi* | [**get_campaign_group_google_ads_report_per_organisation_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_google_ads_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-google-ads-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group google ads report per organisation per campaign per day
*CampaignGroupApi* | [**get_campaign_group_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-linkedin-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group linkedin ads extended report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_pinterest_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_pinterest_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-pinterest-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group pinterest ads extended report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_report_per_organisation_per_day**](docs/CampaignGroupApi.md#get_campaign_group_report_per_organisation_per_day) | **GET** /data/campaign-group-report-per-organisation-per-day/{organisationUuids} | Return campaign group report per organisation per day
*CampaignGroupApi* | [**get_campaign_group_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-snapchat-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group snapchat ads extended report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_tik_tok_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_tik_tok_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-tiktok-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group tiktok ads extended report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-twitter-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group twitter ads extended report per organisation per account per campaign per day
*CampaignGroupApi* | [**get_campaign_group_video_report_per_organisation_per_campaign_per_day**](docs/CampaignGroupApi.md#get_campaign_group_video_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-video-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group video report per organisation per campaign per day
*CampaignGroupApi* | [**get_campaign_group_video_report_per_organisation_per_day**](docs/CampaignGroupApi.md#get_campaign_group_video_report_per_organisation_per_day) | **GET** /data/campaign-group-video-report-per-organisation-per-day/{organisationUuids} | Return campaign group video report per organisation per day
*GenericDataApi* | [**get_campaign_groups**](docs/GenericDataApi.md#get_campaign_groups) | **GET** /data/campaign-groups | Return campaign groups
*GenericDataApi* | [**get_organisations**](docs/GenericDataApi.md#get_organisations) | **GET** /data/organisations | Return organisations
*ProductDataApi* | [**get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month**](docs/ProductDataApi.md#get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month) | **GET** /data/ga4-report-per-channel-group-per-product-name-per-organisation-per-property-per-month/{organisationUuids} | Return GA4 report per channel group per product name per organisation per property per month


## Documentation For Models



<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearerAuth"></a>
### bearerAuth

- **Type**: Bearer authentication


## Author

support@cervinodata.com


