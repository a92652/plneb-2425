# Create a function that:
# 1. given a string “s”, reverse it.
# 2. given a string “s”, returns how many “a” and “A” characters are present in it.
# 3. given a string “s”, returns the number of vowels there are present in it.
# 4. given a string “s”, convert it into lowercase.
# 5. given a string “s”, convert it into uppercase.
# 6. Verifica se uma string é capicua
# 7. Verifica se duas strings estão balanceadas (Duas strings, s1 e s2, estão 
# balanceadas se todos os caracteres de s1 estão presentes em s2.)
# 8. Calcula o número de ocorrências de s1 em s2
# 9. Verifica se s1 é anagrama de s2. 
# ○ "listen" e "silent": Deve imprimir True
# ○ "hello", "world": Deve imprimir False
# 10. Dado um dicionário, calcular a tabela das classes de anagramas


# 1

def reverse(string):
    return string[::-1]


# 2 

def find_a(string):
    s = string.lower()
    return s.count("a")


# 3 

def vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    s = string.lower()
    count = 0
    for char in s:
        if char in vowels:
            count = count + 1
    return count


# 4

def lower(string):
    return string.lower()


# 5

def upper(string):
    return string.upper()


# 6

def capicua(string):
    val = False
    string = string.lower()
    s = string.replace(" ", "")
    cap = s[::-1]
    if s == cap:
        val = True
    return val


# 7

def balanceadas(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    val = True
    for char in s1:
        if char not in s2:
            val = False
            break
    return val


# 8

def ocorrencias(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return s2.count(s1)



# 9

def anagrama(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    val = False
    count = 0
    for char in s1:
        if char in s2:
            count = count + 1
    if count == len(s1) and len(s1) == len(s2):
        val = True
    return val



# 10

def classes_anagramas(words):
    dici = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in dici:
            dici[sorted_word].append(word)
        else:
            dici[sorted_word] = [word]
    return dici


def tabela_anagramas(dici):
    print(f"{'Letras organizadas':<20}{'Classe de anagramas'}")
    print("-" * 50)
    
    for letras, anagramas in sorted(dici.items()):
        anagramas_str = ", ".join(sorted(anagramas))
        print(f"{letras:<20}{anagramas_str}")




# testes automáticos
def testes_automaticos():
    print("\n1. Original: 'hello'; Invertida:", reverse("hello"))
    print("\n2. Contagem de 'a' e 'A' em 'BAnana':", find_a("BAnana"))
    print("\n3. Contagem de vogais em 'Olarilole':", vowels("Olarilole"))
    print("\n4. Original: 'Hello'; em minúsculas:", lower("Hello"))
    print("\n5. Original: 'Hello'; em maiúsculas:", upper("Hello"))
    print("\n6.1. Verifica se a palavra 'Ana' é capicua: ", capicua("Ana"))
    print("\n6.2. Verifica se a frase 'Luz Azul' é capicua: ", capicua("Luz Azul"))
    print("\n7. Verifica se as strings estão balanceadas ('Luz AZual', 'zzaul')?", balanceadas("Luz AZual", "zzaul"))
    print("\n8. Ocorrências de 'ola' em 'ola adeus, ola bom dia':", ocorrencias("ola", "ola adeus, ola bom dia"))
    print("\n9. Verifica se são anagramas:\n 'listen' e 'silent': ", anagrama("listen", "silent"), "\n","'hello' e 'world': ", anagrama("hello", "world"))
    list = ["amor", "mora", "ramo", "roma", "galo", "algo", "gola", "ator", "rato", "rota"]
    print("\n10. Tabela de classes de anagramas:") 
    tabela_anagramas(classes_anagramas(list))

    print("\nTodos os testes foram concluídos!")

# menu

def menu():
    while True:
        print("\n===== MENU DE FUNÇÕES =====")
        print("1. Inverter uma string")
        print("2. Contar 'a' e 'A' numa string")
        print("3. Contar vogais numa string")
        print("4. Converter string para minúsculas")
        print("5. Converter string para maiúsculas")
        print("6. Verificar se uma string é capicua")
        print("7. Verificar se duas strings estão balanceadas")
        print("8. Contar ocorrências de s1 em s2")
        print("9. Verificar se duas strings são anagramas")
        print("10. Criar tabela de classes de anagramas")
        print("11. Executar testes automáticos")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("A sair do programa...")
            break
        elif opcao == "1":
            s = input("Insira uma string: ")
            print("String invertida:", reverse(s))
        elif opcao == "2":
            s = input("Insira uma string: ")
            print("Número de 'a' e 'A':", find_a(s))
        elif opcao == "3":
            s = input("Insira uma string: ")
            print("Número de vogais:", vowels(s))
        elif opcao == "4":
            s = input("Insira uma string: ")
            print("Em minúsculas:", lower(s))
        elif opcao == "5":
            s = input("Insira uma string: ")
            print("Em maiúsculas:", upper(s))
        elif opcao == "6":
            s = input("Insira uma string: ")
            print("É capicua?", capicua(s))
        elif opcao == "7":
            s1 = input("Insira a primeira string: ")
            s2 = input("Insira a segunda string: ")
            print("As strings estão balanceadas?", balanceadas(s1, s2))
        elif opcao == "8":
            s1 = input("Insira a string s1: ")
            s2 = input("Insira a string s2: ")
            print(f"'{s1}' ocorre {ocorrencias(s1, s2)} vezes em '{s2}'")
        elif opcao == "9":
            s1 = input("Insira a string s1: ")
            s2 = input("Insira a string s2: ")
            print("São anagramas?", anagrama(s1, s2))
        elif opcao == "10":
            palavras = input("Insira uma lista de palavras separadas por espaço: ").split()
            print("Tabela de classes de anagramas:")
            tabela_anagramas(classes_anagramas(palavras))
        elif opcao == "11":
            testes_automaticos()
        else:
            print("Opção inválida! Tente novamente.")

menu()