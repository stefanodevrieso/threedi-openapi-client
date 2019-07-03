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


class FileUpload(object):
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
        'put_url': 'str'
    }

    attribute_map = {
        'put_url': 'put_url'
    }

    def __init__(self, put_url=None):  # noqa: E501
        """FileUpload - a model defined in OpenAPI"""  # noqa: E501

        self._put_url = None
        self.discriminator = None

        self.put_url = put_url

    @property
    def put_url(self):
        """Gets the put_url of this FileUpload.  # noqa: E501


        :return: The put_url of this FileUpload.  # noqa: E501
        :rtype: str
        """
        return self._put_url

    @put_url.setter
    def put_url(self, put_url):
        """Sets the put_url of this FileUpload.


        :param put_url: The put_url of this FileUpload.  # noqa: E501
        :type: str
        """
        if put_url is None:
            raise ValueError("Invalid value for `put_url`, must not be `None`")  # noqa: E501
        if put_url is not None and len(put_url) < 1:
            raise ValueError("Invalid value for `put_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._put_url = put_url

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
        if not isinstance(other, FileUpload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other