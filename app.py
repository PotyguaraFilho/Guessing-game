import flet as ft
from random import randint


def main(page: ft.Page):

    page.title = "Jogo de Adivinhação"
    page.horizontal_alignment = "center"
    page.bgcolor = "white"
    page.window_full_screen = True
    

    random_num = randint(1,30)
    global contagem, num_entrou, quantidade_num
    contagem = 0
    num_entrou = []


    def vai_jogar_sim(e):
        img = ft.Image(src=f"Why_Man-removebg-preview.png", width=150,height=150)
        titulo = ft.Text(value="Jogo de Adivinhação\n", size=50, color="black", font_family="Forte")

        vai_jogar = ft.Text("Se abriu, é pra jogar né!", size=25, color="black")
        page.clean()
        page.add(img, titulo, vai_jogar, ft.ElevatedButton("Iniciar", bgcolor="green", color="white", on_click=escolhe_qtd))       

    def reinicia_jogo(e):
        page.clean()
        main(page)

    def opcao_inicio(e):

        if not resp.value:
            resp.error_text = "Você precisa digitar SIM ou NÃO!"
            page.update()
        elif resp.value.lower() == "sim":
            text = ft.Text(f"Opção confirmada: {resp.value}", size=15, color="green")
            page.add(text, ft.ElevatedButton("Vamos lá", on_click=escolhe_qtd, bgcolor="green", color="white"))
            page.update()
        elif resp.value.lower() == "não" or resp.value.lower() == "nao":
            text = ft.Text(f"Opção confirmada: {resp.value}", size=15, color="red")
            page.add(text, ft.ElevatedButton("Tchau então!", on_click=vai_jogar_sim, bgcolor="red", color="white"))
            page.update()
        else:
            erro = ft.Text("Você não está digitando o que se pede!", size=15, color="red")
            page.add(erro)
            page.update()

    def escolhe_qtd(e):
        global quantidade_num

        img = ft.Image(src=f"Why_Man-removebg-preview.png", width=150,height=150)
        titulo = ft.Text(value="Jogo de Adivinhação\n", size=50, color="black", font_family="Forte")
        page.clean()
        page.add(img, titulo)
        page.update()

        text = ft.Text('Digite a quantidade de vezes que quer tentar sendo o máximo, 10 vezes!',size=20, color="black")
        quantidade_num = ft.TextField(label="Digite quantas vezes tentará", text_align="center", color="black", width=350, border_radius=10, on_submit=opcao_qtd)
        page.add(
            text,
            quantidade_num,
            ft.ElevatedButton("Enviar", on_click=opcao_qtd, color="white")
            )
        page.update()

    def opcao_qtd(e):
        global quantidade_num


        if not quantidade_num.value:
            quantidade_num.error_text = "Você precisa digitar a quantidade de vezes para tentar!"
            page.update()
        else:
            qtd_num = int(quantidade_num.value)
            
            if qtd_num > 10:
                quantidade_num.error_text = "Digite um número menor ou igual a 10!"
                page.update()
            else:
                text = ft.Text(f"Quantidade enviada: {qtd_num}", size=15, color="blue") 
                page.add(text, ft.ElevatedButton("Tentar", on_click=quantidade, bgcolor="blue", color="white"))
                page.update()

    def quantidade(e):
        global qtd_vezes, quantidade_num
        
        img = ft.Image(src=f"Why_Man-removebg-preview.png", width=150,height=150)
        titulo = ft.Text(value="Jogo de Adivinhação\n", size=50, color="black", font_family="Forte")
        page.clean()
        page.add(img, titulo)
        page.update()

        qtd_num = int(quantidade_num.value)
        qtd_vezes = ft.Text(f'\n\nVocê terá {qtd_num} chances para tentar acertar.',size=20, color="black")
        page.add(qtd_vezes, ft.ElevatedButton("OK", on_click=entra_num, color="white"))
        page.update()
    
    def entra_num(e):
        global entrada_num
        
        entrada_num = ft.TextField(label="Digite um número", text_align="center", color="black", width=350, border_radius=10, on_submit=verifica)
        page.add(entrada_num , ft.ElevatedButton("Verificar", on_click=verifica, color="white"))
        page.update()

    def verifica(e):
        global entrada_num, qtd_vezes, contagem    
        contagem += 1

        if not entrada_num.value:
            entrada_num.error_text = "Você precisa digitar um número!"
            page.update()
        else:
            num = int(entrada_num.value)
            qtd = int(quantidade_num.value)
            num_entrou.append(num)    
                   
            if num == random_num:
                img = ft.Image(src=f"Why_Man-removebg-preview.png", width=150,height=150)
                titulo = ft.Text(value="Jogo de Adivinhação\n", size=50, color="black", font_family="Forte")
                win = ft.Text(f"Parabéns, você acertou na {contagem}ª tentativa! Número sorteado foi {random_num}", size=20, color="black")
                texto = ft.Text(f"Números digitados: {num_entrou}.", size=20, color="black")
                page.clean()
                page.add(img, titulo, win, texto)
                page.update()
                page.add(ft.ElevatedButton("Sair", on_click=reinicia_jogo, color="white"))
                return
            
            elif contagem == qtd:
                img = ft.Image(src=f"Why_Man-removebg-preview.png", width=150,height=150)
                titulo = ft.Text(value="Jogo de Adivinhação\n", size=50, color="black", font_family="Forte")
                lost = ft.Text(f"\n\nInfelizmente você não conseguiu adivinhar. O número sorteado foi {random_num}", size=20, color="black")
                digitados = ft.Text(f"Números digitados: {num_entrou}", size=20, color="black")
                page.clean()
                page.add(img, titulo, lost, digitados)
                page.update()
                page.add(ft.ElevatedButton("Sair", on_click=reinicia_jogo, color="white"))
                return

            elif num > random_num:
                img = ft.Image(src=f"Why_Man-removebg-preview.png", width=150,height=150)
                titulo = ft.Text(value="Jogo de Adivinhação\n", size=50, color="black", font_family="Forte")
                maior = ft.Text(f"Hmm, {num} é maior, digite um número menor.\n", size=20, color="black")
                tentativas = ft.Text(f'Tentativa: {contagem + 1}', size=20, color="black")
                page.clean()
                page.add(img, titulo, maior, tentativas)
                entra_num(e)

            elif num < random_num:
                img = ft.Image(src=f"Why_Man-removebg-preview.png", width=150,height=150)
                titulo = ft.Text(value="Jogo de Adivinhação\n", size=50, color="black", font_family="Forte")
                menor = ft.Text(f"Hmm, {num} é menor, digite um número maior.\n", size=20, color="black")
                tentativas = ft.Text(f'Tentativa: {contagem + 1}', size=20, color="black")
                page.clean()
                page.add(img, titulo, menor, tentativas)
                entra_num(e)

            
    img = ft.Image(src=f"Why_Man-removebg-preview.png", width=150,height=150)
    titulo = ft.Text(value="Jogo de Adivinhação\n", size=50, color="black", font_family="Forte")
    page.add(img, titulo)
    page.update()

    texto = ft.Text("Deseja iniciar o jogo? SIM OU NÃO", size=20, color="black")
    resp = ft.TextField(label="Sua resposta aqui", text_align="center", color="black", width=350, border_radius=10, on_submit=opcao_inicio)
    page.add(texto, resp, ft.ElevatedButton("Confirmar", on_click=opcao_inicio, color="white"))
    page.update()
    page.scroll = True


ft.app(target=main)
