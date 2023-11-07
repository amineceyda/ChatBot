import pandas as pd
import json
from csv_data_preprocessing import data

# Open and read the intents.json file
with open('intents.json', 'r', encoding='utf-8') as f:
    intents_data = json.load(f)

# Generate campaign promotions by groups
def generate_campaign_promotions(data, intents_data):
    campaign_promotions = {
        "campaigns": []
    }

    # Group by City
    city_groups = data.groupby('Sehir')
    for city, city_data in city_groups:

        campaign = {
            "pattern":f"{city}",
            "tag": f"{city}DiscountCampaign",
            "response": f"{city}'deki %10 indirim fırsatını kaçırmayın!"
        }
        campaign_promotions["campaigns"].append(campaign)


    business_type_groups = data.groupby('IsyeriTipi')
    for business_type, business_type_data in business_type_groups:

        campaign = {
            "pattern": f"{business_type} için özel kampanyalar",
            "tag": f"{business_type}Campaign",
            "response": f"{business_type} işletmelerindeki %20 indirim fırsatını kaçırmayın!"
        }
        campaign_promotions["campaigns"].append(campaign)

    membership_status_groups = data.groupby('UyeDurum')
    for membership_status, membership_status_data in membership_status_groups:
        campaign = {
            "pattern": f"{membership_status} kullanıcılara kampanya",
            "tag": f"{membership_status}Campaign",
            "response": f"{membership_status} üyeleri için sürpriz kampanyayı kaçırmayın! İkinci ürün %50 indirimli"
        }
        campaign_promotions["campaigns"].append(campaign)

    for campaign in campaign_promotions["campaigns"]:
        intents_data["intents"].append({
            "tag": campaign["tag"],
            "patterns": [campaign["pattern"]],
            "responses": [campaign["response"]]
        })

    #kaydet
    with open('intents.json', 'w', encoding='utf-8') as json_file:
        json.dump(intents_data, json_file, ensure_ascii=False)

generate_campaign_promotions(data, intents_data)
