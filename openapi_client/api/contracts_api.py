# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 0.0.52   3Di core release: 2.0.9  deployed on:  13:20PM (UTC) on May 22, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ContractsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def contracts_create(self, data, **kwargs):  # noqa: E501
        """contracts_create  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_create(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Contract data: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Contract
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.contracts_create_with_http_info(data, **kwargs)  # noqa: E501

    def contracts_create_with_http_info(self, data, **kwargs):  # noqa: E501
        """contracts_create  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_create_with_http_info(data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Contract data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Contract, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contracts_create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'data' is set
        if ('data' not in local_var_params or
                local_var_params['data'] is None):
            raise ApiValueError("Missing the required parameter `data` when calling `contracts_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/contracts/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contract',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def contracts_delete(self, id, **kwargs):  # noqa: E501
        """contracts_delete  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this contract. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.contracts_delete_with_http_info(id, **kwargs)  # noqa: E501

    def contracts_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """contracts_delete  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this contract. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contracts_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `contracts_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/contracts/{id}/', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def contracts_list(self, **kwargs):  # noqa: E501
        """contracts_list  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float organisation__id:
        :param float organisation__id__range: Multiple values may be separated by commas.
        :param float organisation__id__gt:
        :param float organisation__id__gte:
        :param float organisation__id__lt:
        :param float organisation__id__lte:
        :param str organisation__id__isnull:
        :param str organisation__name:
        :param str organisation__name__contains:
        :param str organisation__name__icontains:
        :param str organisation__name__in: Multiple values may be separated by commas.
        :param str organisation__name__startswith:
        :param str organisation__name__istartswith:
        :param str organisation__name__endswith:
        :param str organisation__name__regex:
        :param str organisation__unique_id:
        :param str organisation__unique_id__contains:
        :param str organisation__unique_id__icontains:
        :param str organisation__unique_id__in: Multiple values may be separated by commas.
        :param str organisation__unique_id__startswith:
        :param str organisation__unique_id__istartswith:
        :param str organisation__unique_id__endswith:
        :param str organisation__unique_id__regex:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.contracts_list_with_http_info(**kwargs)  # noqa: E501

    def contracts_list_with_http_info(self, **kwargs):  # noqa: E501
        """contracts_list  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param float organisation__id:
        :param float organisation__id__range: Multiple values may be separated by commas.
        :param float organisation__id__gt:
        :param float organisation__id__gte:
        :param float organisation__id__lt:
        :param float organisation__id__lte:
        :param str organisation__id__isnull:
        :param str organisation__name:
        :param str organisation__name__contains:
        :param str organisation__name__icontains:
        :param str organisation__name__in: Multiple values may be separated by commas.
        :param str organisation__name__startswith:
        :param str organisation__name__istartswith:
        :param str organisation__name__endswith:
        :param str organisation__name__regex:
        :param str organisation__unique_id:
        :param str organisation__unique_id__contains:
        :param str organisation__unique_id__icontains:
        :param str organisation__unique_id__in: Multiple values may be separated by commas.
        :param str organisation__unique_id__startswith:
        :param str organisation__unique_id__istartswith:
        :param str organisation__unique_id__endswith:
        :param str organisation__unique_id__regex:
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse2001, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['organisation__id', 'organisation__id__range', 'organisation__id__gt', 'organisation__id__gte', 'organisation__id__lt', 'organisation__id__lte', 'organisation__id__isnull', 'organisation__name', 'organisation__name__contains', 'organisation__name__icontains', 'organisation__name__in', 'organisation__name__startswith', 'organisation__name__istartswith', 'organisation__name__endswith', 'organisation__name__regex', 'organisation__unique_id', 'organisation__unique_id__contains', 'organisation__unique_id__icontains', 'organisation__unique_id__in', 'organisation__unique_id__startswith', 'organisation__unique_id__istartswith', 'organisation__unique_id__endswith', 'organisation__unique_id__regex', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contracts_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'organisation__id' in local_var_params:
            query_params.append(('organisation__id', local_var_params['organisation__id']))  # noqa: E501
        if 'organisation__id__range' in local_var_params:
            query_params.append(('organisation__id__range', local_var_params['organisation__id__range']))  # noqa: E501
        if 'organisation__id__gt' in local_var_params:
            query_params.append(('organisation__id__gt', local_var_params['organisation__id__gt']))  # noqa: E501
        if 'organisation__id__gte' in local_var_params:
            query_params.append(('organisation__id__gte', local_var_params['organisation__id__gte']))  # noqa: E501
        if 'organisation__id__lt' in local_var_params:
            query_params.append(('organisation__id__lt', local_var_params['organisation__id__lt']))  # noqa: E501
        if 'organisation__id__lte' in local_var_params:
            query_params.append(('organisation__id__lte', local_var_params['organisation__id__lte']))  # noqa: E501
        if 'organisation__id__isnull' in local_var_params:
            query_params.append(('organisation__id__isnull', local_var_params['organisation__id__isnull']))  # noqa: E501
        if 'organisation__name' in local_var_params:
            query_params.append(('organisation__name', local_var_params['organisation__name']))  # noqa: E501
        if 'organisation__name__contains' in local_var_params:
            query_params.append(('organisation__name__contains', local_var_params['organisation__name__contains']))  # noqa: E501
        if 'organisation__name__icontains' in local_var_params:
            query_params.append(('organisation__name__icontains', local_var_params['organisation__name__icontains']))  # noqa: E501
        if 'organisation__name__in' in local_var_params:
            query_params.append(('organisation__name__in', local_var_params['organisation__name__in']))  # noqa: E501
        if 'organisation__name__startswith' in local_var_params:
            query_params.append(('organisation__name__startswith', local_var_params['organisation__name__startswith']))  # noqa: E501
        if 'organisation__name__istartswith' in local_var_params:
            query_params.append(('organisation__name__istartswith', local_var_params['organisation__name__istartswith']))  # noqa: E501
        if 'organisation__name__endswith' in local_var_params:
            query_params.append(('organisation__name__endswith', local_var_params['organisation__name__endswith']))  # noqa: E501
        if 'organisation__name__regex' in local_var_params:
            query_params.append(('organisation__name__regex', local_var_params['organisation__name__regex']))  # noqa: E501
        if 'organisation__unique_id' in local_var_params:
            query_params.append(('organisation__unique_id', local_var_params['organisation__unique_id']))  # noqa: E501
        if 'organisation__unique_id__contains' in local_var_params:
            query_params.append(('organisation__unique_id__contains', local_var_params['organisation__unique_id__contains']))  # noqa: E501
        if 'organisation__unique_id__icontains' in local_var_params:
            query_params.append(('organisation__unique_id__icontains', local_var_params['organisation__unique_id__icontains']))  # noqa: E501
        if 'organisation__unique_id__in' in local_var_params:
            query_params.append(('organisation__unique_id__in', local_var_params['organisation__unique_id__in']))  # noqa: E501
        if 'organisation__unique_id__startswith' in local_var_params:
            query_params.append(('organisation__unique_id__startswith', local_var_params['organisation__unique_id__startswith']))  # noqa: E501
        if 'organisation__unique_id__istartswith' in local_var_params:
            query_params.append(('organisation__unique_id__istartswith', local_var_params['organisation__unique_id__istartswith']))  # noqa: E501
        if 'organisation__unique_id__endswith' in local_var_params:
            query_params.append(('organisation__unique_id__endswith', local_var_params['organisation__unique_id__endswith']))  # noqa: E501
        if 'organisation__unique_id__regex' in local_var_params:
            query_params.append(('organisation__unique_id__regex', local_var_params['organisation__unique_id__regex']))  # noqa: E501
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/contracts/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2001',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def contracts_partial_update(self, id, data, **kwargs):  # noqa: E501
        """contracts_partial_update  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_partial_update(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this contract. (required)
        :param Contract data: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Contract
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.contracts_partial_update_with_http_info(id, data, **kwargs)  # noqa: E501

    def contracts_partial_update_with_http_info(self, id, data, **kwargs):  # noqa: E501
        """contracts_partial_update  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_partial_update_with_http_info(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this contract. (required)
        :param Contract data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Contract, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contracts_partial_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `contracts_partial_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in local_var_params or
                local_var_params['data'] is None):
            raise ApiValueError("Missing the required parameter `data` when calling `contracts_partial_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/contracts/{id}/', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contract',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def contracts_read(self, id, **kwargs):  # noqa: E501
        """contracts_read  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this contract. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Contract
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.contracts_read_with_http_info(id, **kwargs)  # noqa: E501

    def contracts_read_with_http_info(self, id, **kwargs):  # noqa: E501
        """contracts_read  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_read_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this contract. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Contract, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contracts_read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `contracts_read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/contracts/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contract',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def contracts_update(self, id, data, **kwargs):  # noqa: E501
        """contracts_update  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_update(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this contract. (required)
        :param Contract data: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Contract
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.contracts_update_with_http_info(id, data, **kwargs)  # noqa: E501

    def contracts_update_with_http_info(self, id, data, **kwargs):  # noqa: E501
        """contracts_update  # noqa: E501

        API endpoint for interacting with contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.contracts_update_with_http_info(id, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int id: A unique integer value identifying this contract. (required)
        :param Contract data: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Contract, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['id', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method contracts_update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ApiValueError("Missing the required parameter `id` when calling `contracts_update`")  # noqa: E501
        # verify the required parameter 'data' is set
        if ('data' not in local_var_params or
                local_var_params['data'] is None):
            raise ApiValueError("Missing the required parameter `data` when calling `contracts_update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in local_var_params:
            body_params = local_var_params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/contracts/{id}/', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Contract',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
