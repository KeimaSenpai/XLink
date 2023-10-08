import flet as ft
from dl import *
import asyncio


async def sendToDownload(e):
    await dowload(url.value, ft)


async def main(page: ft.Page):
    global url, btn
    page.window_width = 1021
    page.window_height = 721
    page.window_resizable = False
    page.padding = 0
    page.fonts = {
        "Revamped": "asset/fonts/Revamped.otf"
    }

    # Componentes que iran en la barra lateral
    text_logo = ft.Text('X', size=50, font_family='Revamped')
    icon_down = ft.Image('asset/img/Icon/file_download.png', height=35)
    icon_uplo = ft.Image('asset/img/Icon/upload_file.png', height=35)
    icon_encr = ft.Image('asset/img/Icon/password_window.png', height=35)
    icon_info = ft.Image('asset/img/Icon/info.png', height=35)

    # Organixo los iconos en Columnas y los centro
    icons = ft.Column(spacing=10, controls=[
        icon_down,
        icon_uplo,
        icon_encr
    ])

    # Aqui es donde organizo todo lo de la barra lateral
    superior = ft.Container(text_logo, alignment=ft.alignment.center)
    medio = ft.Container(icons, alignment=ft.alignment.center)
    inferior = ft.Container(icon_info, alignment=ft.alignment.center)

    # Aqui coloco todo para la barra de navegación
    nab_icon = ft.Column(spacing=100, controls=[
        superior,
        medio,
        inferior
    ])

    # ---------------------Aqui es la seccion de contenido col_2--------------
    text = ft.Text('XLink', size=30, font_family='Arial')
    url = ft.TextField(label='URL')
    btn = ft.ElevatedButton(
        text='Download', color='#ffffff', bgcolor='#262626', on_click=sendToDownload)

    Texto_dow = ft.Column(spacing=10, controls=[
        text,
        url,
        btn
    ])

    Contenedor = ft.Container(Texto_dow, alignment=ft.alignment.center)

    # Contenedores principales
    col_1 = ft.Container(nab_icon, width=60, height=721, bgcolor='#262626')
    col_2 = ft.Container(Contenedor, width=931, height=721, bgcolor='#3A3A3A')

    await page.add_async(
        ft.Row([
            col_1,
            col_2,
        ],
            spacing=0
        )
    )


ft.app(target=main)
