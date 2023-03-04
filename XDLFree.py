import wget
import os

folder = 'Download'
folder_masivo = 'TXT'
version = ('0.5 (Beta)')
# headers = {"user-agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}


def dlfree():
    link_encryp = input('Escribe la URL: ')
    if link_encryp.__contains__('e'):
        codigos = link_encryp.removeprefix('https://xdlfree.com/e/')
        pagina = f"https://uvs.ucm.cmw.sld.cu/webservice/pluginfile.php/577/core_competency/userevidence/{codigos}?token=b460a61906d764f345cc4720ffca843b&forcedownload=1"

    if link_encryp.__contains__('b'):
        codigos = link_encryp.removeprefix('https://xdlfree.com/b/')
        pagina = f"https://uvs.ucm.cmw.sld.cu/webservice/pluginfile.php/1/blog/attachment/{codigos}?token=?token=b460a61906d764f345cc4720ffca843b&forcedownload=1"

    if link_encryp.__contains__('c'):
        codigos = link_encryp.removeprefix('https://xdlfree.com/c/')
        pagina = f"http://catalogobibliotecaelam.sld.cu/index.php?P=DownloadFile&Id={codigos}"

    else:
        print('Error EN la URL')

    print('Download\n')
    # headers = {"user-agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
    print(wget.download(pagina, out=folder))

    print('\nDescargado\n')
    return inicio()


def dl_masivo():
    directory = (folder_masivo)
    with open(os.path.join(directory, 'file.txt'), 'r') as f:
        for line in f:
            url = line.strip()
            link_carpeta = (url)

            if link_carpeta.__contains__('e'):
                codigos = link_carpeta.removeprefix('https://xdlfree.com/e/')
                pagina = f"https://uvs.ucm.cmw.sld.cu/webservice/pluginfile.php/577/core_competency/userevidence/{codigos}?token=b460a61906d764f345cc4720ffca843b&forcedownload=1"

            if link_carpeta.__contains__('b'):
                codigos = link_carpeta.removeprefix('https://xdlfree.com/b/')
                pagina = f"https://uvs.ucm.cmw.sld.cu/webservice/pluginfile.php/1/blog/attachment/{codigos}?token=?token=b460a61906d764f345cc4720ffca843b&forcedownload=1"

            if link_carpeta.__contains__('c'):
                codigos = link_carpeta.removeprefix('https://xdlfree.com/c/')
                pagina = f"http://catalogobibliotecaelam.sld.cu/index.php?P=DownloadFile&Id={codigos}"
            else:
                print('Error en el archivo')

            print(wget.download(pagina, out=folder))
            f.close
    return inicio()


if __name__ == '__main__':
    def inicio():
        os.system('cls')
        if not os.path.exists(folder):
            os.makedirs(folder)
        if not os.path.exists(folder_masivo):
            os.makedirs(folder_masivo)

        print(
            f'              █ Bienvenido a XDL Free █\n\n»Simple scipt para descargar.\n»Desarrollado por KeimaSenpai.\n»Versión: {version}\n')
        print('▐Para Descargar escribe D\n▐Para descarga masiva escribe T\n▐Si quiere salir escriba Q\n▐')
        select = input('▐Escribe la opción: ')
        if select == "D":
            dlfree()
        if select == "T":
            dl_masivo()
        if select == "Q":
            exit

inicio()
