# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dossiers2/common/utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dossiers2/common/utils.py
from __future__ import absolute_import, print_function
import dossiers2, struct
__DOSSIER_CONSOLE_OUTPUT_FORMAT = '%s\n--------------------\n%s\n===================='

def printAccountDossier(accountDossierDescr):
    printDossierFromDescr(accountDossierDescr, dossiers2.getAccountDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printVehicleDossier(vehicleDossierDescr):
    printDossierFromDescr(vehicleDossierDescr, dossiers2.getVehicleDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printTankmanDossier(tankmanDossierDescr):
    printDossierFromDescr(tankmanDossierDescr, dossiers2.getTankmanDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printRated7x7Dossier(rated7x7DossierDescr):
    printDossierFromDescr(rated7x7DossierDescr, dossiers2.getRated7x7DossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printClubDossier(clubDossierDescr):
    printDossierFromDescr(clubDossierDescr, dossiers2.getClubDossierDescr, __DOSSIER_CONSOLE_OUTPUT_FORMAT)


def printDossierFromDescr(dossierDescr, dossierGetter, format):
    printDossier(dossierGetter(dossierDescr), format)


def printDossier(dossier, format):
    print(('\n').join(convertDossierToText(format, dossier)))


def convertDossierToText(format, dossier):
    return [format % (block, dossier[block]) for block in dossier._DossierDescr__blocksLayout]


def getDossierVersion(dossierCompDescr, versionFormat, latestVersion):
    if dossierCompDescr == '':
        return latestVersion
    return struct.unpack_from(versionFormat, dossierCompDescr)[0]
