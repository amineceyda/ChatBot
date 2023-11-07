# ChatBot
## Proje Hakkında

Bu proje, bir doğal dil işleme (NLP) modeli kullanarak bir sohbet botunu eğitmek ve kullanmak amacıyla oluşturulmuştur. Sohbet botu, belirli niyetlere (örneğin, "selam verme" veya "kampanyalar hakkında bilgi verme") yanıt verebilmektedir. Bu README dosyası, projeyi çalıştırmak ve kullanmak için gerekli talimatları içerir.

[https://vtchatbot.streamlit.app/](https://vtchatbot.streamlit.app/)

## Kurulum

Bu projeyi yerel bir geliştirme ortamında çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Projeyi klonlayın:

   ```bash
   git clone https://github.com/amineceyda/ChatBot
   cd ChatBot

2. ChatBot klasörüne gerekli veri setini ekleyin:
   Bu proje, bir CSV veri setini kullanır. Veri seti, projenin tekrar düzenlenmesi için gereklidir. CSV veri setini aşağıdaki linkte bulabilirsiniz.
   
   [hackathon_data](https://drive.google.com/file/d/1eL7C9aW4rg_RlJsDoMasvqs2MnSAIGek/view?usp=drive_link).
   
## Sanal Ortamı Aktifleştirmek

Proje klasörünüzdeki sanal ortamı aktifleştirmek için aşağıdaki adımları izleyebilirsiniz:

1. Proje klasörünüzde bir komut istemcisini açın.

2. Sanal ortamı aktifleştirin (örnek olarak Windows için):

   ```bash
   env\Scripts\activate

  - veya Linux/Mac için:
    
    ```bash
    source env/bin/activate

3. Sanal ortam başarıyla aktifleştirildiğinde, proje bağımlılıkları bu izole edilmiş ortamda çalışır.

Projeyle etkileşime girmek için aşağıdaki komutları kullanabilirsiniz:

- Gerekli bağımlılıkları yüklemek için:
  
    ```bash
    pip install -r requirements.txt

- Eğitim betiği çalıştırmak için:

  ```bash
  python train.py
  
- Sohbet arayüzünü başlatmak için:
  
  ```bash
  streamlit run chat.py

-Sanal ortamı deaktifleştirmek için:
  
  ```bash
    deactive
```

## Veri Eğitimi

Bu projenin bir parçası olarak, eğitilmiş bir NLP modeli gereklidir. Veri eğitimi aşağıdaki adımları içerir:

intents.json dosyası, belirli niyetler (intents) ve bu niyetlere ait örüntüleri içerir.

train.py dosyası, veriyi işler, bir model eğitir ve sonucu data.pth adlı bir dosyada kaydeder.

Veri eğitimi sırasında, belirli bir niyeti tanımak ve buna uygun yanıtlamak için eğitilmiş bir model oluşturulur.

#### Kullanım
  
  Sohbet botu, belirli komutlar kullanarak kullanıcıyla etkileşimde bulunabilir. Örnek kullanımlar:

  Kampanyalar hakkında konuşmak için "Kampanyalar hakkında konuşmak ister misiniz?" yazın.

  Bu komutlar, sohbet botunun belirli soruları tanımasına ve buna göre yanıt vermesine yardımcı olur.
  
## Yeni Kampanya Niyetleri Oluşturmak

Bu projenin bir parçası olarak, belirli gruplara göre kampanya promosyonları oluşturmak için bir araç bulunmaktadır. Bu araç, veri kaynaklarından (örneğin, bir CSV dosyasından) alınan verileri kullanarak yeni niyetler oluşturur.

### Kullanım

Yeni kampanya niyetleri oluşturmak için aşağıdaki adımları izleyebilirsiniz:

1. `csv_data_preprocessing.py` dosyasını kullanarak verileri ön işleyin ve `data` adlı bir veri çerçevesi elde edin.

2. `generate_campaign_promotions` fonksiyonunu kullanarak kampanya promosyonlarını oluşturun ve bu promosyonları `intents.json` dosyasına ekleyin.

Örnek kullanım:

```python
import pandas as pd
import json
from csv_data_preprocessing import data

# Open and read the intents.json file
with open('intents.json', 'r', encoding='utf-8') as f:
    intents_data = json.load(f)

# Generate campaign promotions by groups
def generate_campaign_promotions(data, intents_data):
    # ...
    # (Kodun geri kalanı)
    # ...

generate_campaign_promotions(data, intents_data)
```
#### Dikkat
Kampanya promosyonlarını oluşturmadan önce verilerin uygun bir şekilde işlendiğinden emin olun. Verileri işlemek için csv_data_preprocessing.py dosyasını kullanabilirsiniz.



  
  
