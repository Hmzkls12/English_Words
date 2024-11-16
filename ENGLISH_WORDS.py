import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Çevre değişkenlerini yükle
load_dotenv()

# Generative AI'yi API anahtarı ile yapılandır
API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=API_KEY)

# Generative modeli başlat
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "Girilen ingilizce kelimelerle anlamlı bir ingilizce cümle üret. Verdiğim kelimelerle yeterince anlamlı bir cümle üretmekte zorlanırsan kendin kelime ekle. İlk başta oluşturduğun ingilizce cümleyi yaz sonra da cümlenin türkçesini yaz. Sonra da bu ingilice cümlenin içinde ki her bir kelimenin ingilicesini ve türkçesini bir tablo içinde yaz."

# Streamlit uygulaması
st.title('İngilizce Kelime Öğren')
st.write('Öğrenmek istediğin ingilizce kelimeleri virgül"," ile ayırarak yaz.')

if 'history' not in st.session_state:
    st.session_state.history = []

# Bir metin giriş widget'ı oluştur
user_input = st.text_input("Kelimeler:", key="user_input")

if st.button("Send"):
    if user_input.strip() != '':
        response = chat.send_message(user_input + instruction)
        st.session_state.history.append(("Kelimeler", user_input))
        st.session_state.history.append(("Bot", response.text))
        st.experimental_rerun()  # Metin alanını temizlemek için uygulamayı yeniden çalıştır

for sender, message in st.session_state.history:
    if sender == "Kelimeler":
        st.markdown(f"**Kelimeler:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")


#çalıştırmak için
#python -m streamlit run ENGLISH_WORDS.py