# cervinodata_api.AdvertisingDataApi

All URIs are relative to *https://app.cervinodata.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ad_account_report_per_organisation_per_day**](AdvertisingDataApi.md#get_ad_account_report_per_organisation_per_day) | **GET** /data/ad-account-report-per-organisation-per-day/{organisationUuids} | Return ad account report per organisation per day
[**get_ad_accounts**](AdvertisingDataApi.md#get_ad_accounts) | **GET** /data/ad-accounts/{organisationUuid} | Return ad accounts by organisation
[**get_ad_campaign_report_per_day**](AdvertisingDataApi.md#get_ad_campaign_report_per_day) | **GET** /data/ad-campaign-report-per-day/{organisationUuid} | Return ad campaign report per day by organisation
[**get_ad_campaign_report_per_organisation_per_account_per_campaign_per_device_per_day**](AdvertisingDataApi.md#get_ad_campaign_report_per_organisation_per_account_per_campaign_per_device_per_day) | **GET** /data/ad-campaign-report-per-organisation-per-account-per-campaign-per-device-per-day/{organisationUuids} | Return ad campaign report per organisation per account per campaign per device per day
[**get_ad_campaign_report_per_organisation_per_account_per_day**](AdvertisingDataApi.md#get_ad_campaign_report_per_organisation_per_account_per_day) | **GET** /data/ad-campaign-report-per-organisation-per-account-per-day/{organisationUuids} | Return ad campaign report per organisation per account per day
[**get_ad_campaigns**](AdvertisingDataApi.md#get_ad_campaigns) | **GET** /data/ad-campaigns/{organisationUuid} | Return ad campaigns by organisation
[**get_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](AdvertisingDataApi.md#get_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/bing-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return bing ads extended report per organisation per account per campaign per day
[**get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_device_per_day**](AdvertisingDataApi.md#get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_device_per_day) | **GET** /data/facebook-ad-extended-report-per-organisation-per-account-per-campaign-per-device-per-day/{organisationUuids} | Return facebook ad extended report per organisation per account per campaign per device per day
[**get_google_ads_report_per_organisation_per_account_per_campaign_per_device_per_day**](AdvertisingDataApi.md#get_google_ads_report_per_organisation_per_account_per_campaign_per_device_per_day) | **GET** /data/google-ads-report-per-organisation-per-account-per-campaign-per-device-per-day/{organisationUuids} | Return google ads report per organisation per account per campaign per device per day
[**get_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day**](AdvertisingDataApi.md#get_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day) | **GET** /data/linkedin-ads-extended-report-per-organisation-per-account-per-campaign-per-day/{organisationUuids} | Return linkedin ads extended report per organisation per account per campaign per day


# **get_ad_account_report_per_organisation_per_day**
> str get_ad_account_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return ad account report per organisation per day

Ad account report per organisation  per day

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return ad account report per organisation per day
        api_response = api_instance.get_ad_account_report_per_organisation_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_ad_account_report_per_organisation_per_day: %s\n" % e)
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

# **get_ad_accounts**
> str get_ad_accounts(organisation_uuid, format=format)

Return ad accounts by organisation

Ad accounts by organisation

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
format = 'format_example' # str | Output format (optional)

    try:
        # Return ad accounts by organisation
        api_response = api_instance.get_ad_accounts(organisation_uuid, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_ad_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuid** | **str**| Organisation uuid | 
 **format** | **str**| Output format | [optional] 

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
**400** | Invalid Organisation uuid supplied |  -  |
**404** | Organisation uuid not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_campaign_report_per_day**
> str get_ad_campaign_report_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return ad campaign report per day by organisation

Ad campaign report per day by organisation

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return ad campaign report per day by organisation
        api_response = api_instance.get_ad_campaign_report_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_ad_campaign_report_per_day: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuid** | **str**| Organisation uuid | 
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
**400** | Invalid Organisation uuid supplied |  -  |
**404** | Organisation uuid not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ad_campaign_report_per_organisation_per_account_per_campaign_per_device_per_day**
> str get_ad_campaign_report_per_organisation_per_account_per_campaign_per_device_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return ad campaign report per organisation per account per campaign per device per day

Ad campaign report per organisation per account per campaign per device per day

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return ad campaign report per organisation per account per campaign per device per day
        api_response = api_instance.get_ad_campaign_report_per_organisation_per_account_per_campaign_per_device_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_ad_campaign_report_per_organisation_per_account_per_campaign_per_device_per_day: %s\n" % e)
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

# **get_ad_campaign_report_per_organisation_per_account_per_day**
> str get_ad_campaign_report_per_organisation_per_account_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return ad campaign report per organisation per account per day

Ad campaign report per organisation per account per day

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return ad campaign report per organisation per account per day
        api_response = api_instance.get_ad_campaign_report_per_organisation_per_account_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_ad_campaign_report_per_organisation_per_account_per_day: %s\n" % e)
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

# **get_ad_campaigns**
> str get_ad_campaigns(organisation_uuid, from_date=from_date, format=format)

Return ad campaigns by organisation

Ad campaigns by organisation

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
from_date = '2013-10-20' # date | From date (optional)
format = 'format_example' # str | Output format (optional)

    try:
        # Return ad campaigns by organisation
        api_response = api_instance.get_ad_campaigns(organisation_uuid, from_date=from_date, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_ad_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuid** | **str**| Organisation uuid | 
 **from_date** | **date**| From date | [optional] 
 **format** | **str**| Output format | [optional] 

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
**400** | Invalid Organisation uuid supplied |  -  |
**404** | Organisation uuid not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day**
> str get_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return bing ads extended report per organisation per account per campaign per day

Bing ads extended report per organisation per account per campaign per day

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return bing ads extended report per organisation per account per campaign per day
        api_response = api_instance.get_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_bing_ads_extended_report_per_organisation_per_account_per_campaign_per_day: %s\n" % e)
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

# **get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_device_per_day**
> str get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_device_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return facebook ad extended report per organisation per account per campaign per device per day

Facebook ad extended report per organisation per account per campaign per device per day

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return facebook ad extended report per organisation per account per campaign per device per day
        api_response = api_instance.get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_device_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_facebook_ad_extended_report_per_organisation_per_account_per_campaign_per_device_per_day: %s\n" % e)
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

# **get_google_ads_report_per_organisation_per_account_per_campaign_per_device_per_day**
> str get_google_ads_report_per_organisation_per_account_per_campaign_per_device_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return google ads report per organisation per account per campaign per device per day

Campaign group google ads report per organisation per account per campaign per device per day

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return google ads report per organisation per account per campaign per device per day
        api_response = api_instance.get_google_ads_report_per_organisation_per_account_per_campaign_per_device_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_google_ads_report_per_organisation_per_account_per_campaign_per_device_per_day: %s\n" % e)
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

# **get_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day**
> str get_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return linkedin ads extended report per organisation per account per campaign per day

Linkedin ads extended report per organisation per account per campaign per day

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
    api_instance = cervinodata_api.AdvertisingDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # list[str] | Organisation uuids
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return linkedin ads extended report per organisation per account per campaign per day
        api_response = api_instance.get_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdvertisingDataApi->get_linked_in_ads_extended_report_per_organisation_per_account_per_campaign_per_day: %s\n" % e)
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

