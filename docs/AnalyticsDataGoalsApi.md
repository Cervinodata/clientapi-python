# cervinodata_api.AnalyticsDataGoalsApi

All URIs are relative to *https://app.cervinodata.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analytics_goal_report_per_campaign_per_day**](AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_campaign_per_day) | **GET** /data/analytics-goal-report-per-campaign-per-day/{organisationUuid} | Return analytics goal report per campaign per day by organisation
[**get_analytics_goal_report_per_channel_group_per_day**](AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_channel_group_per_day) | **GET** /data/analytics-goal-report-per-channel-group-per-day/{organisationUuid} | Return analytics goal report per channel group per day by organisation
[**get_analytics_goal_report_per_device_per_channel_group_per_day**](AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_device_per_channel_group_per_day) | **GET** /data/analytics-goal-report-per-device-per-channel-group-per-day/{organisationUuid} | Return analytics goal report per device per channel group per day by organisation
[**get_analytics_goal_report_per_device_per_day**](AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_device_per_day) | **GET** /data/analytics-goal-report-per-device-per-day/{organisationUuid} | Return analytics goal report per device per day by organisation
[**get_analytics_goal_report_per_source_medium_per_day**](AnalyticsDataGoalsApi.md#get_analytics_goal_report_per_source_medium_per_day) | **GET** /data/analytics-goal-report-per-source-medium-per-day/{organisationUuid} | Return analytics goal report per source medium per day by organisation


# **get_analytics_goal_report_per_campaign_per_day**
> str get_analytics_goal_report_per_campaign_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return analytics goal report per campaign per day by organisation

Analytics goal report per campaign per day by organisation

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
api_instance = cervinodata_api.AnalyticsDataGoalsApi(cervinodata_api.ApiClient(configuration))
organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

try:
    # Return analytics goal report per campaign per day by organisation
    api_response = api_instance.get_analytics_goal_report_per_campaign_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsDataGoalsApi->get_analytics_goal_report_per_campaign_per_day: %s\n" % e)
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

# **get_analytics_goal_report_per_channel_group_per_day**
> str get_analytics_goal_report_per_channel_group_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return analytics goal report per channel group per day by organisation

Analytics goal report per channel group per day by organisation

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
api_instance = cervinodata_api.AnalyticsDataGoalsApi(cervinodata_api.ApiClient(configuration))
organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

try:
    # Return analytics goal report per channel group per day by organisation
    api_response = api_instance.get_analytics_goal_report_per_channel_group_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsDataGoalsApi->get_analytics_goal_report_per_channel_group_per_day: %s\n" % e)
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

# **get_analytics_goal_report_per_device_per_channel_group_per_day**
> str get_analytics_goal_report_per_device_per_channel_group_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return analytics goal report per device per channel group per day by organisation

Analytics goal report per device per channel group per day by organisation

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
api_instance = cervinodata_api.AnalyticsDataGoalsApi(cervinodata_api.ApiClient(configuration))
organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

try:
    # Return analytics goal report per device per channel group per day by organisation
    api_response = api_instance.get_analytics_goal_report_per_device_per_channel_group_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsDataGoalsApi->get_analytics_goal_report_per_device_per_channel_group_per_day: %s\n" % e)
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

# **get_analytics_goal_report_per_device_per_day**
> str get_analytics_goal_report_per_device_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return analytics goal report per device per day by organisation

Analytics goal report per device per day by organisation

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
api_instance = cervinodata_api.AnalyticsDataGoalsApi(cervinodata_api.ApiClient(configuration))
organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

try:
    # Return analytics goal report per device per day by organisation
    api_response = api_instance.get_analytics_goal_report_per_device_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsDataGoalsApi->get_analytics_goal_report_per_device_per_day: %s\n" % e)
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

# **get_analytics_goal_report_per_source_medium_per_day**
> str get_analytics_goal_report_per_source_medium_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)

Return analytics goal report per source medium per day by organisation

Analytics goal report per source medium per day by organisation

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
api_instance = cervinodata_api.AnalyticsDataGoalsApi(cervinodata_api.ApiClient(configuration))
organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
from_date = '2013-10-20' # date | From date (optional)
date_format = 'date_format_example' # str | Outputted date format (optional)
format = 'format_example' # str | Output format (use csv for large result sets) (optional)

try:
    # Return analytics goal report per source medium per day by organisation
    api_response = api_instance.get_analytics_goal_report_per_source_medium_per_day(organisation_uuid, from_date=from_date, date_format=date_format, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsDataGoalsApi->get_analytics_goal_report_per_source_medium_per_day: %s\n" % e)
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

