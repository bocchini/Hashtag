import flet as ft
from flet import Page

def main(pagina: Page):
  titulo = ft.Text('Zap')
  pagina.horizontal_alignment = 'center'

  def enviar_mensagem(evento):
    texto = ft.Text(campo_enviar_mensagem.value)
    chat.controls.append(texto)
    pagina.update()

  campo_enviar_mensagem = ft.TextField(label='Digite sua mensagem')
  botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
  linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

  chat = ft.Column()

  def entrar_no_chat(evento):
    popup_flet.open = False
    pagina.remove(titulo)
    pagina.remove(botao)
    pagina.update()
    pagina.add(linha_enviar)
    pagina.add(chat)
    

  titulo_popup = ft.Text('Bem vindo ao Zap')
  caixa_nome = ft.TextField(label='Digite o seu nome')
  botao_popup = ft.ElevatedButton('Entrar no Chat', on_click=entrar_no_chat)
  
  popup_flet = ft.AlertDialog(title=titulo_popup,content=caixa_nome,actions=[botao_popup])

  def abrir_popup(event):

    pagina.dialog = popup_flet
    popup_flet.open = True
    pagina.update()
  
  botao = ft.ElevatedButton('Iniciar chat', on_click=abrir_popup)
  
  pagina.add(titulo)
  pagina.add(botao)


ft.app(main, view=ft.WEB_BROWSER)