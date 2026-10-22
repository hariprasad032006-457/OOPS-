"""Introductory Google Gen AI SDK example.

Install: pip install google-genai
Set GOOGLE_API_KEY in your environment before running.
"""


def main():
    try:
        from google import genai
    except ImportError as exc:
        raise SystemExit(
            "Google Gen AI SDK is missing. Install it with: pip install google-genai"
        ) from exc

    # The SDK reads GOOGLE_API_KEY from the environment.
    client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain what an API is in simple English."
    )
    print(response.text)


if __name__ == "__main__":
    main()
