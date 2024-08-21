from docx import Document

def docx_to_txt():
    doc = Document("../files/m7手册.docx")

    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    full_text = '\n'.join(text)

    with open("../output/m7手册.txt", "w", encoding="utf-8") as output_file:
        output_file.write(full_text)

docx_to_txt()
