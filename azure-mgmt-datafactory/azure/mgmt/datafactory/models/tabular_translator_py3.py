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

from .copy_translator import CopyTranslator


class TabularTranslator(CopyTranslator):
    """A copy activity tabular translator.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param column_mappings: Column mappings. Type: string (or Expression with
     resultType string).
    :type column_mappings: object
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'type': {'key': 'type', 'type': 'str'},
        'column_mappings': {'key': 'columnMappings', 'type': 'object'},
    }

    def __init__(self, *, additional_properties=None, column_mappings=None, **kwargs) -> None:
        super(TabularTranslator, self).__init__(additional_properties=additional_properties, **kwargs)
        self.column_mappings = column_mappings
        self.type = 'TabularTranslator'
