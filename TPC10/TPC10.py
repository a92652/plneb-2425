from bs4 import BeautifulSoup
import requests
import json

# código para extrair várias edições

# estrutura: lista de dicionários, em que cada dicionário corresponde a um artigo
# campos: title, authors, abstract, url, keywords, DOI, publish_date, edition


def get_info(url_artigo):
    # para ir buscar o html da página do artigo
    response = requests.get(url_artigo)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # abstract
    # nem todos os abstracts têm a estrutura: introdução, métodos, resultados e conclusão;
    # alguns é só mesmo texto corrido

    abstract = {} 

    abstract_div = soup.find("section", class_="item abstract")

    if abstract_div is None:
        pass # há casos em que não existe abstract
  
    else:
        for abstract_row in abstract_div.find_all("p"):

            strong = abstract_row.find("strong")
            if not strong:  # existe abstract, mas não está dividido nos vários campos
                if abstract == {}:
                    abstract = abstract_row.text.strip() # aqui já é só string e não um dicionário
                    # mas está dividido em parágrafos, por isso temos de os juntar todos
                else:
                    try:
                        abstract = abstract + abstract_row.text.strip()
                    except: # exceções em alguns artigos
                        continue 
            elif strong.text.strip() == ":": # caso exceção na 133
                pass
            else:
                campo = strong.text.strip(" :")
                texto = abstract_row.text.replace(strong.text, "").strip()
                abstract[campo] = texto

    # keywords
    keywords_div = soup.find("section", class_="item keywords")
    keywords = keywords_div.span.text.split(",")
    lista_keywords = [key.strip() for key in keywords]

    # doi
    doi_div = soup.find("section", class_="item doi")
    doi = doi_div.span.a.text.strip()

    # publish date
    publish_date_div = soup.find("div", class_="item published")
    publish_date = publish_date_div.section.div.span.text.strip()

    return {"abstract": abstract, "keywords": lista_keywords, "doi": doi, "publish_date": publish_date}


def get_edicao(num_edicao):

    artigos_edicao = []

    url_edicao = "https://revista.spmi.pt/index.php/rpmi/issue/view/" + str(num_edicao)
    response = requests.get(url_edicao)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')


    # edição da revista 
    div_edicao = soup.find("div", class_= "page page_issue")
    edicao = div_edicao.h1.text.strip() 

    # explorar o url de cada artigo desta edição 
    for div_row in soup.find_all("div", class_="obj_article_summary"):
        
        artigo = {}

        if num_edicao == 133 or num_edicao == 134: # estas duas têm o título tanto em inglês como em português, por isso vamos buscar o pt
            try:
                titulo = div_row.h3.a.span.text.strip()
            except:
                titulo = div_row.h3.a.text.strip() # exceção no último da 133 que só tem em pt
        else: # nas outras ou tem só em pt (135) ou só em inglês
            titulo = div_row.h3.a.text.strip()
        
        url_artigo = div_row.h3.a["href"]
    
        div_autores = div_row.find("div", class_="authors") 
        autores = div_autores.text.split(",") 
        lista_autores = [a.strip() for a in autores]

        # para ir buscar o resto da informação do artigo
        info_artigo = get_info(url_artigo)

        print(titulo, url_artigo, lista_autores)

        artigo["title"] = titulo
        artigo["url"] = url_artigo
        artigo["authors"] = lista_autores
        artigo["edition"] = edicao

        artigo = artigo | info_artigo # junta os dois dicionários - a informação da página principal com a da página do artigo

        artigos_edicao.append(artigo) # lista de todos os artigos desta edição da revista

    return artigos_edicao


artigos_total = []

# últimas 5 edições da revista
for edicao in range(130, 136):
    artigos_edicao = get_edicao(edicao)
    artigos_total = artigos_total + artigos_edicao


f_out = open("articles_completo.json", "w", encoding="utf-8")
json.dump(artigos_total, f_out, indent = 4, ensure_ascii = False)
f_out.close()
