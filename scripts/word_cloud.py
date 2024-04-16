import fitz  # PyMuPDF
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 确保下载必要的NLTK数据
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
stop_words.update(['et', 'al', 'fl', 'fm', 'fms', 'wang', 'zhang', 'chen', 'liu', 'yu',
                   'li', 'arxiv', 'ieee', 'client', 'model', 'sun', 'yang', 'xu',
                   'data', 'clients', 'publication data', 'han', 'huang', 'wang', 'zhang',
                   'preprint', 'client', 'server', 'network', 'paper', 'proceeding',
                   'conference', 'international', 'journal', 'workshop', 'symposium',
                   'transaction', 'association', 'acm', 'sigcomm', 'sigir', 'vol'])

def extract_text_from_pdfs(pdf_paths):
    text = ""
    for pdf_path in pdf_paths:
        document = fitz.open(pdf_path)
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            text += page.get_text()
    return text

def preprocess_text(text):
    # 去除停用词和其他预处理
    tokens = nltk.word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.isalnum() and not any(
        char.isdigit() for char in word) and word.lower() not in stop_words]
    return ' '.join(filtered_tokens)

def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# 示例PDF文件路径列表
pdf_paths = ['FL4FM.pdf', 'tmp.pdf']

# 提取和预处理文本
text = extract_text_from_pdfs(pdf_paths)
processed_text = preprocess_text(text)

# 生成词云
generate_wordcloud(processed_text)
