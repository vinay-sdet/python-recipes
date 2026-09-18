"""A practical introduction to Python data types for AI learners.

Run this file with:
    python data_types_guide.py
"""

# Basic values
print("1. Basic data types")
name: str = "Ada"
age: int = 36
score: float = 0.97
is_ready: bool = True
missing_value = None

for value in (name, age, score, is_ready, missing_value):
    print(f"{value!r:>6} -> {type(value).__name__}")


# Lists: ordered, changeable collections that may contain duplicates
print("\n2. Lists")
features: list[str] = ["text", "image", "audio", "text"]
print("Original:", features)
print("First feature:", features[0])
print("Last feature:", features[-1])
print("First two features:", features[:2])
features.append("video")
features[0] = "prompt"
print("After append and update:", features)


# Tuples: ordered, fixed collections
print("\n3. Tuples")
model_output: tuple[str, float, bool] = ("cat", 0.98, True)
label, confidence, accepted = model_output
print("Output:", model_output)
print("Unpacked:", label, confidence, accepted)
print("A tuple cannot be changed after creation.")


# Sets: unordered collections of unique values
print("\n4. Sets")
tags: set[str] = {"python", "ai", "python", "data"}
other_tags: set[str] = {"ai", "ml", "vision"}
print("Duplicates removed:", tags)
print("Shared tags:", tags & other_tags)
print("All tags:", tags | other_tags)
print("Tags only in the first set:", tags - other_tags)


# Dictionaries: key-value mappings
print("\n5. Dictionaries")
model: dict[str, object] = {
    "name": "small-classifier",
    "version": 1,
    "accuracy": 0.91,
    "labels": ["spam", "not spam"],
}
print("Model name:", model["name"])
print("Missing key with a default:", model.get("owner", "unknown"))
model["deployed"] = False
for key, value in model.items():
    print(f"{key}: {value}")


# Strings are sequences too, so they support indexing and slicing
print("\n6. Strings")
prompt: str = "Classify this message"
print("First word:", prompt.split()[0])
print("Uppercase:", prompt.upper())
print("Characters 0-6:", prompt[:7])


# Comprehensions create collections from other collections
print("\n7. Comprehensions")
scores: list[float] = [0.82, 0.91, 0.67, 0.95]
high_scores: list[float] = [score for score in scores if score >= 0.9]
score_labels: dict[str, str] = {
    "high" if score >= 0.9 else "needs review": f"{score:.2f}" for score in scores
}
print("High scores:", high_scores)
print("Score labels:", score_labels)


# Nested data: a common shape when working with APIs and datasets
print("\n8. Nested data")
records: list[dict[str, object]] = [
    {"text": "Great product", "label": "positive", "tokens": ["great", "product"]},
    {"text": "Needs work", "label": "negative", "tokens": ["needs", "work"]},
]
print("First record:", records[0])
print("Second record label:", records[1]["label"])


# Choosing a type
print("\n9. Quick guide")
print("list  -> ordered data that may change")
print("tuple -> ordered data that should stay fixed")
print("set   -> unique values and fast membership checks")
print("dict  -> named values stored as key-value pairs")
print("str   -> text")
print("int/float/bool/None -> numbers, truth values, and no value")


# Mutability: lists and dictionaries can change; strings and tuples cannot
print("\n10. Mutability")
mutable_list = ["before"]
mutable_list.append("after")
print("Changed list:", mutable_list)

fixed_tuple = ("before", "after")
print("Fixed tuple:", fixed_tuple)
print("Use a new tuple when you need different values.")
