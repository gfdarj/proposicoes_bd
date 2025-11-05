from datetime import datetime

def hoje_formatado(formato="%d/%m/%Y"):
    return datetime.today().strftime(formato)

def data_por_extenso(data=None):
    if not data:
        data = datetime.today()
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    return f"{data.day} de {meses[data.month - 1]} de {data.year}"
