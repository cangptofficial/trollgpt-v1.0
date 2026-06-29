import os
import random
import gradio as gr

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

# Gradio 5.x uyumlu ChatInterface yapısı
with gr.Blocks() as demo:
    gr.Markdown("# Troll GPT v1\nHer soruya en doğru ve en net cevabı veren yapay zeka (!) sfsjsjjs")
    gr.ChatInterface(fn=troll_chat, theme="soft")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    
    # launch() içindeki queue=False parametresini kaldırdık.
    # Gradio 5 artık WebSocket yerine Render dostu SSE (Server-Sent Events) kullandığı için
    # canlı kuyruk açık olsa bile Render üzerinde bağlantı hatası vermez.
    demo.launch(
        server_name="0.0.0.0", 
        server_port=port, 
        show_error=True
    )
