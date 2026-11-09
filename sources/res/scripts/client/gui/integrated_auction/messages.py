# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/integrated_auction/messages.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/integrated_auction/messages.py
from gui.SystemMessages import SM_TYPE
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.system_messages import ISystemMessages

@dependency.replace_none_kwargs(systemMessages=ISystemMessages)
def pushRateErrorMessage(systemMessages=None):
    text = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.rateError.text())
    systemMessages.pushMessage(text=text, type=SM_TYPE.IntegratedAuctionRateError)


@dependency.replace_none_kwargs(systemMessages=ISystemMessages)
def pushBelowCompetitiveRateMessage(systemMessages=None):
    text = backport.text(R.strings.messenger.serviceChannelMessages.integratedAuction.belowCompetitiveRate.text())
    systemMessages.pushMessage(text=text, type=SM_TYPE.IntegratedAuctionBelowCompetitiveRate)
