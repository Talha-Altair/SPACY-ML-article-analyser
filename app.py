import spacy
from spacy.lang.en import English
from spacy.matcher import Matcher

nlp=spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)

pattern = [{"LOWER":"iphone"},{"IS_PUNCT":False}]

matcher.add("Pattern", [pattern])

doc=nlp("upcoming iphone X is released")

matches=matcher(doc)
for match_id, start, end in matches:
    matched_span = doc[start:end]
    print(matched_span.text)

