import os
import random
import gradio as gr
from fastapi import FastAPI

# Troll cevap havuzumuz
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

# Gradio Arayüzü
io = gr.ChatInterface(
    fn=troll_chat,
    title="Troll GPT v1",
    description="Her soruya en doğru ve en net cevabı veren yapay zeka (!) sfsjsjjs",
    theme="soft"
)

# FastAPI uygulamasını başlatıyoruz
app = FastAPI()

# Gradio'yu FastAPI içine gömüyoruz (Bağlantı kopmalarını engeller)
app = gr.mount_gradio_app(app, io, path="/")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)
