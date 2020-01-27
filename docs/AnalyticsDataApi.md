# cervinodata_api.AnalyticsDataApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_views**](AnalyticsDataApi.md#get_views) | **GET** /data/views/{organisationUuid} | Return views by organisation


# **get_views**
> str get_views(organisation_uuid, format=format)

Return views by organisation

Views by organisation

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

# Defining host is optional and default to http://localhost/api/v1
configuration.host = "http://localhost/api/v1"
# Create an instance of the API class
api_instance = cervinodata_api.AnalyticsDataApi(cervinodata_api.ApiClient(configuration))
organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
format = 'format_example' # str | Output format (optional)

try:
    # Return views by organisation
    api_response = api_instance.get_views(organisation_uuid, format=format)
    pprint(api_response)
except ApiException as e:
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

