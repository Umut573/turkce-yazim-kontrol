from Levenshtein import distance


def en_iyi_oneri_sec(hatali_kelime, oneriler):
    return min(oneriler, key=lambda x: distance(hatali_kelime, x))
