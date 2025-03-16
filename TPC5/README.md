# TPC5: Criação de rotas para dicionário de conceitos

Para este projeto, o objetivo consistia em alterar o trabalho desenvolvido na aula, de maneira a criar uma página que lista todos os conceitos presentes no dicionário médico e que, clicando em cada um destes termos, redireciona para outra página que contém a descrição do mesmo.

---

## **Tarefa 1:** criar a rota '`/conceitos/<designacao>`' que faz o render template de um conceito, mostrando a designação e a respetiva descrição

De modo a satisfazer este requisito, foi criada a rota `/conceitos/<designacao>` e a seguinte função `conceito_individual`, que permite percorrer a lista de conceitos presentes no ficheiro json à procura do termo pretendido, devolvendo no final uma página apenas com a designação e a descrição do termo em questão.

```python

@app.route('/conceitos/<designacao>')
def conceito_individual(designacao):
    for conceito in list(db.keys()):
        if conceito == designacao:
            termo = conceito
            descri = db[termo]
            break
    return render_template("conceitos_solo.html", termo = termo, descri = descri, title = "Conceito " + designacao)
```

Adicionalmente, foi criado o ficheiro **conceitos_solo.html**, que completa o ficheiro **layout.html**, de maneira a possibilitar a visualização do conceito pretendido no browser.


## **Tarefa 2:** permitir que um clique num termo da lista apresentada em '`/conceitos`' redirecione para a página do respetivo conceito criada na tarefa anterior

Para a Tarefa 2, foi adaptado o ficheiro **conceitos.html**, de maneira a que este não retornasse apenas a designação de cada conceito em formato de lista, mas sim a designação num formato clicável, com uma hiperligação para a página do respetivo conceito criada na tarefa anterior. Para isto, foi utilizada a função `url_for()`, que permite ir buscar o url correto, correspondente à rota para cada um dos conceitos.
Deste modo, em vez de no ciclo for constar apenas `{{designacao}}`, essa linha de código foi substituída por:

```html
<a href="{{ url_for('conceito_individual', designacao = designacao) }}" target="_blank">{{designacao}}</a> 
```
