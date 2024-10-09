import pyautogui
import time
import pandas
# Passo 1 Entrar no site da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/
pyautogui.PAUSE = 0.5

pyautogui.press("win") #apertar uma tecla do teclado
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Passo 2 Fazer login
pyautogui.click(x=445, y=389)
pyautogui.write("brrjuliana@outlook.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.click(x=651, y=556)

# Passo 3 Importar a base de dados
tabela = pandas.read_csv("produtos.csv") 

# Passo 4 Cadastrar 1 produto
for linha in tabela.index:
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.click(x=549, y=280)
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5 Repetiir o processo de cadastro ate acabar os produtos

