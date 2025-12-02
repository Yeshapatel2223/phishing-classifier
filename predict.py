import pickle
import numpy as np
import pandas as pd

# Model file path
MODEL_PATH = r"model.pkl"

# Load trained model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# --------------------------------------
# Feature columns used in training
# (Result removed)
# --------------------------------------
columns = [
    'having_IP_Address',
    'URL_Length',
    'Shortining_Service',
    'having_At_Symbol',
    'double_slash_redirecting',
    'Prefix_Suffix',
    'having_Sub_Domain',
    'SSLfinal_State',
    'Domain_registeration_length',
    'Favicon',
    'port',
    'HTTPS_token',
    'Request_URL',
    'URL_of_Anchor',
    'Links_in_tags',
    'SFH',
    'Submitting_to_email',
    'Abnormal_URL',
    'Redirect',
    'on_mouseover',
    'RightClick',
    'popUpWidnow',
    'Iframe',
    'age_of_domain',
    'DNSRecord',
    'web_traffic',
    'Page_Rank',
    'Google_Index',
    'Links_pointing_to_page',
    'Statistical_report'
]

# --------------------------------------
# Sample input (dummy values)
# Replace with your real values
# --------------------------------------
sample_input = {
    'having_IP_Address': -1,
    'URL_Length': 1,
    'Shortining_Service': 1,
    'having_At_Symbol': 1,
    'double_slash_redirecting': -1,
    'Prefix_Suffix': -1,
    'having_Sub_Domain': 0,
    'SSLfinal_State': -1,
    'Domain_registeration_length': -1,
    'Favicon': 1,
    'port': 1,
    'HTTPS_token': -1,
    'Request_URL': 0,
    'URL_of_Anchor': -1,
    'Links_in_tags': 1,
    'SFH': -1,
    'Submitting_to_email': -1,
    'Abnormal_URL': 1,
    'Redirect': 1,
    'on_mouseover': -1,
    'RightClick': 1,
    'popUpWidnow': -1,
    'Iframe': 1,
    'age_of_domain': 1,
    'DNSRecord': 1,
    'web_traffic': -1,
    'Page_Rank': -1,
    'Google_Index': 1,
    'Links_pointing_to_page': -1,
    'Statistical_report': 1
}

# Convert to DataFrame (column order MUST match)
input_df = pd.DataFrame([sample_input], columns=columns)

# Prediction
pred = model.predict(input_df)[0]

print("\n==============================")
print("🔍 Phishing Prediction Result")
print("==============================")
print("\nInput Features:")
print(input_df)
print("\n⚡ MODEL OUTPUT:", pred)

if pred == 1:
    print("\n💀 This Website is PHISHING!")
else:
    print("\n🛡️ Website is SAFE!")
