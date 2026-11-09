# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/gui_items/processors/blueprints_convert_sale.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/gui_items/processors/blueprints_convert_sale.py
from __future__ import absolute_import
import BigWorld
from gui.shared.gui_items.processors import Processor

class ProcessExchangeBlueprintsProcessor(Processor):

    def __init__(self, offerID, count=1):
        super(ProcessExchangeBlueprintsProcessor, self).__init__()
        self.offerID = offerID
        self.count = count

    def _request(self, callback):
        BigWorld.player().exchangeBlueprintsSale(self.offerID, self.count, (lambda code, errStr: self._response(code, callback, errStr=errStr)))
