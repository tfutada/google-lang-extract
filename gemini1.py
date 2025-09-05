from google import genai
from google.genai.types import GenerateContentConfig

# Initialize client
client = genai.Client()

# Call Gemini model with URL context
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Tell me about: https://ai.google.dev",
    config=GenerateContentConfig(
        tools=[{"url_context": {}}]
    )
)

# Print the response text
print(response.text)
