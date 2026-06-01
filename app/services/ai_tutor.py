from app.config import client


def stream_ai_tutor_response(user_question):
    system_prompt = (
        "You are a helpful and patient AI Tutor. "
        "Explain concepts clearly and concisely."
    )

    try:
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_question},
            ],
            temperature=0.7,
            stream=True,
        )

        full_response = ""

        for chunk in stream:
            if (
                chunk.choices[0].delta
                and chunk.choices[0].delta.content
            ):
                text_chunk = chunk.choices[0].delta.content
                full_response += text_chunk
                yield full_response

    except Exception as e:
        yield f"Error: {e}"