# cervinodata_api.AnalyticsDataApi

All URIs are relative to *https://app.cervinodata.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ga4_report_per_channel_group_per_organisation_per_property**](AnalyticsDataApi.md#get_ga4_report_per_channel_group_per_organisation_per_property) | **GET** /data/ga4-report-per-channel-group-per-organisation-per-property/{organisationUuids} | Return GA4 report per channel group per organisation per property
[**get_ga4_report_per_channel_group_per_organisation_per_property_per_month**](AnalyticsDataApi.md#get_ga4_report_per_channel_group_per_organisation_per_property_per_month) | **GET** /data/ga4-report-per-channel-group-per-organisation-per-property-per-month/{organisationUuids} | Return GA4 report per channel group per organisation per property per month
[**get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month**](AnalyticsDataApi.md#get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month) | **GET** /data/ga4-report-per-channel-group-per-product-name-per-organisation-per-property-per-month/{organisationUuids} | Return GA4 report per channel group per product name per organisation per property per month
[**get_ga4_report_per_channel_group_per_source_medium_per_organisation_per_property_per_month**](AnalyticsDataApi.md#get_ga4_report_per_channel_group_per_source_medium_per_organisation_per_property_per_month) | **GET** /data/ga4-report-per-channel-group-per-source-medium-per-organisation-per-property-per-month/{organisationUuids} | Return GA4 report per channel group per source medium per organisation per property per month
[**get_views**](AnalyticsDataApi.md#get_views) | **GET** /data/views/{organisationUuid} | Return views by organisation


# **get_ga4_report_per_channel_group_per_organisation_per_property**
> str get_ga4_report_per_channel_group_per_organisation_per_property(organisation_uuids)

Return GA4 report per channel group per organisation per property

GA4 report per channel group per organisation per property

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
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
    api_instance = cervinodata_api.AnalyticsDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # List[str] | Organisation uuids

    try:
        # Return GA4 report per channel group per organisation per property
        api_response = api_instance.get_ga4_report_per_channel_group_per_organisation_per_property(organisation_uuids)
        print("The response of AnalyticsDataApi->get_ga4_report_per_channel_group_per_organisation_per_property:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataApi->get_ga4_report_per_channel_group_per_organisation_per_property: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**List[str]**](str.md)| Organisation uuids | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ga4_report_per_channel_group_per_organisation_per_property_per_month**
> str get_ga4_report_per_channel_group_per_organisation_per_property_per_month(organisation_uuids)

Return GA4 report per channel group per organisation per property per month

GA4 report per channel group per organisation per property per month

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
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
    api_instance = cervinodata_api.AnalyticsDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # List[str] | Organisation uuids

    try:
        # Return GA4 report per channel group per organisation per property per month
        api_response = api_instance.get_ga4_report_per_channel_group_per_organisation_per_property_per_month(organisation_uuids)
        print("The response of AnalyticsDataApi->get_ga4_report_per_channel_group_per_organisation_per_property_per_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataApi->get_ga4_report_per_channel_group_per_organisation_per_property_per_month: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**List[str]**](str.md)| Organisation uuids | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month**
> str get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month(organisation_uuids)

Return GA4 report per channel group per product name per organisation per property per month

GA4 report per channel group per product name per organisation per property per month

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
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
    api_instance = cervinodata_api.AnalyticsDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # List[str] | Organisation uuids

    try:
        # Return GA4 report per channel group per product name per organisation per property per month
        api_response = api_instance.get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month(organisation_uuids)
        print("The response of AnalyticsDataApi->get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataApi->get_ga4_report_per_channel_group_per_product_name_per_organisation_per_property_per_month: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**List[str]**](str.md)| Organisation uuids | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ga4_report_per_channel_group_per_source_medium_per_organisation_per_property_per_month**
> str get_ga4_report_per_channel_group_per_source_medium_per_organisation_per_property_per_month(organisation_uuids)

Return GA4 report per channel group per source medium per organisation per property per month

GA4 report per channel group per source medium per organisation per property per month

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
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
    api_instance = cervinodata_api.AnalyticsDataApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # List[str] | Organisation uuids

    try:
        # Return GA4 report per channel group per source medium per organisation per property per month
        api_response = api_instance.get_ga4_report_per_channel_group_per_source_medium_per_organisation_per_property_per_month(organisation_uuids)
        print("The response of AnalyticsDataApi->get_ga4_report_per_channel_group_per_source_medium_per_organisation_per_property_per_month:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataApi->get_ga4_report_per_channel_group_per_source_medium_per_organisation_per_property_per_month: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**List[str]**](str.md)| Organisation uuids | 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Invalid Organisation uuids supplied |  -  |
**404** | Organisation uuids not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_views**
> str get_views(organisation_uuid, format=format)

Return views by organisation

Views by organisation

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import os
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
    api_instance = cervinodata_api.AnalyticsDataApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
    format = 'format_example' # str | Output format (optional)

    try:
        # Return views by organisation
        api_response = api_instance.get_views(organisation_uuid, format=format)
        print("The response of AnalyticsDataApi->get_views:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataApi->get_views: %s\n" % e)
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

