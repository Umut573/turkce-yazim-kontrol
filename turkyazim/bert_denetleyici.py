from transformers import BertTokenizer, BertForMaskedLM
import torch
import re


class TurkceBERTDenetleyici:
    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained("dbmdz/bert-base-turkish-cased")
        self.model = BertForMaskedLM.from_pretrained("dbmdz/bert-base-turkish-cased")

    def en_iyi_oneri(self, cumle: str, hatali_kelime: str) -> list:
        cumle = re.sub(r'\b' + re.escape(hatali_kelime) + r'\b', '[MASK]', cumle)
        input_ids = self.tokenizer.encode(cumle, return_tensors="pt")
        mask_index = (input_ids == self.tokenizer.mask_token_id).nonzero().item()

        with torch.no_grad():
            outputs = self.model(input_ids)
            logits = outputs.logits

        mask_word_probs = torch.softmax(logits[0, mask_index], dim=0)
        values, indices = torch.topk(mask_word_probs, 5)

        oneriler = []
        for v, i in zip(values, indices):
            kelime = self.tokenizer.decode(i.item())
            if len(kelime) > 1 and kelime != hatali_kelime:
                oneriler.append(kelime)

        return oneriler
