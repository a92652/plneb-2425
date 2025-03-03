# TPC3: Formatação recorrendo a Expressões Regulares

Neste projeto, o objetivo consistia em resolver diversos desafios encontrados no processo de produção de uma página html a partir de um documento pdf. O referido documento representa um dicionário de termos médicos, onde, na maioria dos casos, os vários termos se encontram separados das respetivas descrições por um '\n', e cada conjunto termo + descrição se encontra separado dos restantes por '\n\n'. 

A dificuldade da formatação surge do facto de, apesar das regras referidas representarem a maioria dos casos, existirem também casos no documento que não seguem estas normas:
 - conjuntos termo + descrição separados por '\n\n\f' (ex: articulação);
 - locais onde o conteúdo da descrição se encontra separado a meio por '\n\n\f' (ex: cretinismo);
 - locais onde o termo e a respetiva descrição se encontram separados por '\n\n\f' (ex: atrepsia);

A solução encontrada para resolver este problema tira partido da estrutura do próprio texto, notando-se que os termos nunca apresentam na sua constituição sinais de pontuação, como a vírgula, o ponto ou o ponto e vírgula, que, por outro lado, se encontram sempre presentes em algum local das descrições.

Deste modo, o primeiro passo do processo de limpeza do documento foi utilizar a expressão regular **`texto = re.sub(r'\n\n\f(?=(.+[.,;]))', "\n", texto)`** para prever se uma expressão iniciada pelo tão problemático '\n\n\f' iria apresentar algum dos referidos sinais de pontuação na sua constituição, ou seja, se o que se seguia era uma descrição. Assim, apenas no caso de pelo menos um destes sinais de pontuação estar presente é que se procedeu à substituição de '\n\n\f' por apenas '\n', resolvendo o problema da separação dos termos das respetivas descrições.

Nos restantes casos de ocorrências de '\f', foi utilizada a expressão regular **`texto = re.sub(r'\f', " ", texto)`** para os remover do documento, substituindo-os por um espaço em branco. Isto permitiu resolver o problema da separação dos vários conjuntos termo + descrição, uma vez que, a partir daqui, cada conjunto pode ser separado e identificado pelo padrão '\n\n'.

Por último, de modo a identificar cada conjunto termo + descrição, foi utilizada a expressão regular **`texto = re.sub(r'\n\n', "\n\n@", texto)`** para acrescentar o marcador '@' ao início de cada novo termo no dicionário.

O restante processo até à obtenção do ficheiro html foi feito do mesmo modo que o executado na aula, eliminando o problema da descrição poder estar separada a meio por '\n\n\f' através da utilização da expressão regular **`descricao = re.sub(r'\n', " ", descricao)`**, que substitui os '\n\n' por espaços vazios (uma vez que os '\f' já tinham sido removidos anteriormente).

O código completo que permite gerar a página html a partir do documento pdf pode ser encontrado em conjunto, sendo que aqui apenas foi detalhada a estratégia de resolução do '\n\n\f'. 