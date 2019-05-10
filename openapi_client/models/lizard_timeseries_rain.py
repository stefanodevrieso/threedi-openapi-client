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


class LizardTimeseriesRain(object):
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
        'simulation': 'str',
        'start_timestep': 'int',
        'end_timestep': 'int',
        'reference_uuid': 'str',
        'start_datetime': 'datetime',
        'interpolate': 'bool',
        'values': 'list[list[float]]'
    }

    attribute_map = {
        'url': 'url',
        'simulation': 'simulation',
        'start_timestep': 'start_timestep',
        'end_timestep': 'end_timestep',
        'reference_uuid': 'reference_uuid',
        'start_datetime': 'start_datetime',
        'interpolate': 'interpolate',
        'values': 'values'
    }

    def __init__(self, url=None, simulation=None, start_timestep=None, end_timestep=None, reference_uuid=None, start_datetime=None, interpolate=None, values=None):  # noqa: E501
        """LizardTimeseriesRain - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._simulation = None
        self._start_timestep = None
        self._end_timestep = None
        self._reference_uuid = None
        self._start_datetime = None
        self._interpolate = None
        self._values = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if simulation is not None:
            self.simulation = simulation
        self.start_timestep = start_timestep
        self.end_timestep = end_timestep
        self.reference_uuid = reference_uuid
        self.start_datetime = start_datetime
        if interpolate is not None:
            self.interpolate = interpolate
        if values is not None:
            self.values = values

    @property
    def url(self):
        """Gets the url of this LizardTimeseriesRain.  # noqa: E501


        :return: The url of this LizardTimeseriesRain.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LizardTimeseriesRain.


        :param url: The url of this LizardTimeseriesRain.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def simulation(self):
        """Gets the simulation of this LizardTimeseriesRain.  # noqa: E501


        :return: The simulation of this LizardTimeseriesRain.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this LizardTimeseriesRain.


        :param simulation: The simulation of this LizardTimeseriesRain.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def start_timestep(self):
        """Gets the start_timestep of this LizardTimeseriesRain.  # noqa: E501

        Start of event in simulation in seconds  # noqa: E501

        :return: The start_timestep of this LizardTimeseriesRain.  # noqa: E501
        :rtype: int
        """
        return self._start_timestep

    @start_timestep.setter
    def start_timestep(self, start_timestep):
        """Sets the start_timestep of this LizardTimeseriesRain.

        Start of event in simulation in seconds  # noqa: E501

        :param start_timestep: The start_timestep of this LizardTimeseriesRain.  # noqa: E501
        :type: int
        """
        if start_timestep is None:
            raise ValueError("Invalid value for `start_timestep`, must not be `None`")  # noqa: E501
        if start_timestep is not None and start_timestep > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `start_timestep`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if start_timestep is not None and start_timestep < 0:  # noqa: E501
            raise ValueError("Invalid value for `start_timestep`, must be a value greater than or equal to `0`")  # noqa: E501

        self._start_timestep = start_timestep

    @property
    def end_timestep(self):
        """Gets the end_timestep of this LizardTimeseriesRain.  # noqa: E501

        End of event in simulation in seconds  # noqa: E501

        :return: The end_timestep of this LizardTimeseriesRain.  # noqa: E501
        :rtype: int
        """
        return self._end_timestep

    @end_timestep.setter
    def end_timestep(self, end_timestep):
        """Sets the end_timestep of this LizardTimeseriesRain.

        End of event in simulation in seconds  # noqa: E501

        :param end_timestep: The end_timestep of this LizardTimeseriesRain.  # noqa: E501
        :type: int
        """
        if end_timestep is not None and end_timestep > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `end_timestep`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if end_timestep is not None and end_timestep < 0:  # noqa: E501
            raise ValueError("Invalid value for `end_timestep`, must be a value greater than or equal to `0`")  # noqa: E501

        self._end_timestep = end_timestep

    @property
    def reference_uuid(self):
        """Gets the reference_uuid of this LizardTimeseriesRain.  # noqa: E501


        :return: The reference_uuid of this LizardTimeseriesRain.  # noqa: E501
        :rtype: str
        """
        return self._reference_uuid

    @reference_uuid.setter
    def reference_uuid(self, reference_uuid):
        """Sets the reference_uuid of this LizardTimeseriesRain.


        :param reference_uuid: The reference_uuid of this LizardTimeseriesRain.  # noqa: E501
        :type: str
        """
        if reference_uuid is None:
            raise ValueError("Invalid value for `reference_uuid`, must not be `None`")  # noqa: E501
        if reference_uuid is not None and len(reference_uuid) > 40:
            raise ValueError("Invalid value for `reference_uuid`, length must be less than or equal to `40`")  # noqa: E501
        if reference_uuid is not None and len(reference_uuid) < 1:
            raise ValueError("Invalid value for `reference_uuid`, length must be greater than or equal to `1`")  # noqa: E501

        self._reference_uuid = reference_uuid

    @property
    def start_datetime(self):
        """Gets the start_datetime of this LizardTimeseriesRain.  # noqa: E501


        :return: The start_datetime of this LizardTimeseriesRain.  # noqa: E501
        :rtype: datetime
        """
        return self._start_datetime

    @start_datetime.setter
    def start_datetime(self, start_datetime):
        """Sets the start_datetime of this LizardTimeseriesRain.


        :param start_datetime: The start_datetime of this LizardTimeseriesRain.  # noqa: E501
        :type: datetime
        """
        if start_datetime is None:
            raise ValueError("Invalid value for `start_datetime`, must not be `None`")  # noqa: E501

        self._start_datetime = start_datetime

    @property
    def interpolate(self):
        """Gets the interpolate of this LizardTimeseriesRain.  # noqa: E501


        :return: The interpolate of this LizardTimeseriesRain.  # noqa: E501
        :rtype: bool
        """
        return self._interpolate

    @interpolate.setter
    def interpolate(self, interpolate):
        """Sets the interpolate of this LizardTimeseriesRain.


        :param interpolate: The interpolate of this LizardTimeseriesRain.  # noqa: E501
        :type: bool
        """

        self._interpolate = interpolate

    @property
    def values(self):
        """Gets the values of this LizardTimeseriesRain.  # noqa: E501


        :return: The values of this LizardTimeseriesRain.  # noqa: E501
        :rtype: list[list[float]]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this LizardTimeseriesRain.


        :param values: The values of this LizardTimeseriesRain.  # noqa: E501
        :type: list[list[float]]
        """

        self._values = values

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
        if not isinstance(other, LizardTimeseriesRain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other