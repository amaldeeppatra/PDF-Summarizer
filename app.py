from flask import Flask, render_template, request
from pypdf import PdfReader
from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template("landing.html")

@app.route('/main', methods=["GET", "POST"])
def mainpdfweb():
    display = ''
    if request.method == "POST":
        file = request.files['file']
        text = ''
        if file and file.filename.lower().endswith('.pdf'):
            # text = extract_text_from_pdf(file)    for pypdf2
            reader = PdfReader(file)
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                text += page.extract_text()

            print(text)

            summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
            ARTICLE = text
            display = summarizer(ARTICLE, max_length=150, min_length=50, do_sample=False)
            display = display[0]
            display = display['summary_text']
        
    return render_template("main.html", output=display)


if __name__ == "__main__":
    app.run(debug=True)