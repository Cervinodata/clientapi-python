# cervinodata_api.GenericDataApi

All URIs are relative to *http://localhost/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_campaign_groups**](GenericDataApi.md#get_campaign_groups) | **GET** /data/campaign-groups | Return campaign groups
[**get_organisations**](GenericDataApi.md#get_organisations) | **GET** /data/organisations | Return organisations


# **get_campaign_groups**
> list[object] get_campaign_groups()

Return campaign groups

campaign groups

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
api_instance = cervinodata_api.GenericDataApi(cervinodata_api.ApiClient(configuration))

try:
    # Return campaign groups
    api_response = api_instance.get_campaign_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericDataApi->get_campaign_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organisations**
> str get_organisations(format=format)

Return organisations

organisations

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
api_instance = cervinodata_api.GenericDataApi(cervinodata_api.ApiClient(configuration))
format = 'format_example' # str | Output format (optional)

try:
    # Return organisations
    api_response = api_instance.get_organisations(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GenericDataApi->get_organisations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

