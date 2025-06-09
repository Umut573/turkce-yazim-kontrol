from zemberek import TurkishSpellChecker
from .bert_denetleyici import TurkceBERTDenetleyici
from .utils.oneriler import en_iyi_oneri_sec
import requests


class TurkceYazimDenetleyici:
    def __init__(self):
        self.zemberek = TurkishSpellChecker()
        self.bert = TurkceBERTDenetleyici()
        self.ozel_kelimeler = set()

    def ozel_kelime_ekle(self, kelime: str):
        self.ozel_kelimeler.add(kelime)
        self.zemberek.add_to_user_dict([kelime])

    def tdk_kontrol(self, kelime: str) -> bool:
        try:
            response = requests.get(f"https://sozluk.gov.tr/gts?ara={kelime}").json()
            return len(response) > 0
        except:
            return False

    def duzelt(self, metin: str) -> str:
        cumleler = [c.strip() for c in metin.split(".") if c.strip()]
        duzeltilmis_cumleler = []

        for cumle in cumleler:
            kelimeler = cumle.split()
            duzeltilmis_kelime_listesi = []

            for kelime in kelimeler:
                if self._kelime_gecerli_mi(kelime):
                    duzeltilmis_kelime_listesi.append(kelime)
                else:
                    oneriler = list(self.zemberek.suggest_for_word(kelime))
                    if not oneriler:
                        oneriler = self.bert.en_iyi_oneri(cumle, kelime)
                    if oneriler:
                        duzeltilmis_kelime_listesi.append(en_iyi_oneri_sec(kelime, oneriler))
                    else:
                        duzeltilmis_kelime_listesi.append(kelime)

            duzeltilmis_cumleler.append(" ".join(duzeltilmis_kelime_listesi))

        return " ".join([c + "." for c in duzeltilmis_cumleler])

    def _kelime_gecerli_mi(self, kelime: str) -> bool:
        return (
            self.zemberek.is_correct(kelime) or
            kelime in self.ozel_kelimeler or
            self.tdk_kontrol(kelime)
        )

    def raporla(self, metin: str) -> dict:
        return {
            "orijinal_metin": metin,
            "duzeltilmis_metin": self.duzelt(metin),
            "hatalar": self._hatalari_bul(metin)
        }

    def _hatalari_bul(self, metin: str) -> list:
        hatalar = []
        for kelime in metin.split():
            if not self._kelime_gecerli_mi(kelime):
                oneriler = list(self.zemberek.suggest_for_word(kelime))
                if not oneriler:
                    oneriler = self.bert.en_iyi_oneri(metin, kelime)
                hatalar.append({
                    "kelime": kelime,
                    "oneriler": oneriler[:3]
                })
        return hatalar
