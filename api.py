from google import genai

client = genai.Client(api_key="key")

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="what is api"
)
print("status code:", interaction.status_code)
print("output text:", interaction.output_text)