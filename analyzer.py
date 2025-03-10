import streamlit as st
import openai
from PIL import Image, ImageDraw, ImageFont
import random

# OpenAI API Key
openai.api_key = "YOUR_OPENAI_API_KEY"

# Initialize OpenAI Client (NEW SYNTAX)
client = openai.OpenAI()

# Streamlit UI
st.title("🎬 AI-Powered Video Title & Thumbnail Generator")

# Input: Video topic
video_topic = st.text_input("📌 Enter your video topic:", "")

# Generate AI-Based Video Titles
if st.button("Generate AI Video Title"):
    prompt = f"Generate 5 engaging, SEO-friendly YouTube video titles for: {video_topic}"
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    titles = response.choices[0].message.content.strip().split("\n")

    st.subheader("📢 Suggested Video Titles:")
    for title in titles:
        st.write(f"✅ {title}")

# Generate Thumbnail Text & Colors
if st.button("Generate Thumbnail Text & Colors"):
    prompt = f"Suggest 3 attention-grabbing phrases & colors for a YouTube thumbnail about: {video_topic}"
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    thumbnail_suggestions = response.choices[0].message.content.strip().split("\n")

    st.subheader("🖼️ Suggested Thumbnail Text & Colors:")
    for suggestion in thumbnail_suggestions:
        st.write(f"🎨 {suggestion}")

# Thumbnail Generator
st.subheader("🎨 Create a Simple Thumbnail")

# Upload background image
uploaded_file = st.file_uploader("Upload a background image for your thumbnail", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    draw = ImageDraw.Draw(image)

    # Choose Random Colors
    colors = ["red", "blue", "yellow", "green", "purple", "orange"]
    text_color = random.choice(colors)

    # Get Text Input
    text = st.text_input("Enter Thumbnail Text:", "🔥 Must Watch!")
    
    # Draw Text on Image
    font = ImageFont.load_default()
    draw.text((50, 50), text, fill=text_color, font=font)

    # Show Image
    st.image(image, caption="Generated Thumbnail", use_column_width=True)

    # Save Option
    if st.button("Save Thumbnail"):
        image.save("thumbnail.png")
        st.success("✅ Thumbnail saved as thumbnail.png")
