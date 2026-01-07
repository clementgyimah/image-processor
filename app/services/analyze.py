import random

def analyze_image(image_id: str):
    # example skin types
    skin_types = ["Normal", "Oily", "Dry", "Combination",  "Sensitive"]
    # example skin issues
    issues_list = ["Hyperpigmentation", "Acne", "Redness", "Eczema", "Aging", "None"]

    return {
        "image_id": image_id,
        "skin_type": random.choice(skin_types),
        "issues": random.sample(issues_list, k=1),
        "confidence": round(random.uniform(0.7, 0.99), 2)
    }
