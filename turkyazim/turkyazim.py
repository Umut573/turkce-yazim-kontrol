from .yazim_denetleyici import TurkceYazimDenetleyici as _TurkceYazimDenetleyici


class TurkceYazim:
    def __init__(self):
        self.denetleyici = _TurkceYazimDenetleyici()
    
    def duzelt(self, metin: str) -> str:
        return self.denetleyici.duzelt(metin)

    def raporla(self, metin: str) -> dict:
        return self.denetleyici.raporla(metin)
