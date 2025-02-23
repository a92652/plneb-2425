# TPC2: Expressões Regulares

Este projeto contém diversas funções que utilizam expressões regulares, explorando as várias **funções regex** e a sua utilidade.

---

## **Lista de Funções Implementadas**

Em seguida apresentam-se todas as funções implementadas no projeto, em conjunto com uma breve descrição e exemplo.

As alíneas compreendidas no **Exercício 1** tiveram apenas como objetivo demonstrar o funcionamento e sintaxe das diversas funções contempladas pelo *regex*, nomeadamente das funções **match**, **search**, **findall**, **sub** e **split**.

### 2. **`palavra_magica(string)`:**
🔹 **Descrição:** Determina se uma string termina com a expressão "por favor", seguida de um sinal de pontuação válido, tendo sido considerados os seguintes: .?!.  
🔹 **Exemplo 1:** `palavra_magica("Posso ir à casa de banho, por favor?")` retorna `True`
🔹 **Exemplo 2:** `palavra_magica("Preciso de um favor.")` retorna `False`

### 3. **`narcissismo(string)`:**
🔹 **Descrição:** Calcula quantas vezes a palavra "eu" aparece numa string, quer esta se encontra em maiúsculas ou minúsculas. 
🔹 **Exemplo:** `narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou.")` retorna `6`

### 4. **`troca_de_curso(string, novo_curso)`:**
🔹 **Descrição:** Substitui todas as ocorrências da expressão "LEI" pela variável "novo_curso" passada à função.
🔹 **Exemplo:** `troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.", "Biomédica")` retorna `Biomédica é o melhor curso! Adoro Biomédica! Gostar de Biomédica devia ser uma lei.`

### 5. **`soma_string(string)`:**
🔹 **Descrição:** Devolve a soma dos números presentes numa string e separados por vírgulas.
🔹 **Exemplo:** `soma_string("4,-6,2,3,8,-3,0,2,-5,1")` retorna `6`

### 6. **`pronomes(string)`:**
🔹 **Descrição:** Encontra e devolve todos os pronomes pessoais presentes numa string, quer se encontrem em minúsculas ou maiúsculas.  
🔹 **Exemplo:** `pronomes("eu e tu fomos à praia com eles. Vós fostes com ela? Nós não")` retorna `['eu', 'tu', 'eles', 'Vós', 'ela', 'Nós']`

### 7. **`variavel_valida(string)`:**
🔹 **Descrição:** Verifica se a string dada apenas contém letras, números ou *underscores* e começa por uma letra.  
🔹 **Exemplo 1:** `variavel_valida("please_work1")` retorna `True`
🔹 **Exemplo 2:** `variavel_valida("1please_work1")` retorna `False`

### 8. **`inteiros(string)`:**
🔹 **Descrição:** Retorna todos os números inteiros presentes numa string (negativos e positivos).  
🔹 **Exemplo:** `inteiros("Fiz um bolo com 2 ovos e 350 g de farinha. -1 fatia por pessoa")` retorna `['2', '350', '-1']`

### 9. **`underscores(string)`:**
🔹 **Descrição:** Substitui todos os espaços de uma string por *underscores*.
🔹 **Exemplo:** `underscores("hoje        está um bonito dia")` retorna `hoje_está_um_bonito_dia`

### 10. **`codigos_postais(list)`:**
🔹 **Descrição:** Recebe uma lista de códigos postais e devolve uma lista de tuplos dos códigos postais divididos pelo hífen.
🔹 **Exemplo 1:** `codigos_postais(["4700-000", "1234-567", "8541-543", "4123-974", "9481-025"])` retorna `[('4700', '000'), ('1234', '567'), ('8541', '543'), ('4123', '974'), ('9481', '025')]`
