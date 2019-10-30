# coding: utf-8

"""
    3DI API

    3DI simulation API   Framework release: 0.0.17   3Di core release: 2.0.2  deployed on:  10:18AM (UTC) on October 30, 2019  # noqa: E501

    OpenAPI spec version: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class SimulationStatus(object):
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
        'name': 'str',
        'simulation': 'str',
        'created': 'datetime',
        'time': 'int',
        'crash_report': 'str',
        'id': 'int'
    }

    attribute_map = {
        'url': 'url',
        'name': 'name',
        'simulation': 'simulation',
        'created': 'created',
        'time': 'time',
        'crash_report': 'crash_report',
        'id': 'id'
    }

    def __init__(self, url=None, name=None, simulation=None, created=None, time=None, crash_report=None, id=None):  # noqa: E501
        """SimulationStatus - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._name = None
        self._simulation = None
        self._created = None
        self._time = None
        self._crash_report = None
        self._id = None
        self.discriminator = None

        if url is not None:
            self.url = url
        self.name = name
        if simulation is not None:
            self.simulation = simulation
        if created is not None:
            self.created = created
        self.time = time
        self.crash_report = crash_report
        if id is not None:
            self.id = id

    @property
    def url(self):
        """Gets the url of this SimulationStatus.  # noqa: E501


        :return: The url of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SimulationStatus.


        :param url: The url of this SimulationStatus.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this SimulationStatus.  # noqa: E501


        :return: The name of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimulationStatus.


        :param name: The name of this SimulationStatus.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        allowed_values = ["created", "starting", "initialized", "queued", "ended", "postprocessing", "finished", "crashed"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def simulation(self):
        """Gets the simulation of this SimulationStatus.  # noqa: E501


        :return: The simulation of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this SimulationStatus.


        :param simulation: The simulation of this SimulationStatus.  # noqa: E501
        :type: str
        """

        self._simulation = simulation

    @property
    def created(self):
        """Gets the created of this SimulationStatus.  # noqa: E501


        :return: The created of this SimulationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SimulationStatus.


        :param created: The created of this SimulationStatus.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def time(self):
        """Gets the time of this SimulationStatus.  # noqa: E501

        simulation time in seconds  # noqa: E501

        :return: The time of this SimulationStatus.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SimulationStatus.

        simulation time in seconds  # noqa: E501

        :param time: The time of this SimulationStatus.  # noqa: E501
        :type: int
        """
        if time is not None and time > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if time is not None and time < 0:  # noqa: E501
            raise ValueError("Invalid value for `time`, must be a value greater than or equal to `0`")  # noqa: E501

        self._time = time

    @property
    def crash_report(self):
        """Gets the crash_report of this SimulationStatus.  # noqa: E501


        :return: The crash_report of this SimulationStatus.  # noqa: E501
        :rtype: str
        """
        return self._crash_report

    @crash_report.setter
    def crash_report(self, crash_report):
        """Sets the crash_report of this SimulationStatus.


        :param crash_report: The crash_report of this SimulationStatus.  # noqa: E501
        :type: str
        """

        self._crash_report = crash_report

    @property
    def id(self):
        """Gets the id of this SimulationStatus.  # noqa: E501


        :return: The id of this SimulationStatus.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SimulationStatus.


        :param id: The id of this SimulationStatus.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if not isinstance(other, SimulationStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
