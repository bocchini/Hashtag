import flet as ft

#Popup
titulo_popup = ft.Text('Bem vindo ao Zap')
caixa_nome = ft.TextField(label='Digite o seu nome')
botao_popup = ft.ElevatedButton('Entrar no Chat')
popup_flet = ft.AlertDialog(title=titulo_popup,content=caixa_nome,actions=[botao_popup])
