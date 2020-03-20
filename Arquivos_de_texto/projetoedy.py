'''https://imasters.com.br/back-end/como-fazer-web-scraping-com-python
pega todos os alunos que passaram em tads na chamada atual
'''


import urllib.request

webUrl = urllib.request.urlopen("http://www.comvest.unicamp.br/vest2020/F2/aprova2/chamada2/geral.html") #EXTRAI O HTML DA PAGINA E RETORNA UMA STRING
with open("documento.txt","w") as arq:
    lista = str(webUrl.read())
    for c in lista.split('\\r\\n'):
        if 'Analise' in c:
            arq.write(f'{c.strip()}\n')



