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


class EntityListResult(Model):
    """Describes the result of the request to view entities.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param value: The list of entities.
    :type value: list[~azure.mgmt.managementgroups.models.EntityInfo]
    :ivar count: Total count of records that match the filter
    :vartype count: int
    :ivar next_link: The URL to use for getting the next set of results.
    :vartype next_link: str
    """

    _validation = {
        'count': {'readonly': True},
        'next_link': {'readonly': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': '[EntityInfo]'},
        'count': {'key': 'count', 'type': 'int'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EntityListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.count = None
        self.next_link = None
