"""
Basic usage examples for TC Translator
"""

from terminex import Terminex, translate

# Example 1: Basic translation with domain
print("=" * 50)
print("Example 1: Basic Translation")
print("=" * 50)

translator = Terminex()

result = translator.translate(
    "The abattoir uses acaricide for pest control on the acreage",
    target_language="twi",
    domain="agric"
)

print(f"Original: {result.original_text}")
print(f"Translated: {result.translated_text}")
print(f"Terms preserved: {len(result.terms_used)}")
for term in result.terms_used:
    print(f"  - {term['term']} → {term['translation']}")
print()

# Example 2: Translation without domain (uses all glossaries)
print("=" * 50)
print("Example 2: Multi-Domain Translation")
print("=" * 50)

result = translator.translate(
    "Agricultural aeroponics systems can improve acre-foot water efficiency",
    target_language="twi"
)

print(f"Translated: {result.translated_text}")
print(f"Terms used: {[t['term'] for t in result.terms_used]}")
print()

# Example 3: Check available languages and domains
print("=" * 50)
print("Example 3: Available Resources")
print("=" * 50)

print(f"Available languages: {translator.available_languages()}")
print(f"Available domains: {translator.available_domains()}")
print(f"Domains for 'twi': {translator.available_domains('twi')}")
print()

# Example 4: Batch translation
print("=" * 50)
print("Example 4: Batch Translation")
print("=" * 50)

texts = [
    "The abattoir processes livestock",
    "Apply acaricide to control pests",
    "Measure the acreage accurately"
]

results = translator.translate(texts, target_language="twi", domain="agric")

for i, result in enumerate(results, 1):
    print(f"{i}. {result.original_text}")
    print(f"   → {result.translated_text}")
print()

# Example 5: API-compatible function
print("=" * 50)
print("Example 5: API-Compatible Interface")
print("=" * 50)

result = translate("The adjuvant improves pesticide effectiveness", dest="twi", domain="agric")
print(f"Text: {result.text}")
print(f"Source: {result.src} → Dest: {result.dest}")
print(f"Terms used: {result.extra_data['terms_used']}")
