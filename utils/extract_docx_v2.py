import zipfile
import xml.etree.ElementTree as ET
import os

docx_path = r"d:\Proyek Mandiri\AI_Eng_Tes\web_dashboard\rencana_pembuatan_dashboard.docx"
output_path = r"d:\Proyek Mandiri\AI_Eng_Tes\utils\requirements.txt"

if not os.path.exists(docx_path):
    print(f"File not found: {docx_path}")
    exit(1)

try:
    with zipfile.ZipFile(docx_path) as document_zip:
        xml_content = document_zip.read('word/document.xml')
        
    tree = ET.fromstring(xml_content)
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    text_content = []
    
    # Iterate over body elements to preserve order
    body = tree.find('.//w:body', ns)
    if body:
        for element in body:
            # Check tag name safely ignoring namespace for simplicity if needed, but using ns is better
            if element.tag == f"{{{ns['w']}}}p": # Paragraph
                texts = [node.text for node in element.findall('.//w:t', ns) if node.text is not None]
                text_content.append("".join(texts))
            elif element.tag == f"{{{ns['w']}}}tbl": # Table
                for row in element.findall('.//w:tr', ns):
                    row_texts = []
                    for cell in row.findall('.//w:tc', ns):
                        cell_texts = []
                        for p in cell.findall('.//w:p', ns):
                            texts = [node.text for node in p.findall('.//w:t', ns) if node.text is not None]
                            cell_texts.append("".join(texts))
                        row_texts.append(" ".join(cell_texts)) # Join cell paragraphs with space
                    text_content.append(" | ".join(row_texts)) # Join cells with pipe
                text_content.append("-" * 20) # Separator for tables

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(text_content))

    print(f"Successfully extracted to {output_path}")

except Exception as e:
    import traceback
    traceback.print_exc()
