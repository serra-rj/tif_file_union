import os
from PIL import Image

def combinar_tiff(arquivo1, arquivo2, caminho_saida):

    with Image.open(arquivo1) as tiff1:
        paginas1 = [tiff1.copy() for pagina in range(tiff1.n_frames) if tiff1.seek(pagina) is None]

    with Image.open(arquivo2) as tiff2:
        paginas2 = [tiff2.copy() for pagina in range(tiff2.n_frames) if tiff2.seek(pagina) is None]

    #Juntar as páginas dos dois arquivos
    paginas_combined = paginas1 + paginas2

    #Salvar todas as páginas no arquivo de saída
    paginas_combined[0].save(
        caminho_saida, save_all=True, append_images=paginas_combined[1:]
    )
    print(f"Arquivos combinados salvos em: {caminho_saida}")

#Caminhos dos arquivos tif
arquivo1 = r"deretório.tif"
arquivo2 = r"diretório.tif"

#Salvar no Desktop
caminho_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
arquivo_saida = os.path.join(caminho_desktop, "arquivo_combinado.tiff")

#Juntar e salva no Desktop
combinar_tiff(arquivo1, arquivo2, arquivo_saida)
