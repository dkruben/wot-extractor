# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/vehicle_hub/vehicle_hub_wallet_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/vehicle_hub/vehicle_hub_wallet_presenter.py
from __future__ import absolute_import
from gui.impl.lobby.page.wallet_presenter import WalletPresenter, GoldProvider, CreditsProvider, CrystalProvider, FreeXpProvider

class VehicleHubWalletPresenter(WalletPresenter):

    def __init__(self):
        super(VehicleHubWalletPresenter, self).__init__((
         CrystalProvider(),
         GoldProvider(),
         CreditsProvider(),
         FreeXpProvider()))
