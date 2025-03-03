import re

file = open("dicionario_medico.txt", encoding = "utf-8")
texto = file.read()

# limpeza
texto = re.sub(r'\n\n\f(?=(.+[.,;]))', "\n", texto) # substitui só nas descrições
texto = re.sub(r'\f', " ", texto) # retirar os \f restantes

# marcar os conceitos
texto = re.sub(r'\n\n', "\n\n@", texto) # @ antes de cada conceito

def limpa(descricao):
    descricao = descricao.strip() # tirar os \n\n do final
    descricao = re.sub(r'\n', " ", descricao)
    return descricao

# extrair os conceitos
conceitos_raw = re.findall(r'@(.*)\n([^@]*)', texto)

conceitos = [(designacao, limpa(descricao)) for designacao, descricao in conceitos_raw]

#print(conceitos)

# gerar HTML

def gera_html(conceitos):
    html_header = f"""
            <!DOCTYPE html>
                <head>
                <meta charset = "UTF-8"/> <!--dava certo na mesma sem isto e sem o encoding no open de escrita-->
                </head>
                <body>
                <h3>Dicionário de Conceitos Médicos</h3>
                <p>Este dicionário foi desenvolvido para a aula de PLNEB 2024/2025</p>"""

    html_conceitos = ""

    for designacao, descricao in conceitos:
        html_conceitos += f"""
                    <div>
                    <p><b>{designacao}</b></p>
                    <p>{descricao}</p>
                    </div>
                    <hr/>
                """
    
    html_footer = f"""
                </body>
            </html>"""

    return html_header + html_conceitos + html_footer 

html = gera_html(conceitos)
f_out = open("dicionario_medico.html", "w", encoding = "utf-8")
f_out.write(html)
f_out.close()

file.close()