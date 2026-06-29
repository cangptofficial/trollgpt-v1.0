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
    if history is None:
        history = []

    bot_response = random.choice(TROLL_RESPONSES)

    # Gradio 5'in modern mesaj formatı
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": bot_response})

    # İlk değer mesaj kutusunu temizler, ikinci değer sohbet geçmişini günceller
    return "", history

# ChatInterface yerine Blocks kullanarak Render dostu bir yapı kuruyoruz
with gr.Blocks(theme="soft") as demo:
    gr.Markdown("# Troll GPT v1\nHer soruya en doğru ve en net cevabı veren yapay zeka (!) sfsjsjjs")

    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(placeholder="Bir şeyler yaz ve Enter'a bas...")

    # Tetikleyici (Enter'a basınca çalışır)
    # queue=False BURADA (event'in kendisinde) veriliyor.
    # Gradio 4/5'te bu parametre launch()'tan kaldırıldı; queue'yu
    # event bazında kapatmak için doğru yer burası.
    msg.submit(
        fn=troll_chat,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot],
        queue=False,
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))

    # NOT: launch() artık 'queue' parametresi almıyor (Gradio 4.0'da
    # enable_queue ile birlikte kaldırıldı). Queue'yu kapatmak istiyorsan
    # bunu yukarıdaki .submit() çağrısında yapman gerekiyor.
    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        show_error=True,
    )
