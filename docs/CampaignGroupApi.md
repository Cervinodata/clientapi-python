# cervinodata_api.CampaignGroupApi

All URIs are relative to *https://app.cervinodata.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campaign_group_ad_report_per_organisation_per_campaign_per_day**](CampaignGroupApi.md#get_campaign_group_ad_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-ad-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group ad report per organisation per campaign per day
[**get_campaign_group_ad_report_per_organisation_per_day**](CampaignGroupApi.md#get_campaign_group_ad_report_per_organisation_per_day) | **GET** /data/campaign-group-ad-report-per-organisation-per-day/{organisationUuids} | Return campaign group ad report per organisation per day
[**get_campaign_group_analytics_report_per_organisation_per_day**](CampaignGroupApi.md#get_campaign_group_analytics_report_per_organisation_per_day) | **GET** /data/campaign-group-analytics-report-per-organisation-per-day/{organisationUuids} | Return campaign group analytics report per organisation per day
[**get_campaign_group_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](CampaignGroupApi.md#get_campaign_group_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-bing-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group bing ads extended report per organisation per account per campaign per day
[**get_campaign_group_facebook_ad_extended_report_per_organisation_per_campaign_per_day**](CampaignGroupApi.md#get_campaign_group_facebook_ad_extended_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-facebook-ad-extended-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group facebook ad extended report per organisation per campaign per day
[**get_campaign_group_facebook_ad_report_per_organisation_per_campaign_per_day**](CampaignGroupApi.md#get_campaign_group_facebook_ad_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-facebook-ad-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group facebook ad report per organisation per campaign per day
[**get_campaign_group_google_ads_report_per_organisation_per_campaign_per_day**](CampaignGroupApi.md#get_campaign_group_google_ads_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-google-ads-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group google ads report per organisation per campaign per day
[**get_campaign_group_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](CampaignGroupApi.md#get_campaign_group_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-linkedin-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group linkedin ads extended report per organisation per account per campaign per day
[**get_campaign_group_report_per_organisation_per_day**](CampaignGroupApi.md#get_campaign_group_report_per_organisation_per_day) | **GET** /data/campaign-group-report-per-organisation-per-day/{organisationUuids} | Return campaign group report per organisation per day
[**get_campaign_group_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](CampaignGroupApi.md#get_campaign_group_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-snapchat-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group snapchat ads extended report per organisation per account per campaign per day
[**get_campaign_group_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](CampaignGroupApi.md#get_campaign_group_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/campaign-group-twitter-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return campaign group twitter ads extended report per organisation per account per campaign per day
[**get_campaign_group_video_report_per_organisation_per_campaign_per_day**](CampaignGroupApi.md#get_campaign_group_video_report_per_organisation_per_campaign_per_day) | **GET** /data/campaign-group-video-report-per-organisation-per-campaign-per-day/{organisationUuids} | Return campaign group video report per organisation per campaign per day
[**get_campaign_group_video_report_per_organisation_per_day**](CampaignGroupApi.md#get_campaign_group_video_report_per_organisation_per_day) | **GET** /data/campaign-group-video-report-per-organisation-per-day/{organisationUuids} | Return campaign group video report per organisation per day


# **get_campaign_group_ad_report_per_organisation_per_campaign_per_day**
> str get_campaign_group_ad_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group ad report per organisation per campaign per day

Campaign group ad report per organisation per campaign per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group ad report per organisation per campaign per day
        api_response = api_instance.get_campaign_group_ad_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_ad_report_per_organisation_per_campaign_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_ad_report_per_organisation_per_day**
> str get_campaign_group_ad_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group ad report per organisation per day

Campaign group ad report per organisation per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group ad report per organisation per day
        api_response = api_instance.get_campaign_group_ad_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_ad_report_per_organisation_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_analytics_report_per_organisation_per_day**
> str get_campaign_group_analytics_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group analytics report per organisation per day

Campaign group analytics report per organisation per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group analytics report per organisation per day
        api_response = api_instance.get_campaign_group_analytics_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_analytics_report_per_organisation_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day**
> str get_campaign_group_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group bing ads extended report per organisation per account per campaign per day

Campaign group bing ads extended report per organisation per account per campaign per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group bing ads extended report per organisation per account per campaign per day
        api_response = api_instance.get_campaign_group_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_facebook_ad_extended_report_per_organisation_per_campaign_per_day**
> str get_campaign_group_facebook_ad_extended_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group facebook ad extended report per organisation per campaign per day

Campaign group facebook ad extended report per organisation per campaign per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group facebook ad extended report per organisation per campaign per day
        api_response = api_instance.get_campaign_group_facebook_ad_extended_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_facebook_ad_extended_report_per_organisation_per_campaign_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_facebook_ad_report_per_organisation_per_campaign_per_day**
> str get_campaign_group_facebook_ad_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group facebook ad report per organisation per campaign per day

Campaign group facebook ad report per organisation  per campaign per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group facebook ad report per organisation per campaign per day
        api_response = api_instance.get_campaign_group_facebook_ad_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_facebook_ad_report_per_organisation_per_campaign_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_google_ads_report_per_organisation_per_campaign_per_day**
> str get_campaign_group_google_ads_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group google ads report per organisation per campaign per day

Campaign group google ads report per organisation  per campaign per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group google ads report per organisation per campaign per day
        api_response = api_instance.get_campaign_group_google_ads_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_google_ads_report_per_organisation_per_campaign_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day**
> str get_campaign_group_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group linkedin ads extended report per organisation per account per campaign per day

Campaign group linkedin ads extended report per organisation per account per campaign per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group linkedin ads extended report per organisation per account per campaign per day
        api_response = api_instance.get_campaign_group_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_report_per_organisation_per_day**
> str get_campaign_group_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group report per organisation per day

Campaign group report per organisation per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group report per organisation per day
        api_response = api_instance.get_campaign_group_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_report_per_organisation_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day**
> str get_campaign_group_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group snapchat ads extended report per organisation per account per campaign per day

Campaign group snapchat ads extended report per organisation per account per campaign per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group snapchat ads extended report per organisation per account per campaign per day
        api_response = api_instance.get_campaign_group_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_snapchat_ads_extended_report_per_organisation_per_account_per_campaign_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day**
> str get_campaign_group_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group twitter ads extended report per organisation per account per campaign per day

Campaign group twitter ads extended report per organisation per account per campaign per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group twitter ads extended report per organisation per account per campaign per day
        api_response = api_instance.get_campaign_group_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_twitter_ads_extended_report_per_organisation_per_account_per_campaign_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_video_report_per_organisation_per_campaign_per_day**
> str get_campaign_group_video_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group video report per organisation per campaign per day

Campaign group video report per organisation per campaign per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group video report per organisation per campaign per day
        api_response = api_instance.get_campaign_group_video_report_per_organisation_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_video_report_per_organisation_per_campaign_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_group_video_report_per_organisation_per_day**
> str get_campaign_group_video_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return campaign group video report per organisation per day

Campaign group video report per organisation per day

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
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
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with cervinodata_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cervinodata_api.CampaignGroupApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return campaign group video report per organisation per day
        api_response = api_instance.get_campaign_group_video_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CampaignGroupApi->get_campaign_group_video_report_per_organisation_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**list[str]**](str.md)| Organisation uuids | 
 **from_date** | **date**| From date | [optional] 
 **date_format** | **str**| Outputted date format | [optional] 
 **format** | **str**| Output format (use csv for large result sets) | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

