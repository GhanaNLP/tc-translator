#!/usr/bin/env python3
"""
Basic usage examples for TC Translator
"""

from tc_translate import TCTranslator, Translator

# Example 1: Using TCTranslator for agriculture domain
print("=== Example 1: Agriculture Translation ===")
agric_translator = TCTranslator(domain='agric', target_lang='twi')

text = "The farmer uses an abattoir and manages his acreage efficiently."
result = agric_translator.translate(text)

print(f"Original: {result['original']}")
print(f"Translated: {result['text']}")
print(f"Terms replaced: {result['replacements_count']}")
print()

# Example 2: Using the Google Translate-like API
print("=== Example 2: Google Translate-like API ===")
translator = Translator()

# With terminology control
result_with_terms = translator.translate(
    "acaricide and adjuvant are important",
    src='en',
    dest='twi',
    domain='agric'
)
print(f"With terminology control: {result_with_terms['text']}")

# Without terminology control (regular Google Translate)
result_without_terms = translator.translate(
    "acaricide and adjuvant are important",
    src='en',
    dest='twi'
)
print(f"Without terminology control: {result_without_terms['text']}")
print()

# Example 3: Batch translation
print("=== Example 3: Batch Translation ===")
texts = [
    "abattoir for animals",
    "acreage measurement",
    "aerial seeding method"
]

batch_results = agric_translator.batch_translate(texts)
for i, result in enumerate(batch_results):
    print(f"{i+1}. {result['original']} → {result['text']}")
