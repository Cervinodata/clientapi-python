"""
    Cervinodata API documentation

    <div style='margin: 2em 0;'>  <p>  Before you get going with the Cervinodata API, set up Cervinodata (read the support page here: <a href='https://support.cervinodata.com/hc/en-nl/articles/360004363237' target='_blank'>How to set up the Cervinodata API</a>).  </p> <h3>To use the Cervinodata API, you need all of the following:</h3> <p> <ol> <li>An active Cervinodata account, you can start a free trial <a href='https://app.cervinodata.com/register' target='_blank'>here</a></li> <li>At least one connection to a platform (check <a href='https://app.cervinodata.com/data-sources-connections' target='_blank'>here</a>)</li> <li>At least one account switched ON (check <a href='https://app.cervinodata.com/accounts' target='_blank'>here</a>)</li> <li>At least one data refresh executed (check <a href='https://app.cervinodata.com/manual-data-refresh' target='_blank'>here</a>)</li> <li>An active API token (check <a href='https://app.cervinodata.com/settings#/api' target='_blank'>here</a>)</li> </ol> </p> <p> Note that limits apply for <a href='https://support.cervinodata.com/hc/articles/360014265139' target='_blank'>Free plan users</a>. </p> <p> If you wish to automate your Cervinodata API connection, check out the list of client API's at <a href='https://github.com/Cervinodata' target='_blank'>https://github.com/Cervinodata</a>. </p> </div>  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@cervinodata.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cervinodata_api.api_client import ApiClient, Endpoint as _Endpoint
from cervinodata_api.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class AnalyticsDataGoalsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_analytics_goal_report_per_campaign_per_day_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/data/analytics-goal-report-per-campaign-per-day/{organisationUuid}',
                'operation_id': 'get_analytics_goal_report_per_campaign_per_day',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organisation_uuid',
                    'from_date',
                    'date_format',
                    'format',
                ],
                'required': [
                    'organisation_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                    'date_format',
                    'format',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('date_format',): {

                        "YYYY-MM-DD": "YYYY-MM-DD",
                        "YYYYMMDD": "YYYYMMDD"
                    },
                    ('format',): {

                        "CSV": "csv",
                        "JSON": "json"
                    },
                },
                'openapi_types': {
                    'organisation_uuid':
                        (str,),
                    'from_date':
                        (date,),
                    'date_format':
                        (str,),
                    'format':
                        (str,),
                },
                'attribute_map': {
                    'organisation_uuid': 'organisationUuid',
                    'from_date': 'from_date',
                    'date_format': 'date_format',
                    'format': 'format',
                },
                'location_map': {
                    'organisation_uuid': 'path',
                    'from_date': 'query',
                    'date_format': 'query',
                    'format': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/csv',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_analytics_goal_report_per_channel_group_per_day_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/data/analytics-goal-report-per-channel-group-per-day/{organisationUuid}',
                'operation_id': 'get_analytics_goal_report_per_channel_group_per_day',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organisation_uuid',
                    'from_date',
                    'date_format',
                    'format',
                ],
                'required': [
                    'organisation_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                    'date_format',
                    'format',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('date_format',): {

                        "YYYY-MM-DD": "YYYY-MM-DD",
                        "YYYYMMDD": "YYYYMMDD"
                    },
                    ('format',): {

                        "CSV": "csv",
                        "JSON": "json"
                    },
                },
                'openapi_types': {
                    'organisation_uuid':
                        (str,),
                    'from_date':
                        (date,),
                    'date_format':
                        (str,),
                    'format':
                        (str,),
                },
                'attribute_map': {
                    'organisation_uuid': 'organisationUuid',
                    'from_date': 'from_date',
                    'date_format': 'date_format',
                    'format': 'format',
                },
                'location_map': {
                    'organisation_uuid': 'path',
                    'from_date': 'query',
                    'date_format': 'query',
                    'format': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/csv',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_analytics_goal_report_per_device_per_day_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/data/analytics-goal-report-per-device-per-day/{organisationUuid}',
                'operation_id': 'get_analytics_goal_report_per_device_per_day',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organisation_uuid',
                    'from_date',
                    'date_format',
                    'format',
                ],
                'required': [
                    'organisation_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                    'date_format',
                    'format',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('date_format',): {

                        "YYYY-MM-DD": "YYYY-MM-DD",
                        "YYYYMMDD": "YYYYMMDD"
                    },
                    ('format',): {

                        "CSV": "csv",
                        "JSON": "json"
                    },
                },
                'openapi_types': {
                    'organisation_uuid':
                        (str,),
                    'from_date':
                        (date,),
                    'date_format':
                        (str,),
                    'format':
                        (str,),
                },
                'attribute_map': {
                    'organisation_uuid': 'organisationUuid',
                    'from_date': 'from_date',
                    'date_format': 'date_format',
                    'format': 'format',
                },
                'location_map': {
                    'organisation_uuid': 'path',
                    'from_date': 'query',
                    'date_format': 'query',
                    'format': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/csv',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_analytics_goal_report_per_source_medium_per_day_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'bearerAuth'
                ],
                'endpoint_path': '/data/analytics-goal-report-per-source-medium-per-day/{organisationUuid}',
                'operation_id': 'get_analytics_goal_report_per_source_medium_per_day',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'organisation_uuid',
                    'from_date',
                    'date_format',
                    'format',
                ],
                'required': [
                    'organisation_uuid',
                ],
                'nullable': [
                ],
                'enum': [
                    'date_format',
                    'format',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('date_format',): {

                        "YYYY-MM-DD": "YYYY-MM-DD",
                        "YYYYMMDD": "YYYYMMDD"
                    },
                    ('format',): {

                        "CSV": "csv",
                        "JSON": "json"
                    },
                },
                'openapi_types': {
                    'organisation_uuid':
                        (str,),
                    'from_date':
                        (date,),
                    'date_format':
                        (str,),
                    'format':
                        (str,),
                },
                'attribute_map': {
                    'organisation_uuid': 'organisationUuid',
                    'from_date': 'from_date',
                    'date_format': 'date_format',
                    'format': 'format',
                },
                'location_map': {
                    'organisation_uuid': 'path',
                    'from_date': 'query',
                    'date_format': 'query',
                    'format': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'text/csv',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_analytics_goal_report_per_campaign_per_day(
        self,
        organisation_uuid,
        **kwargs
    ):
        """Return analytics goal report per campaign per day by organisation  # noqa: E501

        Analytics goal report per campaign per day by organisation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_analytics_goal_report_per_campaign_per_day(organisation_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            organisation_uuid (str): Organisation uuid

        Keyword Args:
            from_date (date): From date. [optional]
            date_format (str): Outputted date format. [optional]
            format (str): Output format (use csv for large result sets). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['organisation_uuid'] = \
            organisation_uuid
        return self.get_analytics_goal_report_per_campaign_per_day_endpoint.call_with_http_info(**kwargs)

    def get_analytics_goal_report_per_channel_group_per_day(
        self,
        organisation_uuid,
        **kwargs
    ):
        """Return analytics goal report per channel group per day by organisation  # noqa: E501

        Analytics goal report per channel group per day by organisation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_analytics_goal_report_per_channel_group_per_day(organisation_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            organisation_uuid (str): Organisation uuid

        Keyword Args:
            from_date (date): From date. [optional]
            date_format (str): Outputted date format. [optional]
            format (str): Output format (use csv for large result sets). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['organisation_uuid'] = \
            organisation_uuid
        return self.get_analytics_goal_report_per_channel_group_per_day_endpoint.call_with_http_info(**kwargs)

    def get_analytics_goal_report_per_device_per_day(
        self,
        organisation_uuid,
        **kwargs
    ):
        """Return analytics goal report per device per day by organisation  # noqa: E501

        Analytics goal report per device per day by organisation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_analytics_goal_report_per_device_per_day(organisation_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            organisation_uuid (str): Organisation uuid

        Keyword Args:
            from_date (date): From date. [optional]
            date_format (str): Outputted date format. [optional]
            format (str): Output format (use csv for large result sets). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['organisation_uuid'] = \
            organisation_uuid
        return self.get_analytics_goal_report_per_device_per_day_endpoint.call_with_http_info(**kwargs)

    def get_analytics_goal_report_per_source_medium_per_day(
        self,
        organisation_uuid,
        **kwargs
    ):
        """Return analytics goal report per source medium per day by organisation  # noqa: E501

        Analytics goal report per source medium per day by organisation  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_analytics_goal_report_per_source_medium_per_day(organisation_uuid, async_req=True)
        >>> result = thread.get()

        Args:
            organisation_uuid (str): Organisation uuid

        Keyword Args:
            from_date (date): From date. [optional]
            date_format (str): Outputted date format. [optional]
            format (str): Output format (use csv for large result sets). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            str
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['organisation_uuid'] = \
            organisation_uuid
        return self.get_analytics_goal_report_per_source_medium_per_day_endpoint.call_with_http_info(**kwargs)

