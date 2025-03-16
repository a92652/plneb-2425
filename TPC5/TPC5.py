from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


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
    for conceito in list(db.keys()):
        if conceito == designacao:
            termo = conceito
            descri = db[termo]
            break
    return render_template("conceitos_solo.html", termo = termo, descri = descri, title = "Conceito " + designacao)


@app.route("/api/conceitos/<designacao>")
def api_conceito(designacao):
    return {"designacao": designacao, "descricao": db[designacao]}


@app.post("/conceitos")
def adicionar_conceito(): # para obter os valores dados pelo cliente
    # from json
    data = request.get_json()
    #{"designacao": "", "descricao": ""} # o json vem neste formato 
    db[data["designacao"]] = data["descricao"]
 
    f_out = open("conceitos_.json", "w", encoding = "utf-8") 
    json.dump(db, f_out, indent = 4, ensure_ascii = False)
    f_out.close()
    return data


app.run(host="localhost", port = 4002, debug = True)

