# coding: utf-8

"""
    3DI API

    3DI simulation API   Framework release: 0.0.16   3Di core release: 2.0.2  deployed on:  03:33PM (UTC) on October 29, 2019  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class StatusesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def statuses_list(self, **kwargs):  # noqa: E501
        """Show the latest status off all simulations.  # noqa: E501

        List all simulations that ever have finished successfully  ``` ?name=finished ```  List all simulations that have finished successfully during the week of the 1988 UEFA European Football Championship ``` ?name=finished&created__date__gte=1988-06-10&created__date__lte=1988-06-25 ```  The `created` field is of type date-time in ISO 8601 (UTC) format. To get all crashed simulations since St Nicolas 2018  ``` ?name=crashed&created__gte=2018-12-05T00:00:00Z ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statuses_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str name__contains:
        :param str name__in: Multiple values may be separated by commas.
        :param str name__startswith:
        :param str name__istartswith:
        :param str name__endswith:
        :param str name__regex:
        :param str created:
        :param str created__gt:
        :param str created__gte:
        :param str created__lt:
        :param str created__lte:
        :param str created__date:
        :param str created__date__gt:
        :param str created__date__gte:
        :param str created__date__lt:
        :param str created__date__lte:
        :param float created__year:
        :param float created__year__gt:
        :param float created__year__gte:
        :param float created__year__lt:
        :param float created__year__lte:
        :param float created__month:
        :param float created__month__lte:
        :param float created__day:
        :param float created__day__lt:
        :param float created__week:
        :param float created__week_day:
        :param float id:
        :param float id__range: Multiple values may be separated by commas.
        :param float id__gt:
        :param float id__gte:
        :param float id__lt:
        :param float id__lte:
        :param str id__isnull:
        :param float id__in: Multiple values may be separated by commas.
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: list[SimulationStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.statuses_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.statuses_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def statuses_list_with_http_info(self, **kwargs):  # noqa: E501
        """Show the latest status off all simulations.  # noqa: E501

        List all simulations that ever have finished successfully  ``` ?name=finished ```  List all simulations that have finished successfully during the week of the 1988 UEFA European Football Championship ``` ?name=finished&created__date__gte=1988-06-10&created__date__lte=1988-06-25 ```  The `created` field is of type date-time in ISO 8601 (UTC) format. To get all crashed simulations since St Nicolas 2018  ``` ?name=crashed&created__gte=2018-12-05T00:00:00Z ```  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statuses_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name:
        :param str name__contains:
        :param str name__in: Multiple values may be separated by commas.
        :param str name__startswith:
        :param str name__istartswith:
        :param str name__endswith:
        :param str name__regex:
        :param str created:
        :param str created__gt:
        :param str created__gte:
        :param str created__lt:
        :param str created__lte:
        :param str created__date:
        :param str created__date__gt:
        :param str created__date__gte:
        :param str created__date__lt:
        :param str created__date__lte:
        :param float created__year:
        :param float created__year__gt:
        :param float created__year__gte:
        :param float created__year__lt:
        :param float created__year__lte:
        :param float created__month:
        :param float created__month__lte:
        :param float created__day:
        :param float created__day__lt:
        :param float created__week:
        :param float created__week_day:
        :param float id:
        :param float id__range: Multiple values may be separated by commas.
        :param float id__gt:
        :param float id__gte:
        :param float id__lt:
        :param float id__lte:
        :param str id__isnull:
        :param float id__in: Multiple values may be separated by commas.
        :param int limit: Number of results to return per page.
        :param int offset: The initial index from which to return the results.
        :return: list[SimulationStatus]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['name', 'name__contains', 'name__in', 'name__startswith', 'name__istartswith', 'name__endswith', 'name__regex', 'created', 'created__gt', 'created__gte', 'created__lt', 'created__lte', 'created__date', 'created__date__gt', 'created__date__gte', 'created__date__lt', 'created__date__lte', 'created__year', 'created__year__gt', 'created__year__gte', 'created__year__lt', 'created__year__lte', 'created__month', 'created__month__lte', 'created__day', 'created__day__lt', 'created__week', 'created__week_day', 'id', 'id__range', 'id__gt', 'id__gte', 'id__lt', 'id__lte', 'id__isnull', 'id__in', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method statuses_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'name__contains' in local_var_params:
            query_params.append(('name__contains', local_var_params['name__contains']))  # noqa: E501
        if 'name__in' in local_var_params:
            query_params.append(('name__in', local_var_params['name__in']))  # noqa: E501
        if 'name__startswith' in local_var_params:
            query_params.append(('name__startswith', local_var_params['name__startswith']))  # noqa: E501
        if 'name__istartswith' in local_var_params:
            query_params.append(('name__istartswith', local_var_params['name__istartswith']))  # noqa: E501
        if 'name__endswith' in local_var_params:
            query_params.append(('name__endswith', local_var_params['name__endswith']))  # noqa: E501
        if 'name__regex' in local_var_params:
            query_params.append(('name__regex', local_var_params['name__regex']))  # noqa: E501
        if 'created' in local_var_params:
            query_params.append(('created', local_var_params['created']))  # noqa: E501
        if 'created__gt' in local_var_params:
            query_params.append(('created__gt', local_var_params['created__gt']))  # noqa: E501
        if 'created__gte' in local_var_params:
            query_params.append(('created__gte', local_var_params['created__gte']))  # noqa: E501
        if 'created__lt' in local_var_params:
            query_params.append(('created__lt', local_var_params['created__lt']))  # noqa: E501
        if 'created__lte' in local_var_params:
            query_params.append(('created__lte', local_var_params['created__lte']))  # noqa: E501
        if 'created__date' in local_var_params:
            query_params.append(('created__date', local_var_params['created__date']))  # noqa: E501
        if 'created__date__gt' in local_var_params:
            query_params.append(('created__date__gt', local_var_params['created__date__gt']))  # noqa: E501
        if 'created__date__gte' in local_var_params:
            query_params.append(('created__date__gte', local_var_params['created__date__gte']))  # noqa: E501
        if 'created__date__lt' in local_var_params:
            query_params.append(('created__date__lt', local_var_params['created__date__lt']))  # noqa: E501
        if 'created__date__lte' in local_var_params:
            query_params.append(('created__date__lte', local_var_params['created__date__lte']))  # noqa: E501
        if 'created__year' in local_var_params:
            query_params.append(('created__year', local_var_params['created__year']))  # noqa: E501
        if 'created__year__gt' in local_var_params:
            query_params.append(('created__year__gt', local_var_params['created__year__gt']))  # noqa: E501
        if 'created__year__gte' in local_var_params:
            query_params.append(('created__year__gte', local_var_params['created__year__gte']))  # noqa: E501
        if 'created__year__lt' in local_var_params:
            query_params.append(('created__year__lt', local_var_params['created__year__lt']))  # noqa: E501
        if 'created__year__lte' in local_var_params:
            query_params.append(('created__year__lte', local_var_params['created__year__lte']))  # noqa: E501
        if 'created__month' in local_var_params:
            query_params.append(('created__month', local_var_params['created__month']))  # noqa: E501
        if 'created__month__lte' in local_var_params:
            query_params.append(('created__month__lte', local_var_params['created__month__lte']))  # noqa: E501
        if 'created__day' in local_var_params:
            query_params.append(('created__day', local_var_params['created__day']))  # noqa: E501
        if 'created__day__lt' in local_var_params:
            query_params.append(('created__day__lt', local_var_params['created__day__lt']))  # noqa: E501
        if 'created__week' in local_var_params:
            query_params.append(('created__week', local_var_params['created__week']))  # noqa: E501
        if 'created__week_day' in local_var_params:
            query_params.append(('created__week_day', local_var_params['created__week_day']))  # noqa: E501
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))  # noqa: E501
        if 'id__range' in local_var_params:
            query_params.append(('id__range', local_var_params['id__range']))  # noqa: E501
        if 'id__gt' in local_var_params:
            query_params.append(('id__gt', local_var_params['id__gt']))  # noqa: E501
        if 'id__gte' in local_var_params:
            query_params.append(('id__gte', local_var_params['id__gte']))  # noqa: E501
        if 'id__lt' in local_var_params:
            query_params.append(('id__lt', local_var_params['id__lt']))  # noqa: E501
        if 'id__lte' in local_var_params:
            query_params.append(('id__lte', local_var_params['id__lte']))  # noqa: E501
        if 'id__isnull' in local_var_params:
            query_params.append(('id__isnull', local_var_params['id__isnull']))  # noqa: E501
        if 'id__in' in local_var_params:
            query_params.append(('id__in', local_var_params['id__in']))  # noqa: E501
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
            '/statuses/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SimulationStatus]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def statuses_read(self, id, **kwargs):  # noqa: E501
        """statuses_read  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statuses_read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this simulation status. (required)
        :return: SimulationStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.statuses_read_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.statuses_read_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def statuses_read_with_http_info(self, id, **kwargs):  # noqa: E501
        """statuses_read  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.statuses_read_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: A unique integer value identifying this simulation status. (required)
        :return: SimulationStatus
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
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method statuses_read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in local_var_params or
                local_var_params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `statuses_read`")  # noqa: E501

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
            '/statuses/{id}/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimulationStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
