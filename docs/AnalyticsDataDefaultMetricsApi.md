# cervinodata_api.AnalyticsDataDefaultMetricsApi

All URIs are relative to *https://app.cervinodata.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analytics_report_per_campaign_per_day**](AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_campaign_per_day) | **GET** /data/analytics-report-per-campaign-per-day/{organisationUuid} | Return analytics report per campaign per day by organisation
[**get_analytics_report_per_channel_group_per_day**](AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_channel_group_per_day) | **GET** /data/analytics-report-per-channel-group-per-day/{organisationUuid} | Return analytics report per channel group per day by organisation
[**get_analytics_report_per_device_per_channel_group_per_organisation_per_view_per_day**](AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_device_per_channel_group_per_organisation_per_view_per_day) | **GET** /data/analytics-report-per-device-per-channel-group-per-organisation-per-view-per-day/{organisationUuids} | Return analytics report per device per channel group per organisation per view per day
[**get_analytics_report_per_device_per_day**](AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_device_per_day) | **GET** /data/analytics-report-per-device-per-day/{organisationUuid} | Return analytics report per device per day by organisation
[**get_analytics_report_per_source_medium_per_day**](AnalyticsDataDefaultMetricsApi.md#get_analytics_report_per_source_medium_per_day) | **GET** /data/analytics-report-per-source-medium-per-day/{organisationUuid} | Return analytics report per source medium per day by organisation
[**get_ga4_report_per_device_per_channel_group_per_organisation_per_property_per_day**](AnalyticsDataDefaultMetricsApi.md#get_ga4_report_per_device_per_channel_group_per_organisation_per_property_per_day) | **GET** /data/ga4-report-per-device-per-channel-group-per-organisation-per-property-per-day/{organisationUuids} | Return GA4 report per device per channel group per organisation per property per day


# **get_analytics_report_per_campaign_per_day**
> str get_analytics_report_per_campaign_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return analytics report per campaign per day by organisation

Analytics report per campaign per day by organisation

### Example

* Bearer Authentication (bearerAuth):

```python
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
    api_instance = cervinodata_api.AnalyticsDataDefaultMetricsApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
    from_date = '2013-10-20' # date | From date (optional)
    date_format = 'date_format_example' # str | Outputted date format (optional)
    format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return analytics report per campaign per day by organisation
        api_response = api_instance.get_analytics_report_per_campaign_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
        print("The response of AnalyticsDataDefaultMetricsApi->get_analytics_report_per_campaign_per_day:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataDefaultMetricsApi->get_analytics_report_per_campaign_per_day: %s\n" % e)
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

# **get_analytics_report_per_channel_group_per_day**
> str get_analytics_report_per_channel_group_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return analytics report per channel group per day by organisation

Analytics report per channel group per day by organisation

### Example

* Bearer Authentication (bearerAuth):

```python
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
    api_instance = cervinodata_api.AnalyticsDataDefaultMetricsApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
    from_date = '2013-10-20' # date | From date (optional)
    date_format = 'date_format_example' # str | Outputted date format (optional)
    format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return analytics report per channel group per day by organisation
        api_response = api_instance.get_analytics_report_per_channel_group_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
        print("The response of AnalyticsDataDefaultMetricsApi->get_analytics_report_per_channel_group_per_day:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataDefaultMetricsApi->get_analytics_report_per_channel_group_per_day: %s\n" % e)
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

# **get_analytics_report_per_device_per_channel_group_per_organisation_per_view_per_day**
> str get_analytics_report_per_device_per_channel_group_per_organisation_per_view_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return analytics report per device per channel group per organisation per view per day

Analytics report per device per channel group per organisation per view per day

### Example

* Bearer Authentication (bearerAuth):

```python
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
    api_instance = cervinodata_api.AnalyticsDataDefaultMetricsApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # List[str] | Organisation uuids
    from_date = '2013-10-20' # date | From date (optional)
    date_format = 'date_format_example' # str | Outputted date format (optional)
    format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return analytics report per device per channel group per organisation per view per day
        api_response = api_instance.get_analytics_report_per_device_per_channel_group_per_organisation_per_view_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        print("The response of AnalyticsDataDefaultMetricsApi->get_analytics_report_per_device_per_channel_group_per_organisation_per_view_per_day:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataDefaultMetricsApi->get_analytics_report_per_device_per_channel_group_per_organisation_per_view_per_day: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**List[str]**](str.md)| Organisation uuids | 
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

# **get_analytics_report_per_device_per_day**
> str get_analytics_report_per_device_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return analytics report per device per day by organisation

Analytics report per device per day by organisation

### Example

* Bearer Authentication (bearerAuth):

```python
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
    api_instance = cervinodata_api.AnalyticsDataDefaultMetricsApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
    from_date = '2013-10-20' # date | From date (optional)
    date_format = 'date_format_example' # str | Outputted date format (optional)
    format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return analytics report per device per day by organisation
        api_response = api_instance.get_analytics_report_per_device_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
        print("The response of AnalyticsDataDefaultMetricsApi->get_analytics_report_per_device_per_day:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataDefaultMetricsApi->get_analytics_report_per_device_per_day: %s\n" % e)
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

# **get_analytics_report_per_source_medium_per_day**
> str get_analytics_report_per_source_medium_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return analytics report per source medium per day by organisation

Analytics report per source medium per day by organisation

### Example

* Bearer Authentication (bearerAuth):

```python
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
    api_instance = cervinodata_api.AnalyticsDataDefaultMetricsApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
    from_date = '2013-10-20' # date | From date (optional)
    date_format = 'date_format_example' # str | Outputted date format (optional)
    format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return analytics report per source medium per day by organisation
        api_response = api_instance.get_analytics_report_per_source_medium_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
        print("The response of AnalyticsDataDefaultMetricsApi->get_analytics_report_per_source_medium_per_day:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataDefaultMetricsApi->get_analytics_report_per_source_medium_per_day: %s\n" % e)
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

# **get_ga4_report_per_device_per_channel_group_per_organisation_per_property_per_day**
> str get_ga4_report_per_device_per_channel_group_per_organisation_per_property_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)

Return GA4 report per device per channel group per organisation per property per day

GA4 report per device per channel group per organisation per property per day

### Example

* Bearer Authentication (bearerAuth):

```python
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
    api_instance = cervinodata_api.AnalyticsDataDefaultMetricsApi(api_client)
    organisation_uuids = ['organisation_uuids_example'] # List[str] | Organisation uuids
    from_date = '2013-10-20' # date | From date (optional)
    date_format = 'date_format_example' # str | Outputted date format (optional)
    format = 'format_example' # str | Output format (use csv for large result sets) (optional)

    try:
        # Return GA4 report per device per channel group per organisation per property per day
        api_response = api_instance.get_ga4_report_per_device_per_channel_group_per_organisation_per_property_per_day(organisation_uuids, from_date=from_date, date_format=date_format, format=format)
        print("The response of AnalyticsDataDefaultMetricsApi->get_ga4_report_per_device_per_channel_group_per_organisation_per_property_per_day:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsDataDefaultMetricsApi->get_ga4_report_per_device_per_channel_group_per_organisation_per_property_per_day: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuids** | [**List[str]**](str.md)| Organisation uuids | 
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

