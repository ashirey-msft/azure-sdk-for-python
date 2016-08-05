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


class TldLegalAgreement(Model):
    """Represents a legal agreement for top level domain.

    :param agreement_key: Unique identifier for the agreement
    :type agreement_key: str
    :param title: Agreement title
    :type title: str
    :param content: Agreement details
    :type content: str
    :param url: Url where a copy of the agreement details is hosted
    :type url: str
    """ 

    _attribute_map = {
        'agreement_key': {'key': 'agreementKey', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, agreement_key=None, title=None, content=None, url=None):
        self.agreement_key = agreement_key
        self.title = title
        self.content = content
        self.url = url