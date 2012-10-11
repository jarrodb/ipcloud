"""
Physical Interface Management
"""

import settings

class PIF:
    def __init__(self, session):
        self._session = session


def get_network(session, pif):
    return session.xenapi.PIF.get_network(pif)

def get_public_pif(session):
    pifs = get_pif_records(session)
    for rec in pifs:
        if pifs[rec]['device'] == settings.PIF_PUBLIC:
            return rec
    return None

def get_private_pif(session):
    pifs = get_pif_records(session)
    for rec in pifs:
        if pifs[rec]['device'] == settings.PIF_PRIVATE:
            return rec
    return None

def get_pif_records(session):
    return session.xenapi.PIF.get_all_records()
