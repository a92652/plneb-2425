from flask import Flask, request, render_template
import json
import re

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")


dbFile = open("conceitos_.json", encoding = "utf-8")
db = json.load(dbFile)
dbFile.close()


@app.route('/api/conceitos')
def conceitos_api():
    return db 

@app.route('/conceitos')
def conceitos():
    designacoes = list(db.keys())
    return render_template("conceitos.html", designacoes = designacoes, title = "Lista de Conceitos")


@app.route('/conceitos/<designacao>') 
def conceito_individual(designacao):
    if designacao in db:
        descri = db[designacao]
        return render_template("conceitos_solo.html", termo = designacao, descri = descri, title = "Conceito " + designacao)
    else:
        return render_template("conceitos_solo.html", termo = "Erro", descri = "Descrição não encontrada", title = "Conceito " + designacao)


@app.route("/api/conceitos/<designacao>")
def api_conceito(designacao):
    return {"designacao": designacao, "descricao": db[designacao]}


@app.post("/api/conceitos")
def adicionar_conceito_api(): 
    # from json
    data = request.get_json()

    db[data["designacao"]] = data["descricao"]
   
    f_out = open("conceitos_.json", "w", encoding = "utf-8") 
    json.dump(db, f_out, indent = 4, ensure_ascii = False)
    f_out.close()
    return data


@app.post("/conceitos")
def adicionar_conceito():
    descricao = request.form.get("descricao")
    designacao = request.form.get("designacao")
    db[designacao] = descricao
    
    f_out = open("conceitos_.json", "w", encoding = "utf-8") 
    json.dump(db, f_out, indent = 4, ensure_ascii = False)
    f_out.close()

    designacoes = sorted(list(db.keys()))
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")


@app.route('/pesquisa')
def meun_pesquisa():
    resultados = {}

    return render_template("menu_pesquisa.html", resultados = resultados, title="Menu de Pesquisa")


@app.post('/pesquisa')
def pesquisa_conceito():
    resultados = {}
    pesquisa = request.form.get("termo")
    
    #pesquisa = request.form["termo"].lower()

    padrao = rf"\b{re.escape(pesquisa)}\b" # para só selecionar palavras completas

    for termo, descri in db.items():
        # if pesquisa in termo.lower() or pesquisa in descri.lower():
        # if re.search(fr'\b{re.escape(pesquisa)}\b', termo, flags = re.IGNORECASE) or re.search(fr'\b{re.escape(pesquisa)}\b', descri, flags = re.IGNORECASE):
        if re.search(padrao, termo, flags = re.IGNORECASE) or re.search(padrao, descri, flags = re.IGNORECASE):
            # resultados[termo] = descri

            # para a parte que deu match ficar em bold + clicável
            bold_termo = re.sub(padrao, rf'<a href="/conceitos/\g<0>" target="_blank" class="text-primary"><strong>\g<0></strong></a>', termo, flags=re.IGNORECASE)
            bold_descri = re.sub(padrao, rf'<a href="/conceitos/\g<0>" target="_blank" class="text-primary"><strong>\g<0></strong></a>', descri, flags=re.IGNORECASE)

            resultados[bold_termo] = bold_descri

    return render_template("menu_pesquisa.html", resultados = resultados, pesquisa = pesquisa, title="Menu de Pesquisa")

app.run(host="localhost", port = 40002, debug = True)
