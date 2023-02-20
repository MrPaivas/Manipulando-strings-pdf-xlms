from PyPDF2 import PdfReader

class Pdf():
    """Classe para representar um pdf"""
    def __init__(self, caminho, pagina):
        self.pdf = PdfReader(caminho)
        self.orientetion = 0
        self.paginas = int(pagina)
        self.page = self.pdf.pages[self.paginas]


    def contador_de_paginas(self):
        """conta quantas paginas existem no pdf"""
        contagem = len(self.pdf.pages)
        print("Esse PDF Contem " + str(contagem) + " paginas.")

    def pdf_to_txt(self):
        """extrai o texto do pdf e cria um arquivo em txt"""
        with open("extracao.txt","w") as self.txt_file:
            self.txt_file.write(self.page.extract_text(self.orientetion))



#pdf_01 = Pdf("F:\Documentos\Programacao\Projetos\PYTHON\pdfs\Teste_pdf_python.pdf", 0)
#pdf_02 = Pdf("F:\Documentos\Programacao\Projetos\PYTHON\pdfs\DODF.pdf", 8)
#pdf_01.contador_de_paginas()
#pdf_02.contador_de_paginas()

#pdf_02.pdf_to_txt()
