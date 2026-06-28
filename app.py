import os
import random
import gradio as gr

# Troll cevap havuzu
TROLL_RESPONSES = [
    "Ben bilmem, git Gemini'a sor!",
    "Bana niye soruyon? Git Gemini'a sor, o daha akıllı.",
    "Burası danışma mı kardeşim? Ahan da Gemini orada, ona sor.",
    "Şu an çok meşgulüm, sorunu kopyala ve doğruca Gemini'a yapıştır.",
    "Bu sorunun cevabı bende değil, Gemini abime sor.",
    "Yahu her şeyi bana sormaktan bıkmadınız mı? Git Gemini'a yaz."
]

def troll_chat(message, history):
    return random.choice(TROLL_RESPONSES)

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        "# Troll GPT v1\n"
        "Her soruya en doğru ve en net cevabı veren yapay zeka (!) 😄"
    )

    gr.ChatInterface(
        fn=troll_chat,
        type="messages"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        show_error=True
    )
