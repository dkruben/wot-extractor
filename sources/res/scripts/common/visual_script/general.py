# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/visual_script/general.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/visual_script/general.py
from __future__ import absolute_import
from uuid_utils import genUUID
from visual_script.block import Block, makeResEditorData, InitParam
from visual_script.slot_types import SLOT_TYPE

class ResourceSelector(Block):

    def __init__(self, *args, **kwargs):
        super(ResourceSelector, self).__init__(*args, **kwargs)
        root, ext = self._getInitParams()
        self._res = self._makeDataInputSlot('res', SLOT_TYPE.RESOURCE)
        self._res.setEditorData(makeResEditorData(root, ext))
        self._out = self._makeDataOutputSlot('out', SLOT_TYPE.RESOURCE, self._exec)

    def _exec(self):
        self._out.setValue(self._res.getValue())

    @classmethod
    def initParams(cls):
        return [InitParam('root', SLOT_TYPE.STR, 'wot'), InitParam('ext', SLOT_TYPE.STR, 'xml')]


class GenerateUniqueString(Block):

    def __init__(self, *args, **kwargs):
        super(GenerateUniqueString, self).__init__(*args, **kwargs)
        self._prefix = self._makeDataInputSlot('prefix', SLOT_TYPE.STR)
        self._res = self._makeDataOutputSlot('res', SLOT_TYPE.STR, self._getData)

    @classmethod
    def blockIcon(cls):
        return ':vse/blocks/text'

    @classmethod
    def blockCategory(cls):
        return 'Strings'

    def _getData(self):
        prefix = self._prefix.getValue() if self._prefix.hasValue() else ''
        self._res.setValue(('{prefix}_{ts}').format(prefix=prefix, ts=genUUID().time))
