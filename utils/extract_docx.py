import zipfile
import xml.etree.ElementTree as ET
import os

docx_path = r"d:\Proyek Mandiri\AI_Eng_Tes\web_dashboard\rencana_pembuatan_dashboard.docx"

if not os.path.exists(docx_path):
    print(f"File not found: {docx_path}")
    exit(1)

try:
    with zipfile.ZipFile(docx_path) as document_zip:
        xml_content = document_zip.read('word/document.xml')
        
    tree = ET.fromstring(xml_content)
    
    # Namespace for Word
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    paragraphs = []
    
    # Find all paragraphs
    for p in tree.findall('.//w:p', ns):
        texts = [node.text for node in p.findall('.//w:t', ns) if node.text is not None]
        paragraphs.append("".join(texts))
        
    print("\n".join(paragraphs))

except Exception as e:
    print(f"Error: {e}")
