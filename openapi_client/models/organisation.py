# coding: utf-8

"""
    3Di API

    3Di simulation API (latest version: 3.0)   Framework release: 0.0.37   3Di core release: 2.0.6  deployed on:  02:54PM (UTC) on March 20, 2020  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Organisation(object):
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
        'unique_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'url': 'url',
        'unique_id': 'unique_id',
        'name': 'name'
    }

    def __init__(self, url=None, unique_id=None, name=None):  # noqa: E501
        """Organisation - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._unique_id = None
        self._name = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.unique_id = unique_id
        self.name = name

    @property
    def url(self):
        """Gets the url of this Organisation.  # noqa: E501


        :return: The url of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Organisation.


        :param url: The url of this Organisation.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def unique_id(self):
        """Gets the unique_id of this Organisation.  # noqa: E501


        :return: The unique_id of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this Organisation.


        :param unique_id: The unique_id of this Organisation.  # noqa: E501
        :type: str
        """
        if unique_id is None:
            raise ValueError("Invalid value for `unique_id`, must not be `None`")  # noqa: E501
        if unique_id is not None and len(unique_id) > 32:
            raise ValueError("Invalid value for `unique_id`, length must be less than or equal to `32`")  # noqa: E501
        if unique_id is not None and len(unique_id) < 1:
            raise ValueError("Invalid value for `unique_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._unique_id = unique_id

    @property
    def name(self):
        """Gets the name of this Organisation.  # noqa: E501


        :return: The name of this Organisation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Organisation.


        :param name: The name of this Organisation.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

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
        if not isinstance(other, Organisation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
