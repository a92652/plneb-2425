# TPC7: Implementação com recurso a DataTables

Para este projeto, o objetivo consistia em implementar uma tabela, com recurso às DataTables, que expusesse as várias designações e respetivas descrições presentes no dicionário médico fornecido.

As alterações efetuadas ao trabalho previamente desenvolvido foram as seguintes:

## **Alteração 1:** Implementação da tabela com recurso a DataTables

Em primeiro lugar, foi criada a rota `/tabela` no ficheiro `TPC7.py`, à qual é passada o ficheiro json correspondente ao dicionário médico e o template `tabela.html`.

```python

@app.get("/conceitos/tabela")
def conceitos_tabela():
    return render_template("tabela.html", db = db)

```

De seguida, na diretoria `templates`foi criado o ficheiro `tabela.html`, onde se construiu uma tabela que itera sobre o dicionário médico passado na rota, correspondendo cada linha da tabela ao termo e respetiva descrição. Foram feitos pequenos ajustes para que a tabela não se extendesse até às margens da página e para que os títulos de cada coluna ("Designação" e "Descrição") aparecessem centrados.

```html

<div class="container mt-4"> 
    <table id="tabela_conceitos" class="display">
        <thead>
            <tr>
                <th class="text-center">Designação</th>
                <th class="text-center">Descrição</th>
            </tr>
        </thead>
        <tbody>
            {% for designacao, descricao in db.items() %}
            <tr> 
                <td>{{ designacao }}</td>
                <td>{{ descricao }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>

```

Por último, para proceder à implementação com recurso a DataTables, foi adicionado o seguinte script na diretoria `scripts`.

```javascript

$(document).ready( function () {
    $('#tabela_conceitos').DataTable();
} );

```

## **Alteração 2:** Habilitação da Pesquisa por Expressões Regulares

De modo a possibilitar a pesquisa por expressões regulares na tabela, foi adicionada a opção `search.regex: true` ao script anteriormente mencionado.

```javascript

$(document).ready( function () {
    $('#tabela_conceitos').DataTable({
        "search": {
            "regex": true  // pesquisa com expressões regulares
        }
    });
} );

```

## **Alteração 3:** Adição da Página da Tabela à Home e à Barra de Navegação

No template `home.html`, este foi criado o botão `Tabela` e foi adicionado o caminho para a página criada, permitindo a passagem de uma página para outra.

```html

<a href="/conceitos/tabela" class="btn btn-outline-secondary btn-lg px-4">Tabela</a>

```

Para além disso, também se adiciou esta opção na barra de navegação definida no ficheiro `layout.html`.

```html

<a class="nav-link" href="/conceitos/tabela">Tabela</a>

```


## **Alteração 4:** Estilização da Tabela com Recurso a Bootstrap 5 e CSS

Como referido anteriormente, foi utilizada a estilização fornecida pelo Bootstrap 5 para ajustar a largura da tabela e para centrar os títulos de cada coluna. Adicionalmente, recorreu-se à estilização por CSS para alterar não só as cores da tabela em si, mas também a cor de destaque dada quando se passa com o cursor por cima. Estas alterações podem ser encontradas no ficheiro `table.css` na diretoria `css`.

```css

/* Cor de fundo para o header */
#tabela_conceitos thead th {
    background-color: #fbd2ff;
    color: #000000
}

/* Cor de fundo para as linhas */
#tabela_conceitos tr:nth-child(odd) {
    background-color: #fff8da;
}
#tabela_conceitos tr:nth-child(even) {
    background-color: #ffe9d1;
}


/* Cor quando se passa com o rato por cima  */
#tabela_conceitos tbody tr:hover {
    background: #baddff;
}

```