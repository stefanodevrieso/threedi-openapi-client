# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 1.0.5   3Di core release: 2.0.9  deployed on:  10:00AM (UTC) on June 9, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Result(object):
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
        'basic': 'bool',
        'damage_estimation': 'bool',
        'arrival_time': 'bool'
    }

    attribute_map = {
        'basic': 'basic',
        'damage_estimation': 'damage_estimation',
        'arrival_time': 'arrival_time'
    }

    def __init__(self, basic=None, damage_estimation=None, arrival_time=None):  # noqa: E501
        """Result - a model defined in OpenAPI"""  # noqa: E501

        self._basic = None
        self._damage_estimation = None
        self._arrival_time = None
        self.discriminator = None

        self.basic = basic
        self.damage_estimation = damage_estimation
        self.arrival_time = arrival_time

    @property
    def basic(self):
        """Gets the basic of this Result.  # noqa: E501


        :return: The basic of this Result.  # noqa: E501
        :rtype: bool
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        """Sets the basic of this Result.


        :param basic: The basic of this Result.  # noqa: E501
        :type: bool
        """
        if basic is None:
            raise ValueError("Invalid value for `basic`, must not be `None`")  # noqa: E501

        self._basic = basic

    @property
    def damage_estimation(self):
        """Gets the damage_estimation of this Result.  # noqa: E501


        :return: The damage_estimation of this Result.  # noqa: E501
        :rtype: bool
        """
        return self._damage_estimation

    @damage_estimation.setter
    def damage_estimation(self, damage_estimation):
        """Sets the damage_estimation of this Result.


        :param damage_estimation: The damage_estimation of this Result.  # noqa: E501
        :type: bool
        """
        if damage_estimation is None:
            raise ValueError("Invalid value for `damage_estimation`, must not be `None`")  # noqa: E501

        self._damage_estimation = damage_estimation

    @property
    def arrival_time(self):
        """Gets the arrival_time of this Result.  # noqa: E501


        :return: The arrival_time of this Result.  # noqa: E501
        :rtype: bool
        """
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, arrival_time):
        """Sets the arrival_time of this Result.


        :param arrival_time: The arrival_time of this Result.  # noqa: E501
        :type: bool
        """
        if arrival_time is None:
            raise ValueError("Invalid value for `arrival_time`, must not be `None`")  # noqa: E501

        self._arrival_time = arrival_time

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
        if not isinstance(other, Result):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
