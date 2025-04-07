from bs4 import BeautifulSoup
import requests
import json

# agora para extrair as denças de todas as páginas e não só da página a

def get_doenca_info(url_href):
    url_doenca = "https://www.atlasdasaude.pt" + url_href
    response = requests.get(url_doenca)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')


    div_content = soup.find("div", class_="node-doencas")

    conteudo_doenca = {}

    doenca_descri_div = soup.find("div", class_="field-name-body")

    elem = doenca_descri_div.find("div", class_="field-item even")

    titulo = "Descrição"
    conteudo_doenca["Descrição"] = ""

    for item in elem:
        if item.name == 'p' or item.name == 'div': # descrição - entra com o título
            conteudo_doenca[titulo] += item.text

        elif item.name == 'h2': # causas e sintomas
            titulo = item.text.title()
            if "Artigos Relacionados" in titulo:
                conteudo_doenca[titulo] = {} 
            else:
                conteudo_doenca[titulo] = ""

        elif item.name == 'ul': # lista de sintomas 
            lista_sint = []
            for li in item.find_all('li'):
                lista_sint.append(li.text)
            conteudo_doenca["Sintomas"] = lista_sint

        elif item.name == 'h3': # artigos relacionados
            conteudo_doenca[titulo][item.text.strip()] = item.a['href']
            

    return {"url": url_doenca, "content": str(div_content)} | conteudo_doenca


def doencas_letra(letra):

    # para ir buscar o html da página das doenças
    url = "https://www.atlasdasaude.pt/doencasaaz/" + letra
    print(url)
    response = requests.get(url)

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    doencas = {}

    for div_row in soup.find_all("div", class_="views-row"):
        
        designacao = div_row.div.h3.a.text.strip()
        doenca_url = div_row.div.h3.a["href"]
        doenca_info = get_doenca_info(doenca_url)
        
        desc_div = div_row.find("div", class_="views-field-body")
        desc = desc_div.div.text

        doenca_info["resumo"] = desc.strip().replace(" ", " ")
        doencas[designacao] = doenca_info

        
    return doencas


res = {}

# maneira mega complexa de iterar sobre o alfabeto
for a in range(ord("a"), ord("z") + 1):
    letra = chr(a)
    res = res | doencas_letra(letra)
               

f_out = open("doencas_3.json", "w", encoding="utf-8")
json.dump(res, f_out, indent = 4, ensure_ascii = False)
f_out.close()