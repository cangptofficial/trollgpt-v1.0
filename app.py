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

# Gradio 4'te chat fonksiyonu sadece botun vereceği metni (string) döner, gerisini arayüz halleder.
def troll_chat(message, history):
    return random.choice(TROLL_RESPONSES)

# O sade ve şık ChatInterface yapısına geri döndük
with gr.Blocks(theme="soft") as demo:
    gr.Markdown("# Troll GPT v1\nHer soruya en doğru ve en net cevabı veren yapay zeka (!) sfsjsjjs")
    gr.ChatInterface(fn=troll_chat)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    
    # queue=False Gradio 4'te hata vermez, aksine Render'ın bağlantıyı koparmasını ENGELLER.
    demo.launch(
        server_name="0.0.0.0", 
        server_port=port, 
        show_error=True,
        queue=False
    )
