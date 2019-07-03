# coding: utf-8

"""
    3DI API

    3DI simulation API  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class InitialFlowStateOverview(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'flow_state': 'FlowStateOverview'
    }

    attribute_map = {
        'url': 'url',
        'flow_state': 'flow_state'
    }

    def __init__(self, url=None, flow_state=None):  # noqa: E501
        """InitialFlowStateOverview - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._flow_state = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if flow_state is not None:
            self.flow_state = flow_state

    @property
    def url(self):
        """Gets the url of this InitialFlowStateOverview.  # noqa: E501


        :return: The url of this InitialFlowStateOverview.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InitialFlowStateOverview.


        :param url: The url of this InitialFlowStateOverview.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def flow_state(self):
        """Gets the flow_state of this InitialFlowStateOverview.  # noqa: E501


        :return: The flow_state of this InitialFlowStateOverview.  # noqa: E501
        :rtype: FlowStateOverview
        """
        return self._flow_state

    @flow_state.setter
    def flow_state(self, flow_state):
        """Sets the flow_state of this InitialFlowStateOverview.


        :param flow_state: The flow_state of this InitialFlowStateOverview.  # noqa: E501
        :type: FlowStateOverview
        """

        self._flow_state = flow_state

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InitialFlowStateOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other