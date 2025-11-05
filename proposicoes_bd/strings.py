def capitalizar_primeiras_palavras(texto):
    return ' '.join(p.capitalize() for p in texto.split())

def remover_acentos(texto):
    import unicodedata
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
