import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Career Guidance Chatbot", layout="wide")

# --- SESSION STATE ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- INTENTS ---
intents = {
    "What careers can I pursue with maths and science?": "You can explore careers like Engineering 🛠️, Data Science 📊, Medicine 🩺, or Architecture 🏛️.",
    "What if I enjoy helping others?": "You might enjoy careers in Social Work 🤝, Teaching 👩‍🏫, Nursing 🏥, or Psychology 🧠.",
    "What jobs are in high demand in South Africa?": "Tech 👨‍💻, Healthcare 🩺, Education 📘, and Green Energy 🌱 sectors are booming!",
    "I love working with computers": "You might enjoy Software Development 💻, Cybersecurity 🔐, AI 🤖, or IT Support 🧰.",
    "I enjoy drawing and design": "Consider careers in Graphic Design 🎨, Architecture 🏛️, Animation 🧞, or Fashion Design 👗."
}

# --- SIDEBAR: INTERESTS ---
st.sidebar.header(" Your Preferences")
fav_subjects = st.sidebar.multiselect("Top 3 Subjects", ["Maths", "Science", "English", "History", "Geography", "Art", "Computer Studies", "Business Studies", "Life Sciences", "Economics"])
interests = st.sidebar.multiselect("Areas of Interest", ["Technology", "Healthcare", "Arts & Design", "Business", "Law & Politics", "Social Work", "Environment & Nature", "Education", "Science & Research"])
skills = st.sidebar.multiselect("Your Strengths", ["Creative Thinking", "Problem-Solving", "Teamwork", "Writing", "Communication", "Coding", "Analysing", "Hands-on Tasks"])
personality = st.sidebar.selectbox("Your Personality Type", ["Choose...", "Introvert", "Extrovert", "Creative", "Analytical", "Empathetic", "Logical"])
values = st.sidebar.multiselect("What matters to you in a job?", ["Helping Others", "High Salary", "Work-Life Balance", "Innovation", "Stability", "Flexibility", "Leadership", "Creativity"])

# --- HEADER ---
st.title(" Career Guidance Chatbot")
st.markdown("Click a quick question or ask your own below. The bot replies instantly using predefined logic and smart suggestions.")

# --- QUICK QUESTIONS ---
st.subheader(" Quick Questions")
cols = st.columns(3)
clicked_intent = None
for i, question in enumerate(list(intents.keys())):
    if cols[i % 3].button(question):
        clicked_intent = question

# --- USER INPUT ---
st.subheader(" Ask Your Own Question")
user_input = st.text_input("Type your question and press Enter:")

# --- DETECT INTENT OR AI-LIKE LOGIC ---
def get_bot_reply(user_message):
    if user_message in intents:
        return intents[user_message]
    else:
        keywords = {
            "math": "Consider engineering, data science, or accounting 💼.",
            "help": "You might like social work, teaching or counselling 🤝.",
            "design": "Try graphic design, architecture or interior design 🎨.",
            "nature": "Environmental science or agriculture could be great 🌿.",
            "technology": "Explore software development, AI, or cybersecurity 👨‍💻.",
            "people": "Think about careers in HR, psychology, or public relations 🗣️.",
        }
        for word, response in keywords.items():
            if word in user_message.lower():
                return response
        return "🤔 I'm not sure, but you can explore careers based on your subjects and interests on the left!"

# --- HANDLE CHAT ---
if clicked_intent:
    bot_reply = get_bot_reply(clicked_intent)
    st.session_state.chat.append(("You", clicked_intent))
    st.session_state.chat.append(("Bot", bot_reply))
elif user_input:
    bot_reply = get_bot_reply(user_input)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("Bot", bot_reply))

# --- DISPLAY CHAT HISTORY ---
for sender, message in st.session_state.chat:
    with st.chat_message(sender.lower()):
        st.write(message)

# --- AI-LIKE CAREER MATCH BASED ON USER PROFILE ---
st.subheader(" Career Suggestions Based on Your Preferences")
matched_careers = []

# By Subjects + Interests
if "Maths" in fav_subjects and "Technology" in interests:
    matched_careers.append("Data Analyst 📊")
if "Science" in fav_subjects and "Healthcare" in interests:
    matched_careers.append("Doctor 🩺")
if "Computer Studies" in fav_subjects:
    matched_careers.append("Software Engineer 💻")
if "Art" in fav_subjects and "Creative Thinking" in skills:
    matched_careers.append("Graphic Designer 🎨")
if "Life Sciences" in fav_subjects and "Environment & Nature" in interests:
    matched_careers.append("Environmental Scientist 🌿")

# Personality / Value-based suggestions
if personality == "Creative":
    matched_careers.append("Animator 🎬")
if personality == "Analytical":
    matched_careers.append("Data Scientist 📈")
if personality == "Empathetic":
    matched_careers.append("Psychologist 🧠")
if "Helping Others" in values:
    matched_careers.append("Social Worker 🤝")
if "High Salary" in values and "Maths" in fav_subjects:
    matched_careers.append("Actuary 💰")
if "Innovation" in values and "Technology" in interests:
    matched_careers.append("AI Engineer 🤖")

if matched_careers:
    for career in set(matched_careers):
        st.success(f"✅ Suggested: {career}")
else:
    st.info("Please select more preferences to see suggestions.")

# --- CHART: SKILL MATCH ---
if skills:
    st.subheader("📊 Skills Match Chart")
    fig, ax = plt.subplots()
    ax.bar(skills, [random.randint(60, 100) for _ in skills])
    ax.set_ylabel("Skill Match (%)")
    ax.set_title("Your Skill Compatibility")
    st.pyplot(fig)

# --- EMOJI REACTIONS ---
st.subheader("😃 How do you feel about these suggestions?")
emoji = st.radio("React with an emoji:", ["👍", "😊", "🤔", "🙁"])
st.write(f"Thanks for your reaction: {emoji}")
