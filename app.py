#!/usr/bin/env python3
"""
voice_conversion.py: Convert English sentences between active and passive voice using spaCy.
"""
import spacy
from spacy.symbols import nsubj, nsubjpass, dobj, aux, auxpass

nlp = spacy.load('en_core_web_sm')
# Common "be" forms for passive constructions\AUX_FORMS = {"am", "is", "are", "was", "were", "be", "been", "being"}


def is_passive(doc):
    return any(tok.dep == nsubjpass for tok in doc)


def convert_active_to_passive(doc):
    subj = [tok for tok in doc if tok.dep == nsubj]
    dobject = [tok for tok in doc if tok.dep == dobj]
    verbs = [tok for tok in doc if tok.pos_ == 'VERB']
    if not subj or not dobject or not verbs:
        return doc.text
    subj_text = subj[0].text
    dobj_text = dobject[0].text
    verb = verbs[0].lemma_
    # Use past participle via spaCy morphological tag if available
    pp = verbs[0]._.inflect('VBN') if verbs[0]._.inflect else verb + 'ed'
    sentence = f"{dobj_text.capitalize()} {AUX_FORMS.pop()} {pp} by {subj_text}"
    return sentence


def convert_passive_to_active(doc):
    # Find components
    subj = [tok for tok in doc if tok.dep == nsubjpass]
    agent = [tok for tok in doc if tok.dep_ == 'pobj']
    verbs = [tok for tok in doc if tok.pos_ == 'VERB']
    if not subj or not agent or not verbs:
        return doc.text
    subj_text = subj[0].text
    agent_text = agent[0].text
    verb = verbs[0].lemma_
    sentence = f"{agent_text.capitalize()} {verb} {subj_text}"
    return sentence


def main():
    text = input("Enter an English sentence: ")
    doc = nlp(text)
    if is_passive(doc):
        print("Detected passive voice. Converting to active...")
        print(convert_passive_to_active(doc))
    else:
        print("Detected active voice. Converting to passive...")
        print(convert_active_to_passive(doc))


if __name__ == '__main__':
    main()
