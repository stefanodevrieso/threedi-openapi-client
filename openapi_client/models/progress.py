# coding: utf-8

"""
    3Di API

    3Di simulation API   Framework release: 0.0.19   3Di core release: 2.0.2  deployed on:  03:09PM (UTC) on November 07, 2019  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Progress(object):
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
        'time': 'float',
        'percentage': 'int'
    }

    attribute_map = {
        'time': 'time',
        'percentage': 'percentage'
    }

    def __init__(self, time=None, percentage=None):  # noqa: E501
        """Progress - a model defined in OpenAPI"""  # noqa: E501

        self._time = None
        self._percentage = None
        self.discriminator = None

        self.time = time
        self.percentage = percentage

    @property
    def time(self):
        """Gets the time of this Progress.  # noqa: E501


        :return: The time of this Progress.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Progress.


        :param time: The time of this Progress.  # noqa: E501
        :type: float
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def percentage(self):
        """Gets the percentage of this Progress.  # noqa: E501


        :return: The percentage of this Progress.  # noqa: E501
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this Progress.


        :param percentage: The percentage of this Progress.  # noqa: E501
        :type: int
        """
        if percentage is None:
            raise ValueError("Invalid value for `percentage`, must not be `None`")  # noqa: E501

        self._percentage = percentage

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
        if not isinstance(other, Progress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
