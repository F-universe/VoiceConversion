VoiceConversion

A CLI tool that converts English sentences between active and passive voice.

Brief Description

Active voice: the subject performs the action (e.g., "The cat chased the mouse.")
Passive voice: the subject receives the action (e.g., "The mouse was chased by the cat.")
VoiceConversion detects the voice of an input sentence and transforms it into the opposite voice.

Requirements

Python 3.7+

spaCy library and the English model

Installation

pip install spacy
python -m spacy download en_core_web_sm

Usage

python voice_conversion.py

Enter a sentence in English.

The script prints whether it was active or passive and outputs the converted sentence.

Customization

Tweak auxiliary verb forms in AUX_FORMS if needed.

Extend heuristics in is_passive to handle more complex constructions.
