from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

ARTICLE = '''
ranking is 401-500 in the world. KIIT has been accredited with an A++ grade by the National Assessment and Accreditation Council (NAAC) with an all-India 16th rank by the National Institution of Ranking Framework, NIRF, Ministry of Education. It has also been the top university for innovation among private institutions for two consecutive years (2020, 2021) according to AICTE, Government of India. It has been ranked among the top 151-200 universities in the world as per the Times Higher Education Young University Ranking 2022. KIIT has made colossal contributions to Sports. Currently, 11 Olympians pursue their education at KIIT. The University has been conferred the Sportstar Award and FICCI India Sports Award for the promotion of sports.
'''

print(summarizer(ARTICLE, max_length=100, min_length=50, do_sample=False))