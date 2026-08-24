# cervinodata_api.GenericDataApi

All URIs are relative to *https://app.cervinodata.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organisation**](GenericDataApi.md#create_organisation) | **POST** /data/organisations | Create an organisation
[**delete_organisation**](GenericDataApi.md#delete_organisation) | **DELETE** /data/organisations/{organisationUuid} | Delete an organisation
[**get_campaign_groups**](GenericDataApi.md#get_campaign_groups) | **GET** /data/campaign-groups | Return campaign groups
[**get_organisations**](GenericDataApi.md#get_organisations) | **GET** /data/organisations | Return organisations
[**update_organisation**](GenericDataApi.md#update_organisation) | **PUT** /data/organisations/{organisationUuid} | Update an organisation


# **create_organisation**
> object create_organisation(create_organisation_request)

Create an organisation

Create a new organisation

### Example

* Bearer Authentication (bearerAuth):

```python
import cervinodata_api
from cervinodata_api.models.create_organisation_request import CreateOrganisationRequest
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
    api_instance = cervinodata_api.GenericDataApi(api_client)
    create_organisation_request = cervinodata_api.CreateOrganisationRequest() # CreateOrganisationRequest | 

    try:
        # Create an organisation
        api_response = api_instance.create_organisation(create_organisation_request)
        print("The response of GenericDataApi->create_organisation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericDataApi->create_organisation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organisation_request** | [**CreateOrganisationRequest**](CreateOrganisationRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**422** | Validation error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organisation**
> delete_organisation(organisation_uuid)

Delete an organisation

Delete an organisation. Accounts belonging to the organisation are reassigned to the default organisation. The default organisation itself cannot be deleted.

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
    api_instance = cervinodata_api.GenericDataApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid

    try:
        # Delete an organisation
        api_instance.delete_organisation(organisation_uuid)
    except Exception as e:
        print("Exception when calling GenericDataApi->delete_organisation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuid** | **str**| Organisation uuid | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | No access |  -  |
**404** | Organisation uuid not found |  -  |
**422** | Default organisation cannot be deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_campaign_groups**
> List[object] get_campaign_groups()

Return campaign groups

campaign groups

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
    api_instance = cervinodata_api.GenericDataApi(api_client)

    try:
        # Return campaign groups
        api_response = api_instance.get_campaign_groups()
        print("The response of GenericDataApi->get_campaign_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericDataApi->get_campaign_groups: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

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
    api_instance = cervinodata_api.GenericDataApi(api_client)
    format = 'format_example' # str | Output format (optional)

    try:
        # Return organisations
        api_response = api_instance.get_organisations(format=format)
        print("The response of GenericDataApi->get_organisations:\n")
        pprint(api_response)
    except Exception as e:
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

# **update_organisation**
> object update_organisation(organisation_uuid, create_organisation_request)

Update an organisation

Update an existing organisation

### Example

* Bearer Authentication (bearerAuth):

```python
import cervinodata_api
from cervinodata_api.models.create_organisation_request import CreateOrganisationRequest
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
    api_instance = cervinodata_api.GenericDataApi(api_client)
    organisation_uuid = 'organisation_uuid_example' # str | Organisation uuid
    create_organisation_request = cervinodata_api.CreateOrganisationRequest() # CreateOrganisationRequest | 

    try:
        # Update an organisation
        api_response = api_instance.update_organisation(organisation_uuid, create_organisation_request)
        print("The response of GenericDataApi->update_organisation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GenericDataApi->update_organisation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_uuid** | **str**| Organisation uuid | 
 **create_organisation_request** | [**CreateOrganisationRequest**](CreateOrganisationRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**403** | No access |  -  |
**404** | Organisation uuid not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

