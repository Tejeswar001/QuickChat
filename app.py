import gradio as gr
from gemini_client import query_gemini
from sheets_logger import log_message

# -------- Chat State --------
def respond(user_message, history):
    if not user_message.strip():
        return history, ""

    bot_reply = query_gemini(user_message, history)

    if not bot_reply:
        bot_reply = "⚠️ No response from model."

    # Log to Google Sheets
    try:
        log_message(user_message, bot_reply)
    except Exception as e:
        print("Sheets logging failed:", e)

    history = history + [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": bot_reply}
    ]

    return history, ""


def clear_chat():
    return [], ""


# -------- UI --------
with gr.Blocks() as demo:

    gr.Markdown(
        """
        # AI ChatBot  
        Building open-domain chatbots is a challenging area for machine learning research.
        """
    )

    with gr.Row():
        # -------- Left Panel --------
        with gr.Column(scale=1):
            gr.Markdown("### input")

            user_input = gr.Textbox(
                placeholder="What you think about love?",
                lines=2,
                show_label=False
            )

            with gr.Row():
                clear_btn = gr.Button("Clear", variant="secondary")
                submit_btn = gr.Button("Submit", variant="primary")

        # -------- Right Panel --------
        with gr.Column(scale=1):
            gr.Markdown("### output")

            chatbot = gr.Chatbot(
                label="",
                height=420
            )

    gr.Markdown("### Examples")
    example_btn = gr.Button("How are you?")

    # -------- Events --------
    submit_btn.click(
        respond,
        inputs=[user_input, chatbot],
        outputs=[chatbot, user_input]
    )

    user_input.submit(
        respond,
        inputs=[user_input, chatbot],
        outputs=[chatbot, user_input]
    )

    clear_btn.click(
        clear_chat,
        outputs=[chatbot, user_input]
    )

    example_btn.click(
        lambda: "How are you?",
        outputs=user_input
    )


# Theme moved to launch() in Gradio 6.x
demo.launch(theme=gr.themes.Soft(primary_hue="purple"),share=True)
