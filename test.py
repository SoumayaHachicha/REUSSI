from spire.doc import *
from spire.doc.common import *
import os
import docx

def replace_images_with_text(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.docx'):
            docx_path = os.path.join(directory, filename)
            doc = Document()

            doc.LoadFromFile(docx_path)

            variable = filename

            variable = variable.replace('docx', 'png') 

            j = 1

            for k in range(doc.Sections.Count):
                sec = doc.Sections.get_Item(k)

                for m in range(sec.Paragraphs.Count):
                    para = sec.Paragraphs.get_Item(m)

                    pictures = []

                    for x in range(para.ChildObjects.Count):
                        docObj = para.ChildObjects.get_Item(x)
                        if docObj.DocumentObjectType == DocumentObjectType.Picture:
                            pictures.append(docObj)

                    for pic in pictures:
                        index = para.ChildObjects.IndexOf(pic)
                        textRange = TextRange(doc)
                        textRange.Text = "Image/{0}/{1}".format(j, variable)
                        para.ChildObjects.Insert(index, textRange)
                        para.ChildObjects.Remove(pic)
                        j += 1

            doc.SaveToFile(docx_path, FileFormat.Docx)



