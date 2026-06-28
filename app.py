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
    # Gelen mesaja hiç bakmadan direkt rastgele bir troll cevap yapıştırıyoruz
    return random.choice(TROLL_RESPONSES)

# Gradio Sohbet Arayüzü Ayarları
demo = gr.ChatInterface(
    fn=troll_chat,
    title="Troll GPT v1",
    description="Her soruya en doğru ve en net cevabı veren yapay zeka (!) sfsjsjjs",
    examples=["Naber?", "Python nedir?", "En iyi oyun hangisi?"],
    theme="soft"
)

if __name__ == "__main__":
    # Render'ın portunu yakalamak için gerekli ayar
    port = int(os.environ.get("PORT", 7860))
    
    # Render üzerinde sorunsuz çalışması için server_name='0.0.0.0' olmalı
    demo.launch(server_name="0.0.0.0", server_port=port)
