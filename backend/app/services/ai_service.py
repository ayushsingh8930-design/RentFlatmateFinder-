import json
import google.generativeai as genai

from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

def gemini_score(tenant, property):
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
        Given this room listing:

        City: {property.city}
        Rent: {property.rent}

        And this tenant profile:

        Preferred Location: {tenant.preferred_location}
        Budget: {tenant.budget}

        Return ONLY valid JSON:

        {{
          "score": 85,
          "explanation": "Short explanation"
        }}
        """

        response = model.generate_content(prompt)
        print("Gemini Response:", response.text)

        text = response.text.strip()

        if text.startswith("```json"):
          text = text.replace("```json", "", 1)

        if text.endswith("```"):
          text = text[:-3]

        text = text.strip()

        return json.loads(text)

    except Exception as e:
        print(f"Gemini Error: {e}")
        return rule_based_score(tenant, property)


def rule_based_score(tenant, property):

    score = 0
    explanation = []

    if tenant.preferred_location.lower() == property.city.lower():
        score += 50
        explanation.append("Location matched.")

    if tenant.budget >= property.rent:
        score += 50
        explanation.append("Budget matched.")

    return {
        "score": score,
        "explanation": " ".join(explanation)
    }