from google import genai
from google.genai.errors import APIError
from dotenv import load_dotenv
import os
import time


load_dotenv()


def create_client():
    """Create the Gemini API client."""
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set in the .env file."
        )

    return genai.Client(api_key=api_key)


def generate_answer(client, query, retrieved_chunks):
    """
    Generate an answer using only the retrieved document context.
    """

    if not retrieved_chunks:
        return "I couldn't find relevant information in the provided documents."

    context_parts = []

    for chunk in retrieved_chunks:
        source = chunk["source"]
        page = chunk.get("page")

        if page:
            location = f"{source}, page {page}"
        else:
            location = source

        context_parts.append(
            f"Source: {location}\n"
            f"Content: {chunk['text']}"
        )

    context = "\n\n---\n\n".join(context_parts)

    prompt = f"""
You are a document question-answering assistant.

Answer the user's question using ONLY the information provided
in the retrieved document context below.

Do not use outside knowledge.

If the answer cannot be found in the context, say:
"I couldn't find this information in the provided documents."

Be concise and clear.

User question:
{query}

Retrieved document context:
{context}
"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
            )

            return response.text

        except APIError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == 2:
                print(f"\nGemini API error: {error}")
                return (
                    "The Gemini API is temporarily unavailable. "
                    "Please try again later."
                )

            time.sleep(2 ** attempt)

        except Exception as error:
            print(f"\nUnexpected Gemini error: {error}")
            return "The answer could not be generated because an unexpected error occurred."