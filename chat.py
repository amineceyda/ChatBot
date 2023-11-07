import random
import json
import torch
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
import streamlit as st

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "VT"
st.title("Kampanya Botu")

# Kullanıcıdan metin girişi al
user_input = st.text_input("Sen:", "")

if user_input:
    sentence = tokenize(user_input)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    response = ""
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                break
    else:
        response = "Üzgünüm, sizi anlayamadım. Daha farklı açıklar mısınız?"

    st.text(f"Bot: {response}")


# "Öneriler" başlığı altında kampanya başlıklarını göster

st.header("Öneriler")
for intent in intents['intents']:
    if intent["tag"].startswith("campaign_"):
        campaign_title = intent["patterns"][0]  # Kampanya başlığını ilk pattern olarak alabilirsiniz
        if st.button(campaign_title):
            # Kullanıcı kampanyaya tıkladığında kampanya detaylarını göster
            st.subheader(campaign_title)
            response = random.choice(intent['responses'])
            st.write(response)