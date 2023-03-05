import flet
from flet import ElevatedButton, Page, Text, TextField, Row


def main(page: Page):
    link_user = TextField(label='Inserta una URL')

    lbl_encrypado = Text()

    def encryptado(event):
        enlace_encriptado = lbl_encrypado.replace(
            'http://catalogobibliotecaelam.sld.cu/index.php?P=DownloadFile&Id=', 'https://xdlfree.com/c/')
        lbl_encrypado.value = f'{enlace_encriptado}'
        page.update()

    row = Row(controls=[
        link_user,
        ElevatedButton(text='Encriptar', on_click=encryptado),
        lbl_encrypado
    ])

    page.add(row)


flet.app(target=main)
