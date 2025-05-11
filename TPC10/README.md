# TPC8: Web Scrapping - Revista de Medicina Interna

Para este projeto, o objetivo consistia em extrair várias informações sobre os artigos publicados nas várias edições da [Revista da Sociedade Portuguesa de Medicina Interna](https://revista.spmi.pt/index.php/rpmi/issue/archive) e organizá-las num ficheiro json.

As várias edições podem ser encontradas na secção _Archive_. Clicando na edição pretendida, é possível aceder aos vários artigos nela publicados e, clicando em cada um desses artigos, é possível obter várias informações sobre os mesmos, como o título (por vezes tanto em inglês, como em português), os autores, o _abstract_, a data de publicação, o DOI e as _keywords_.

## **Estrutura do Ficheiro JSON**

Para cada artigo, o ficheiro json criado apresenta, então, os seguintes campos:

- `title`: título do artigo, em português se disponível, caso contrário em inglês;
- `url`: link da página referente ao artigo em questão;
- `authors`: lista dos autores do artigo em questão;
- `edition`: edição da revista em que o artigo foi publicado;
- `abstract`: resumo do artigo, em formato de _string_, quando apenas contém texto corrido, ou em formato de dicionário com os campos `Introdução`, `Métodos`, `Resultados` e `Conclusão`, quando estes estão presentes e identificados;
- `keywords`: lista das palavras-chave do artigo em questão;
- `doi`: código doi do artigo em questão;
- `publish_date`: data de publicação do artigo em questão.

É de notar que nem todos os artigos apresentam _abstract_ ou _keywords_, pelo que estes campos podem aparecer vazios no ficheiro final. Adicionalmente, também existem casos em que estes campos estão presentes no artigo, mas em que o conteúdo é apenas ".".

O resultado final obtido é uma lista de dicionários, onde cada dicionário corresponde a um artigo (com os campos apresentados anteriormente).

Para este propósito, foram construída a função `get_edicao()`, que recebe como argumento o número da edição da revistam, itera sobre os vários artigos nela contidos, extrai os dados já acessíveis, como o título e os autores, e chama a função `get_info()`, que, por sua vez, extrai a restante informação da página de cada artigo.

Deste modo, no ficheiro JSON em anexo encontra-se a informação extraída dos artigos presentes nas últimas cinco edições da revista.

## **Exemplo de entrada no dicionário JSON obtido**

```json

{
    "title": "Comportamento do Utilizador do Serviço de Urgência do Hospital da Horta-Açores",
    "url": "https://revista.spmi.pt/index.php/rpmi/article/view/2582",
    "authors": [
        "Ana Simas",
        "Nuno Amorim",
        "Catarina Cabrita",
        "Ricardo Veloso",
        "Juvenal Morais",
        "Rui Suzano"
    ],
    "edition": "Vol. 32 No. 1 (2025): Janeiro / Março",
    "abstract": {
        "Introdução": "O uso inapropriado dos serviços de urgência,com todas as consequências negativas para os sistemas desaúde, é um fenómeno generalizado multifactorial e com tendência crescente.",
        "Métodos": "Para conhecer a nossa realidade fizemos um estudo do comportamento do utilizador do serviço de urgência do Hospital da Horta através de um inquérito, tendo sido analisados 463 casos, representando 6,5% de todos os episódios do período de estudo, dos quais 44% eram do género masculino e 56% feminino e dois terços dos quais tinham idades entre 24 e os 66 anos.",
        "Resultados": "Com base na triagem de Manchester 60% dos inquiridos foram classificados não urgentes (Verdes, Azuise Brancos). Apenas 5% tinha contactado a linha Saúde24 e só 12% tentou consulta no médico de família.",
        "Conclusão": "Os motivos principais pela opção hospitalar foram a auto percepção de urgência clínica, a busca na celeridade do Serviço de Urgência para resolução do problema, o menor tempo de espera no atendimento, a maior probabilidade de acesso a um especialista hospitalar e/ou a exames diagnósticos e a uma expectativa de maior qualidade no serviço prestado."
    },
    "keywords": [
        "Açores",
        "Inquéritos e Questionários",
        "Mau Uso de Serviços de Saúde/estatísticas e dados numéricos",
        "Serviço de Urgência Hospitalar/estatística e dados numéricos"
    ],
    "doi": "https://doi.org/10.24950/rspmi.2582",
    "publish_date": "2025-03-31"
}

```