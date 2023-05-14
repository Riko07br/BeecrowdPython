import unicodedata
import re
import pyperclip
"""
Script para remover acentos ao copiar o nome da Questao direto do Beecrowd
"""

name = input()

#Codigo para remover os acentos e carateres latinos encontrado aqui:
#https://gist.github.com/boniattirodrigo/67429ada53b7337d2e79

# Unicode normalize transforma um caracter em seu equivalente em latin.
nfkd = unicodedata.normalize('NFKD', name)
palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])

# Usa expressão regular para retornar a palavra apenas com números, letras e espaço
name = re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

name = name.replace(" ", "_")

#deixa na area de transferencia
pyperclip.copy(name + ".py")
