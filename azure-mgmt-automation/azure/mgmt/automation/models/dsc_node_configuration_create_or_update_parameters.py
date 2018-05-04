# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DscNodeConfigurationCreateOrUpdateParameters(Model):
    """DscNodeConfigurationCreateOrUpdateParameters.

    :param source: Gets or sets the source.
    :type source: ~azure.mgmt.automation.models.ContentSource
    :param configuration: Gets or sets the configuration of the node.
    :type configuration:
     ~azure.mgmt.automation.models.DscConfigurationAssociationProperty
    :param increment_node_configuration_build: If a new build version of
     NodeConfiguration is required.
    :type increment_node_configuration_build: bool
    :param name: Name of the node configuration.
    :type name: str
    :param tags: Gets or sets the tags attached to the resource.
    :type tags: dict[str, str]
    """

    _validation = {
        'source': {'required': True},
        'configuration': {'required': True},
    }

    _attribute_map = {
        'source': {'key': 'properties.source', 'type': 'ContentSource'},
        'configuration': {'key': 'properties.configuration', 'type': 'DscConfigurationAssociationProperty'},
        'increment_node_configuration_build': {'key': 'properties.incrementNodeConfigurationBuild', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, source, configuration, increment_node_configuration_build=None, name=None, tags=None):
        super(DscNodeConfigurationCreateOrUpdateParameters, self).__init__()
        self.source = source
        self.configuration = configuration
        self.increment_node_configuration_build = increment_node_configuration_build
        self.name = name
        self.tags = tags
