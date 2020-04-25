import pdfx
import spacy
import pandas as pd

pdf = pdfx.PDFx("Path of the pdf file")
text = pdf.get_text()

nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

cols = ("text", "lemma", "POS", "explain", "stopword")
rows = []

for t in doc:
    row = [t.text, t.lemma_, t.pos_, spacy.explain(t.pos_), t.is_stop]
    rows.append(row)

df = pd.DataFrame(rows, columns=cols)

for ent in doc.ents:
    print(ent.text, ent.label_)