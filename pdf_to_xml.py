from openpyxl import Workbook
import tranformador_de_pdf
import re

class Excel():
    def __init__(self, nome_xls, caminho_pdf, pagina_pdf):
        self.dest_filename = nome_xls
        self.pdf = tranformador_de_pdf.Pdf(caminho_pdf, pagina_pdf)
        self.wb = Workbook()

    def transformar_p_txt(self):
        """Chama o metodo e faz um arquivo em txt"""
        self.pdf.pdf_to_txt()

    def format_string(self):
        """formata as strings salvas no txt de uma maneira conveniente para se salvar na planilha"""
        with open("extracao.txt", "r+") as file_txt:
            with open("doc.txt", "w") as new_file:
                for line in file_txt:
                    new_file.
                    new_file.write(line.replace(";", "\n"))

    def txt_p_excel(self, nome_aba, nome_colun):
        """Criando uma planilha do arquivo txt ja editado """
        self.wb.create_sheet(nome_aba)
        self.planilha = self.wb[nome_aba]
        self.planilha.append([nome_colun])
        #abrindo arquivo txt pra jogar na planilha linha por linha
        with open("doc.txt") as txt_file:
            for line in txt_file:
                self.planilha.append([line])
        self.wb.save(filename=self.dest_filename)

teste_pdf = Excel("testeDODF2.xlsx", "DODF.pdf", 9)
teste_pdf.transformar_p_txt()
teste_pdf.format_string()
#teste_pdf.txt_p_excel("teste2", "nomes")




