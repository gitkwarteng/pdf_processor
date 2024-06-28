import io
from typing import Dict
from pdfminer.high_level import extract_text
import nltk
from nltk import pos_tag, word_tokenize

from api.models import PDFContent

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def process_pdf(*, file):
    """Process pdf file for nouns and verbs."""
    pdf_content = file.read()
    text = extract_text(io.BytesIO(pdf_content))

    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    nouns = [word for word, pos in tagged if pos.startswith('NN')]
    verbs = [word for word, pos in tagged if pos.startswith('VB')]

    return {
        'nouns': list(set(nouns)),
        'verbs': list(set(verbs))
    }


def save_pdf_content(*, email: str, file_name: str, data: Dict):
    """Save pdf content to database."""
    content = PDFContent(
        email=email,
        file=file_name,
        nouns=data.get('nouns', []),
        verbs=data.get('verbs', [])
    )
    content.save()

    return content
