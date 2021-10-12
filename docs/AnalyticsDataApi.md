# cervinodata_api.AnalyticsDataApi

All URIs are relative to *https://app.cervinodata.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_views**](AnalyticsDataApi.md#get_views) | **GET** /data/views/{organisationUuid} | Return views by organisation


# **get_views**
> str get_views(organisation_uuid)

Return views by organisation

Views by organisation

### Example

* Bearer Authentication (bearerAuth):

```python
import time
import cervinodata_api
from cervinodata_api.api import analytics_data_api
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
    api_instance = analytics_data_api.AnalyticsDataApi(api_client)
    organisation_uuid = "organisationUuid_example" # str | Organisation uuid
    format = "csv" # str | Output format (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return views by organisation
        api_response = api_instance.get_views(organisation_uuid)
        pprint(api_response)
    except cervinodata_api.ApiException as e:
        print("Exception when calling AnalyticsDataApi->get_views: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return views by organisation
        api_response = api_instance.get_views(organisation_uuid, format=format)
        pprint(api_response)
    except cervinodata_api.ApiException as e:
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

