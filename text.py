from pypdf import PdfReader
from transformers import pipeline

reader = PdfReader('Project Title_ Football Stats Application.pdf')

text = ''

for i in range(len(reader.pages)):
    page = reader.pages[i]
    text += page.extract_text()

print(text)


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = text

print(summarizer(ARTICLE, max_length=150, min_length=50, do_sample=False))