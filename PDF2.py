import PyPDF2
import pandas as pd

# Abrir o arquivo PDF
pdf_file = open('Guia do IRRF.pdf', 'rb')

# Criar um objeto pdf reader
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Extrair o texto de cada página do arquivo PDF
text = ''
for page in range(len(pdf_reader.pages)):
    text += pdf_reader.pages[page].extract_text()

# Fechar o arquivo PDF
pdf_file.close()

# Criar um dataframe pandas a partir do texto extraído
df = pd.DataFrame([x.split(',') for x in text.split('\n')])

# Salvar o dataframe como um arquivo CSV
df.to_csv('Guia do IRRF.csv', index=False)


# Adicionar um print statement
print('Arquivo CSV gerado com sucesso!')
