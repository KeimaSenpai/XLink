import wget
import os

FOLDER = 'Download'


async def dowload(link, ft):
    ft.Text(
        f"{link}")

    print(link)
    if link.__contains__('e'):
        if not os.path.exists(FOLDER):
            os.makedirs(FOLDER)
        codigos = link.removeprefix('https://xlink.cu/e/')
        pagina = f"https://cursad.jovenclub.cu/webservice/pluginfile.php/114867/core_competency/userevidence/{codigos}?forcedownload=1&token=a3b76f193d445b43d93f6478d7f2cac4"

    else:
        print('Error en la URL')

    print('Download\n')
    print(wget.download(pagina, out=FOLDER))

    print('\nDescargado\n')
