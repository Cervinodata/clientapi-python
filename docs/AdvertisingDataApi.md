# cervinodata_api.AdvertisingDataApi

All URIs are relative to *https://app.cervinodata.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ad_accounts**](AdvertisingDataApi.md#get_ad_accounts) | **GET** /data/ad-accounts/{organisationUuid} | Return ad accounts by organisation
[**get_ad_campaign_report_per_day**](AdvertisingDataApi.md#get_ad_campaign_report_per_day) | **GET** /data/ad-campaign-report-per-day/{organisationUuid} | Return ad campaign report per day by organisation
[**get_ad_campaign_report_per_organisation_per_account_per_day**](AdvertisingDataApi.md#get_ad_campaign_report_per_organisation_per_account_per_day) | **GET** /data/ad-campaign-report-per-organisation-per-account-per-day/{organisationUuids} | Return ad campaign report per organisation per account per day
[**get_ad_campaigns**](AdvertisingDataApi.md#get_ad_campaigns) | **GET** /data/ad-campaigns/{organisationUuid} | Return ad campaigns by organisation


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
configuration = cervinodata_api.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://app.cervinodata.com/api/v1
configuration.host = "https://app.cervinodata.com/api/v1"
# Create an instance of the API class
api_instance = cervinodata_api.AdvertisingDataApi(cervinodata_api.ApiClient(configuration))
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
configuration = cervinodata_api.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://app.cervinodata.com/api/v1
configuration.host = "https://app.cervinodata.com/api/v1"
# Create an instance of the API class
api_instance = cervinodata_api.AdvertisingDataApi(cervinodata_api.ApiClient(configuration))
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
configuration = cervinodata_api.Configuration()
# Configure Bearer authorization: bearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://app.cervinodata.com/api/v1
configuration.host = "https://app.cervinodata.com/api/v1"
# Create an instance of the API class
api_instance = cervinodata_api.AdvertisingDataApi(cervinodata_api.ApiClient(configuration))
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

