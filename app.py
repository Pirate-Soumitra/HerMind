# app.py

import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from visualization import visualize_user_input, show_radar_chart

# Load model and scaler
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('model/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Function to predict mental health status
def predict_health_status(features):
    scaled_features = scaler.transform([features])
    prediction = model.predict(scaled_features)
    return prediction

def main():
    st.set_page_config(page_title="HerMind - Women Mental Health", page_icon="🧠", layout="centered")

    st.markdown("""
        <style>
            .title {
                font-size:40px !important;
                color:#D63384;
                text-align:center;
                margin-bottom:20px;
            }
            .stSelectbox label {
                font-weight:600 !important;
                color:#6C757D;
            }
            .predict-button {
                background-color: #D63384;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 20px;
                margin-top: 20px;
            }
            .result {
                font-size: 24px;
                font-weight: bold;
                color: #20C997;
                margin-top: 30px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">🌸 HerMind - Women Mental Health 🌸</div>', unsafe_allow_html=True)

    st.subheader("📚 Academic Details")
    academic_status_map = {
        "Never Attended": 0,
        "Attended": 1,
        "Drop Out": 2,
        "Currently Attending": 3
    }
    academic_status = academic_status_map[st.selectbox("Academic Status 🎓", list(academic_status_map.keys()))]

    academic_performance_map = {
        "Poor": 0,
        "Average": 1,
        "Good": 2
    }
    academic_performance = academic_performance_map[st.selectbox("Academic Performance 📖", list(academic_performance_map.keys()))]

    st.subheader("📱 Lifestyle & Social Factors")
    social_media_exposure_map = {
        "Nil": 0,
        "Rarely": 1,
        "Frequently": 2
    }
    social_media_exposure = social_media_exposure_map[st.selectbox("Social Media Exposure 📱", list(social_media_exposure_map.keys()))]

    physical_abuse_map = {
        "No": 0,
        "Yes": 1
    }
    physical_abuse = physical_abuse_map[st.selectbox("Physical Abuse 🚫", list(physical_abuse_map.keys()))]

    sexual_abuse_map = {
        "No": 0,
        "Yes": 1
    }
    sexual_abuse = sexual_abuse_map[st.selectbox("Sexual Abuse 🚫", list(sexual_abuse_map.keys()))]

    st.subheader("👨‍👩‍👧 Communication & Freedom")
    communication_with_parents_map = {
        "Difficult": 0,
        "Easy": 1
    }
    communication_with_parents = communication_with_parents_map[st.selectbox("Communication with Parents 🧓", list(communication_with_parents_map.keys()))]

    communication_with_friends_map = {
        "Difficult": 0,
        "Easy": 1
    }
    communication_with_friends = communication_with_friends_map[st.selectbox("Communication with Friends 👭", list(communication_with_friends_map.keys()))]

    freedom_to_move_map = {
        "No": 0,
        "Yes": 1
    }
    freedom_to_move = freedom_to_move_map[st.selectbox("Freedom to Move 🚶‍♀️", list(freedom_to_move_map.keys()))]

    expression_of_opinion_map = {
        "No": 0,
        "Yes": 1
    }
    expression_of_opinion = expression_of_opinion_map[st.selectbox("Expression of Opinion 🗣️", list(expression_of_opinion_map.keys()))]

    confront_wrong_acts_map = {
        "No": 0,
        "Yes": 1
    }
    confront_wrong_acts = confront_wrong_acts_map[st.selectbox("Confront Wrong Acts 💪", list(confront_wrong_acts_map.keys()))]

    st.subheader("💍 Relationship & Family")
    engaged_marriage_decided_map = {
        "No": 0,
        "Yes": 1
    }
    engaged_marriage_decided = engaged_marriage_decided_map[st.selectbox("Engaged / Marriage Decided 💍", list(engaged_marriage_decided_map.keys()))]

    discussion_sexual_problems_map = {
        "No": 0,
        "Yes": 1
    }
    discussion_sexual_problems = discussion_sexual_problems_map[st.selectbox("Discussion about Sexual Problems in Family 💬", list(discussion_sexual_problems_map.keys()))]

    discussion_relationships_in_family_map = {
        "No": 0,
        "Yes": 1
    }
    discussion_relationships_in_family = discussion_relationships_in_family_map[st.selectbox("Discussion about Relationships in Family 🏠", list(discussion_relationships_in_family_map.keys()))]

    st.subheader("🩺 Health & Emotions")
    medical_symptoms_map = {
        "Nil": 0,
        "Mild": 1,
        "Moderate": 2,
        "Severe": 3
    }
    medical_symptoms = medical_symptoms_map[st.selectbox("Medical Symptoms 🤒", list(medical_symptoms_map.keys()))]

    impulsive_aggressive_behavior_map = {
        "No": 0,
        "Yes": 1
    }
    impulsive_aggressive_behavior = impulsive_aggressive_behavior_map[st.selectbox("Impulsive / Aggressive Behavior 😡", list(impulsive_aggressive_behavior_map.keys()))]

    family_problems_map = {
        "No": 0,
        "Yes": 1
    }
    family_problems = family_problems_map[st.selectbox("Family Problems 🏚️", list(family_problems_map.keys()))]

    divorce_map = {
        "No": 0,
        "Yes": 1
    }
    divorce = divorce_map[st.selectbox("Divorce in Family 💔", list(divorce_map.keys()))]

    partner_abuse_map = {
        "No": 0,
        "Yes": 1
    }
    partner_abuse = partner_abuse_map[st.selectbox("Partner Abuse 🚷", list(partner_abuse_map.keys()))]

    substance_abuse_map = {
        "No": 0,
        "Yes": 1
    }
    substance_abuse = substance_abuse_map[st.selectbox("Substance Abuse 🍷", list(substance_abuse_map.keys()))]

    relationship_problems_map = {
        "No": 0,
        "Yes": 1
    }
    relationship_problems = relationship_problems_map[st.selectbox("Relationship Problems ❤️‍🩹", list(relationship_problems_map.keys()))]

    peer_pressure_map = {
        "No": 0,
        "Yes": 1
    }
    peer_pressure = peer_pressure_map[st.selectbox("Peer Pressure 🤯", list(peer_pressure_map.keys()))]

    # Collecting features
    features = np.array([academic_status, academic_performance, social_media_exposure, 
                         physical_abuse, sexual_abuse, communication_with_parents, 
                         communication_with_friends, freedom_to_move, expression_of_opinion, 
                         confront_wrong_acts, engaged_marriage_decided, discussion_sexual_problems,
                         discussion_relationships_in_family, medical_symptoms, 
                         impulsive_aggressive_behavior, family_problems, divorce, partner_abuse, 
                         substance_abuse, relationship_problems, peer_pressure])

    if st.button("💬 Am I Depressed ?"):
        prediction_label_map = {
            0: "🧘 No, my dear, you're not. Stay positive and keep shining! 🌟",
            1: "🆘 Yes, my dear, please seek help. You are not alone. 💖"
        }
        prediction = predict_health_status(features)
        predicted_label = prediction_label_map.get(prediction[0], "Unknown")
        st.markdown(f'<div class="result">{predicted_label}</div>', unsafe_allow_html=True)

        # Show visualizations
        visualize_user_input(features)
        show_radar_chart(features)

if __name__ == "__main__":
    main()