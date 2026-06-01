import gradio as gr
from app.services.ai_tutor import stream_ai_tutor_response


def create_interface():
    return gr.Interface(
        fn=stream_ai_tutor_response,
        inputs=gr.Textbox(
            lines=2,
            placeholder="Ask the AI Tutor anything...",
            label="Your Question",
        ),
        outputs=gr.Markdown(
            label="AI Tutor's Answer (Streaming)"
        ),
        title="🤖 AI Tutor with Streaming",
        description="Enter your question. The answer will appear word-by-word!",
    )