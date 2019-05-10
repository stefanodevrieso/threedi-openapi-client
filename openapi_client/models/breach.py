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


class Breach(object):
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
        'potential_breach': 'str',
        'duration_till_max_depth': 'int',
        'initial_width': 'float',
        'simulation': 'str',
        'start_timestep': 'int'
    }

    attribute_map = {
        'url': 'url',
        'potential_breach': 'potential_breach',
        'duration_till_max_depth': 'duration_till_max_depth',
        'initial_width': 'initial_width',
        'simulation': 'simulation',
        'start_timestep': 'start_timestep'
    }

    def __init__(self, url=None, potential_breach=None, duration_till_max_depth=None, initial_width=None, simulation=None, start_timestep=None):  # noqa: E501
        """Breach - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._potential_breach = None
        self._duration_till_max_depth = None
        self._initial_width = None
        self._simulation = None
        self._start_timestep = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.potential_breach = potential_breach
        self.duration_till_max_depth = duration_till_max_depth
        self.initial_width = initial_width
        if simulation is not None:
            self.simulation = simulation
        self.start_timestep = start_timestep

    @property
    def url(self):
        """Gets the url of this Breach.  # noqa: E501


        :return: The url of this Breach.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Breach.


        :param url: The url of this Breach.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def potential_breach(self):
        """Gets the potential_breach of this Breach.  # noqa: E501


        :return: The potential_breach of this Breach.  # noqa: E501
        :rtype: str
        """
        return self._potential_breach

    @potential_breach.setter
    def potential_breach(self, potential_breach):
        """Sets the potential_breach of this Breach.


        :param potential_breach: The potential_breach of this Breach.  # noqa: E501
        :type: str
        """
        if potential_breach is None:
            raise ValueError("Invalid value for `potential_breach`, must not be `None`")  # noqa: E501

        self._potential_breach = potential_breach

    @property
    def duration_till_max_depth(self):
        """Gets the duration_till_max_depth of this Breach.  # noqa: E501

        duration till maximum depth in seconds  # noqa: E501

        :return: The duration_till_max_depth of this Breach.  # noqa: E501
        :rtype: int
        """
        return self._duration_till_max_depth

    @duration_till_max_depth.setter
    def duration_till_max_depth(self, duration_till_max_depth):
        """Sets the duration_till_max_depth of this Breach.

        duration till maximum depth in seconds  # noqa: E501

        :param duration_till_max_depth: The duration_till_max_depth of this Breach.  # noqa: E501
        :type: int
        """
        if duration_till_max_depth is None:
            raise ValueError("Invalid value for `duration_till_max_depth`, must not be `None`")  # noqa: E501
        if duration_till_max_depth is not None and duration_till_max_depth > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `duration_till_max_depth`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if duration_till_max_depth is not None and duration_till_max_depth < 0:  # noqa: E501
            raise ValueError("Invalid value for `duration_till_max_depth`, must be a value greater than or equal to `0`")  # noqa: E501

        self._duration_till_max_depth = duration_till_max_depth

    @property
    def initial_width(self):
        """Gets the initial_width of this Breach.  # noqa: E501

        initial width in meters  # noqa: E501

        :return: The initial_width of this Breach.  # noqa: E501
        :rtype: float
        """
        return self._initial_width

    @initial_width.setter
    def initial_width(self, initial_width):
        """Sets the initial_width of this Breach.

        initial width in meters  # noqa: E501

        :param initial_width: The initial_width of this Breach.  # noqa: E501
        :type: float
        """
        if initial_width is None:
            raise ValueError("Invalid value for `initial_width`, must not be `None`")  # noqa: E501

        self._initial_width = initial_width

    @property
    def simulation(self):
        """Gets the simulation of this Breach.  # noqa: E501


        :return: The simulation of this Breach.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this Breach.


        :param simulation: The simulation of this Breach.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def start_timestep(self):
        """Gets the start_timestep of this Breach.  # noqa: E501

        Start of event in simulation in seconds  # noqa: E501

        :return: The start_timestep of this Breach.  # noqa: E501
        :rtype: int
        """
        return self._start_timestep

    @start_timestep.setter
    def start_timestep(self, start_timestep):
        """Sets the start_timestep of this Breach.

        Start of event in simulation in seconds  # noqa: E501

        :param start_timestep: The start_timestep of this Breach.  # noqa: E501
        :type: int
        """
        if start_timestep is None:
            raise ValueError("Invalid value for `start_timestep`, must not be `None`")  # noqa: E501
        if start_timestep is not None and start_timestep > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `start_timestep`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if start_timestep is not None and start_timestep < 0:  # noqa: E501
            raise ValueError("Invalid value for `start_timestep`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start_timestep = start_timestep

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
        if not isinstance(other, Breach):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other