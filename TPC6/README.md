# TPC6: Criação de um Menu de Pesquisa

Para este projeto, o objetivo consistia em aprimorar o trabalho desenvolvido na aula, de maneira a criar um menu de pesquisa, que permite a procura de termos e devolve todas as entradas do dicionário onde esse termo aparece, quer seja na designação ou na descrição. Adicionalmente, nas entradas do dicionário devolvidas,o termo procurado encontra-se realçado a negrito e é clicável, redirecionando para a página do termo, caso este possua uma entrada no dicionário. 

As alterações efetuadas ao trabalho previamente desenvolvido foram as seguintes:

## **Alteração 1:** criação da rota `/pesquisa`, no ficheiro `TPC6.py`, tanto para operações de GET como de POST, de maneira a possibitar a inserção do termo que se pretende pesquisar e a exibição dos respetivos resultados.

Recorreu-se à utilização de expressões regulares para criar um padrão que garantisse que apenas eram capturadas palavras completas e não partes das mesmas, ou seja, por exemplo, que a pesquisa da palavra 'mão' não devolvesse resultados com a palavra 'irmão'. Graças ainda às expressões regulares, foi também possível que a pesquisa ocorresse independentemente da ocorrência de maiúsculas/minúsculas ao longo da palavra, através da utilização da flag `IGNORECASE`.

Por último, tanto o dicionário de resultados obtidos, como o termo pesquisado são passados de volta para o template, de maneira a possibilitar a exibição correta dos mesmos na página desenvolvida. 

```python

@app.route('/pesquisa')
def meun_pesquisa():
    resultados = {}

    return render_template("menu_pesquisa.html", resultados = resultados, title="Menu de Pesquisa")


@app.post('/pesquisa')
def pesquisa_conceito():
    resultados = {}
    pesquisa = request.form.get("termo")

    padrao = rf"\b{re.escape(pesquisa)}\b" # para só selecionar palavras completas

    for termo, descri in db.items():
        if re.search(padrao, termo, flags = re.IGNORECASE) or re.search(padrao, descri, flags = re.IGNORECASE):
            # para a parte que deu match ficar em bold + clicável
            bold_termo = re.sub(padrao, rf'<a href="/conceitos/\g<0>" target="_blank" class="text-primary"><strong>\g<0></strong></a>', termo, flags=re.IGNORECASE)
            bold_descri = re.sub(padrao, rf'<a href="/conceitos/\g<0>" target="_blank" class="text-primary"><strong>\g<0></strong></a>', descri, flags=re.IGNORECASE)

            resultados[bold_termo] = bold_descri

    return render_template("menu_pesquisa.html", resultados = resultados, pesquisa = pesquisa, title="Menu de Pesquisa")

```

## **Alteração 2:** criação do template `menu_pesquisa.html`, para exibição da página web

Este ficheiro é uma extensão do ficheiro `layout.html` e o seu principal componente é um formulário para a introdução do termo a pesquisar pelo utilizador. Caso o termo pesquisado exista no dicionário médico, a lista de resultados obtida é percorrida, exibindo na página todas as correspondências encontradas. Para mais fácil utilização e compreensão por parte do utilizador, o termo procurado encontra-se destacado a negrito e é clicável, redirecionando para a página que contém a sua própria descrição, caso esta exista. Por outro lado, se o termo pesquisado não existir no dicionário médico, é devolvida uma mensagem de erro com a informação "Nenhum resultado encontrado.". 


## **Alteração 3:** Adição de funcionalidade ao botão de 'Pesquisar', no ficheiro `home.html`

No template `home.html`, este botão já se encontrava criado, mas não redirecoinava para lado nenhum, uma vez que esta funcionalidade de pesquisa não existia. Deste modo, foi adicionado o caminho para a página criada, permitindo a passagem de uma página para outra.


## **Alteração 4:** Adição da página de pesquisa na barra de navegação, no ficheiro `layout.html`

A barra de navegação, que antes só possuia a opção de 'Conceitos', agora passa também a apresentar a opção de 'Pesquisa', redirecionando para a respetiva páginaquando clicada.
