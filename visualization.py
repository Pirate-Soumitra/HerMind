# visualization.py

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def visualize_user_input(features):
    feature_names = [
        "Academic Status", "Academic Performance", "Social Media Exposure",
        "Physical Abuse", "Sexual Abuse", "Comm. w/ Parents", "Comm. w/ Friends",
        "Freedom to Move", "Opinion Expression", "Confront Wrong Acts",
        "Marriage Decided", "Sexual Discussion", "Relationship Discussion",
        "Medical Symptoms", "Impulsive Behavior", "Family Problems", "Divorce",
        "Partner Abuse", "Substance Abuse", "Relationship Problems", "Peer Pressure"
    ]

    # Normalize values between 0 and 1 for better visualization
    norm_features = np.array(features) / max(max(features), 1)

    st.subheader("📊 Your Psychological & Social Profile")

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=norm_features, y=feature_names, palette="magma", ax=ax)
    ax.set_title("User Profile Factors", fontsize=16, weight='bold')
    ax.set_xlabel("Severity / Exposure Level", fontsize=12)
    st.pyplot(fig)

def show_radar_chart(features):
    feature_categories = {
        "Academics": features[0:2],
        "Social Media": [features[2]],
        "Abuse": features[3:5],
        "Communication": features[5:7],
        "Freedom": features[7:10],
        "Family Talk": features[10:13],
        "Health": [features[13]],
        "Aggression": [features[14]],
        "Family Issues": features[15:17],
        "Toxic Relationships": features[17:21]
    }

    categories = list(feature_categories.keys())
    values = [np.mean(vals) for vals in feature_categories.values()]

    values += values[:1]  # to close the radar loop

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2, linestyle='solid')
    ax.fill(angles, values, 'pink', alpha=0.3)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_title("🧠 Mental Health Risk Radar", fontsize=14, weight='bold', pad=20)
    st.pyplot(fig)
