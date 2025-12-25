import streamlit as st

st.set_page_config(page_title="CodeSoft AI Chatbot", layout="centered")

st.title("🤖 CodeBot - CodeSoft Chatbot")
st.markdown("Hi! I'm your CodeSoft Assistant. Ask me anything about internships, projects, or certification!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "CodeBot", "content": "**CodeBot:** Welcome to CodeSoft! 👋\nHow can I help you today?\n\nYou can ask about:\n- Internship Opportunities\n- Project Guidelines\n- Application Process\n- Certificates\n- Support / Contact Us"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your question here...")

# Logic for chatbot response
def chatbot_reply(user_msg):

    msg = user_msg.lower()
    # Go Back to Main Menu
    if "main menu" in msg or msg.strip() == "menu":
        st.session_state.messages = [
            {"role": "CodeBot", "content": "**CodeBot:** Welcome to CodeSoft! 👋\nHow can I help you today?\n\nYou can ask about:\n- Internship Opportunities\n- Project Guidelines\n- Application Process\n- Certificates\n- Support / Contact Us"}
        ]
        return "**CodeBot:** You are back at the main menu. How can I help you today?\n\nYou can ask about:\n- Internship Opportunities\n- Project Guidelines\n- Application Process\n- Certificates\n- Support / Contact Us"

    if "internship" in msg or "Internship Opportunities" in msg or "opportunity" in msg:
        return (
            "**CodeBot:** **We offer internships in:**\n"
            "- 🌐Web Development\n"
            "- 📱App Development\n"
            "- 🐍Python Programming\n"
            "- ♨️Java Development\n"
            "- ☁️Cloud Computing\n"
            "- 🧠AI/ML\n\n"
            "Please type the name of the internship you're interested in to know more.\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )

    
    elif "web" in msg or "website" in msg:
        return (
            "**CodeBot:** **Here are the details for the Web Development Internship:**\n\n"
            "**Topics Covered:** HTML, CSS, Bootstrap, JavaScript, React\n\n"
            "Projects: Portfolio Website, E-commerce Site, Blog Platform, Weather App, To-Do List\n"
            "- **Duration:** 1 or 2 months\n"
            "- **Mode:** 100% Online\n"
            "- **Benefits:** Certificate + LOR + Recognition 🎓\n\n"
            "[Apply Here](https://www.codsoft.in/)\n\n"
            "Feel free to ask about specific projects or details!\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )
    elif ("app development" in msg) or ("mobile app" in msg) or (msg.strip() == "app"):
        return (
            "**CodeBot:** **Here are the details for the App Development Internship:**\n\n"
            "**Topics Covered:** Android, Flutter, React Native\n\n"
            "Projects: Quiz App, E-commerce App, Social Media App, Fitness Tracker, News Reader\n"
            "- **Duration:** 1 or 2 months\n"
            "- **Mode:** 100% Online\n"
            "- **Benefits:** Certificate + LOR + Recognition 🎓\n\n"
            "[Apply Here](https://www.codsoft.in/)\n\n"
            "Feel free to ask about specific projects or details!\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )
    elif "python" in msg or "django" in msg:
        return (
            "**CodeBot:** **Here are the details for the Python Programming Internship:**\n\n"
            "**Topics Covered:** Python Basics, Django, Flask, Data Analysis\n\n"
            "Projects: Web Scraper, Blog App, Data Visualization, REST API, Chatbot\n"
            "- **Duration:** 1 or 2 months\n"
            "- **Mode:** 100% Online\n"
            "- **Benefits:** Certificate + LOR + Recognition 🎓\n\n"
            "[Apply Here](https://www.codsoft.in/)\n\n"
            "Feel free to ask about specific projects or details!\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )
    elif "java" in msg or "spring" in msg:
        return (
            "**CodeBot:** **Here are the details for the Java Development Internship:**\n\n"
            "**Topics Covered:** Java Basics, Spring Framework, Hibernate\n\n"
            "Projects: Banking System, E-commerce App, Library Management, Online Quiz, Chat Application\n"
            "- **Duration:** 1 or 2 months\n"
            "- **Mode:** 100% Online\n"
            "- **Benefits:** Certificate + LOR + Recognition 🎓\n\n"
            "[Apply Here](https://www.codsoft.in/)\n\n"
            "Feel free to ask about specific projects or details!\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )
    elif "cloud" in msg or "aws" in msg or "azure" in msg:
        return (
            "**CodeBot:** **Here are the details for the Cloud Computing Internship:**\n\n"
            "**Topics Covered:** AWS, Azure, Google Cloud, DevOps\n\n"
            "Projects: Cloud Deployment, CI/CD Pipeline, Serverless Architecture, Containerization, Monitoring\n"
            "- **Duration:** 1 or 2 months\n"
            "- **Mode:** 100% Online\n"
            "- **Benefits:** Certificate + LOR + Recognition 🎓\n\n"
            "[Apply Here](https://www.codsoft.in/)\n\n"
            "Feel free to ask about specific projects or details!\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )
    elif "ai" in msg or "ml" in msg or "artificial" in msg:
        return (
            "**CodeBot:** **Here are the details for the AI/ML Internship:**\n"
            "- **Topics Covered:**\n"
            "- Projects: Chatbots, Face Detection, Image Captioning, Recommendation System, AI Games\n"
            "- Duration: 1 or 2 months\n"
            "- Mode: 100% Online\n"
            "- Benefits: Certificate + LOR + Recognition 🎓\n\n"
            "[Apply Here](https://www.codsoft.in/)\n\n"
            "Feel free to ask about specific projects or details!\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )

#) 🔙 Go Back to Main Menu

    
    elif "project" in msg:
        return (
            "**CodeBot:** **Project Guidelines:**\n"
            "- 5 Projects per internship\n"
            "- Topics provided\n"
            "- Sample datasets included\n"
            "- Submit via GitHub or file upload\n"
            "- Flexible deadlines\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )
    elif "certificate" in msg or "lor" in msg or "recommendation" in msg:
        return (
            "**CodeBot:** **Certification Info:**\n"
            "- You get a completion certificate after submitting projects.\n"
            "- Top performers also receive a Letter of Recommendation (LOR).\n"
            "- LinkedIn shoutouts for standout interns!\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )
    elif "application process" in msg or "apply" in msg or "application" in msg:
        return (
            "**CodeBot:** **Application Steps:**\n"
            "1. Go to [codsoft.in](https://www.codsoft.in)\n"
            "2. Select your internship\n"
            "3. Fill in your details\n"
            "4. Submit & wait for confirmation email 📧\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )
    elif "contact" in msg or "support" in msg:
        return (
            "**CodeBot:** **Contact Us:**\n"
            "- 📧 Email: support@codsoft.in\n"
            "- ☎️ Phone: +91-XXXXXXXXXX\n"
            "- 🌐 Website: [codsoft.in](https://www.codsoft.in)\n\n"
            "🔙 Type 'main menu' to go back to the Main Menu."
        )
    else:
        return (
            "**CodeBot:** Sorry, I didn't understand that. 🤔\n\n"
            "**CodeBot:** You can ask about:\n- Internship Opportunities\n- AI/ML Details\n- How to Apply\n- Certification\n- Support\n\nType 'main menu' to return to the main menu."
        )

# Process new user input
if user_input:
    # Store user message with prefix
    user_display = f"User: {user_input}"
    st.session_state.messages.append({"role": "user", "content": user_display})

    # Get bot response
    response = chatbot_reply(user_input)

    # Store bot response
    st.session_state.messages.append({"role": "bot", "content": response})

    # Display both messages
    with st.chat_message("user"):
        st.markdown(user_display)

    with st.chat_message("bot"):
        st.markdown(response)
