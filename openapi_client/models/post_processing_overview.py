# coding: utf-8

"""
    3Di API

    3Di simulation API   Framework release: 0.0.12   3Di core release: 2.0.2  deployed on:  12:03PM (UTC) on October 17, 2019  # noqa: E501

    The version of the OpenAPI document: 3.0
    Contact: info@nelen-schuurmans.nl
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PostProcessingOverview(object):
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
        'simulation': 'int',
        'result_uuid': 'str',
        'process_basic_results': 'bool',
        'start_time_sim': 'str',
        'end_time_sim': 'str',
        'organisation': 'str',
        'username': 'str',
        'scenario_name': 'str',
        'model_name': 'str',
        'model_revision': 'str',
        'arrival': 'ArrivalTimePostProcessing',
        'damage': 'DamagePostProcessing',
        'damage_sources': 'str'
    }

    attribute_map = {
        'simulation': 'simulation',
        'result_uuid': 'result_uuid',
        'process_basic_results': 'process_basic_results',
        'start_time_sim': 'start_time_sim',
        'end_time_sim': 'end_time_sim',
        'organisation': 'organisation',
        'username': 'username',
        'scenario_name': 'scenario_name',
        'model_name': 'model_name',
        'model_revision': 'model_revision',
        'arrival': 'arrival',
        'damage': 'damage',
        'damage_sources': 'damage_sources'
    }

    def __init__(self, simulation=None, result_uuid=None, process_basic_results=None, start_time_sim=None, end_time_sim=None, organisation=None, username=None, scenario_name=None, model_name=None, model_revision=None, arrival=None, damage=None, damage_sources=None):  # noqa: E501
        """PostProcessingOverview - a model defined in OpenAPI"""  # noqa: E501

        self._simulation = None
        self._result_uuid = None
        self._process_basic_results = None
        self._start_time_sim = None
        self._end_time_sim = None
        self._organisation = None
        self._username = None
        self._scenario_name = None
        self._model_name = None
        self._model_revision = None
        self._arrival = None
        self._damage = None
        self._damage_sources = None
        self.discriminator = None

        if simulation is not None:
            self.simulation = simulation
        if result_uuid is not None:
            self.result_uuid = result_uuid
        if process_basic_results is not None:
            self.process_basic_results = process_basic_results
        if start_time_sim is not None:
            self.start_time_sim = start_time_sim
        if end_time_sim is not None:
            self.end_time_sim = end_time_sim
        if organisation is not None:
            self.organisation = organisation
        if username is not None:
            self.username = username
        if scenario_name is not None:
            self.scenario_name = scenario_name
        if model_name is not None:
            self.model_name = model_name
        if model_revision is not None:
            self.model_revision = model_revision
        self.arrival = arrival
        self.damage = damage
        if damage_sources is not None:
            self.damage_sources = damage_sources

    @property
    def simulation(self):
        """Gets the simulation of this PostProcessingOverview.  # noqa: E501


        :return: The simulation of this PostProcessingOverview.  # noqa: E501
        :rtype: int
        """
        return self._simulation

    @simulation.setter
    def simulation(self, simulation):
        """Sets the simulation of this PostProcessingOverview.


        :param simulation: The simulation of this PostProcessingOverview.  # noqa: E501
        :type: int
        """

        self._simulation = simulation

    @property
    def result_uuid(self):
        """Gets the result_uuid of this PostProcessingOverview.  # noqa: E501


        :return: The result_uuid of this PostProcessingOverview.  # noqa: E501
        :rtype: str
        """
        return self._result_uuid

    @result_uuid.setter
    def result_uuid(self, result_uuid):
        """Sets the result_uuid of this PostProcessingOverview.


        :param result_uuid: The result_uuid of this PostProcessingOverview.  # noqa: E501
        :type: str
        """

        self._result_uuid = result_uuid

    @property
    def process_basic_results(self):
        """Gets the process_basic_results of this PostProcessingOverview.  # noqa: E501


        :return: The process_basic_results of this PostProcessingOverview.  # noqa: E501
        :rtype: bool
        """
        return self._process_basic_results

    @process_basic_results.setter
    def process_basic_results(self, process_basic_results):
        """Sets the process_basic_results of this PostProcessingOverview.


        :param process_basic_results: The process_basic_results of this PostProcessingOverview.  # noqa: E501
        :type: bool
        """

        self._process_basic_results = process_basic_results

    @property
    def start_time_sim(self):
        """Gets the start_time_sim of this PostProcessingOverview.  # noqa: E501


        :return: The start_time_sim of this PostProcessingOverview.  # noqa: E501
        :rtype: str
        """
        return self._start_time_sim

    @start_time_sim.setter
    def start_time_sim(self, start_time_sim):
        """Sets the start_time_sim of this PostProcessingOverview.


        :param start_time_sim: The start_time_sim of this PostProcessingOverview.  # noqa: E501
        :type: str
        """

        self._start_time_sim = start_time_sim

    @property
    def end_time_sim(self):
        """Gets the end_time_sim of this PostProcessingOverview.  # noqa: E501


        :return: The end_time_sim of this PostProcessingOverview.  # noqa: E501
        :rtype: str
        """
        return self._end_time_sim

    @end_time_sim.setter
    def end_time_sim(self, end_time_sim):
        """Sets the end_time_sim of this PostProcessingOverview.


        :param end_time_sim: The end_time_sim of this PostProcessingOverview.  # noqa: E501
        :type: str
        """

        self._end_time_sim = end_time_sim

    @property
    def organisation(self):
        """Gets the organisation of this PostProcessingOverview.  # noqa: E501


        :return: The organisation of this PostProcessingOverview.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this PostProcessingOverview.


        :param organisation: The organisation of this PostProcessingOverview.  # noqa: E501
        :type: str
        """

        self._organisation = organisation

    @property
    def username(self):
        """Gets the username of this PostProcessingOverview.  # noqa: E501


        :return: The username of this PostProcessingOverview.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this PostProcessingOverview.


        :param username: The username of this PostProcessingOverview.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def scenario_name(self):
        """Gets the scenario_name of this PostProcessingOverview.  # noqa: E501

        Scenario name for saving the results  # noqa: E501

        :return: The scenario_name of this PostProcessingOverview.  # noqa: E501
        :rtype: str
        """
        return self._scenario_name

    @scenario_name.setter
    def scenario_name(self, scenario_name):
        """Sets the scenario_name of this PostProcessingOverview.

        Scenario name for saving the results  # noqa: E501

        :param scenario_name: The scenario_name of this PostProcessingOverview.  # noqa: E501
        :type: str
        """
        if scenario_name is not None and len(scenario_name) > 50:
            raise ValueError("Invalid value for `scenario_name`, length must be less than or equal to `50`")  # noqa: E501
        if scenario_name is not None and len(scenario_name) < 1:
            raise ValueError("Invalid value for `scenario_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._scenario_name = scenario_name

    @property
    def model_name(self):
        """Gets the model_name of this PostProcessingOverview.  # noqa: E501


        :return: The model_name of this PostProcessingOverview.  # noqa: E501
        :rtype: str
        """
        return self._model_name

    @model_name.setter
    def model_name(self, model_name):
        """Sets the model_name of this PostProcessingOverview.


        :param model_name: The model_name of this PostProcessingOverview.  # noqa: E501
        :type: str
        """

        self._model_name = model_name

    @property
    def model_revision(self):
        """Gets the model_revision of this PostProcessingOverview.  # noqa: E501


        :return: The model_revision of this PostProcessingOverview.  # noqa: E501
        :rtype: str
        """
        return self._model_revision

    @model_revision.setter
    def model_revision(self, model_revision):
        """Sets the model_revision of this PostProcessingOverview.


        :param model_revision: The model_revision of this PostProcessingOverview.  # noqa: E501
        :type: str
        """

        self._model_revision = model_revision

    @property
    def arrival(self):
        """Gets the arrival of this PostProcessingOverview.  # noqa: E501


        :return: The arrival of this PostProcessingOverview.  # noqa: E501
        :rtype: ArrivalTimePostProcessing
        """
        return self._arrival

    @arrival.setter
    def arrival(self, arrival):
        """Sets the arrival of this PostProcessingOverview.


        :param arrival: The arrival of this PostProcessingOverview.  # noqa: E501
        :type: ArrivalTimePostProcessing
        """
        if arrival is None:
            raise ValueError("Invalid value for `arrival`, must not be `None`")  # noqa: E501

        self._arrival = arrival

    @property
    def damage(self):
        """Gets the damage of this PostProcessingOverview.  # noqa: E501


        :return: The damage of this PostProcessingOverview.  # noqa: E501
        :rtype: DamagePostProcessing
        """
        return self._damage

    @damage.setter
    def damage(self, damage):
        """Sets the damage of this PostProcessingOverview.


        :param damage: The damage of this PostProcessingOverview.  # noqa: E501
        :type: DamagePostProcessing
        """
        if damage is None:
            raise ValueError("Invalid value for `damage`, must not be `None`")  # noqa: E501

        self._damage = damage

    @property
    def damage_sources(self):
        """Gets the damage_sources of this PostProcessingOverview.  # noqa: E501


        :return: The damage_sources of this PostProcessingOverview.  # noqa: E501
        :rtype: str
        """
        return self._damage_sources

    @damage_sources.setter
    def damage_sources(self, damage_sources):
        """Sets the damage_sources of this PostProcessingOverview.


        :param damage_sources: The damage_sources of this PostProcessingOverview.  # noqa: E501
        :type: str
        """

        self._damage_sources = damage_sources

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
        if not isinstance(other, PostProcessingOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
