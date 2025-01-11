import streamlit as st
from datetime import datetime

def generate_linkedin_post(event_name, event_date, event_description, event_link=None):
    """Generate a professional LinkedIn post"""
    post = f"""🎯 Excited to announce: {event_name}!

📅 Mark your calendars for {event_date}

{event_description}

{f'🔗 Learn more: {event_link}' if event_link else ''}

#ProfessionalDevelopment #Events #Networking"""
    return post

def generate_twitter_post(event_name, event_date, event_description, event_link=None):
    """Generate a concise Twitter post"""
    # Truncate description if too long
    max_desc_length = 150
    if len(event_description) > max_desc_length:
        event_description = event_description[:max_desc_length] + "..."
    
    post = f"""📢 Join us for {event_name}!
📅 {event_date}

{event_description}

{f'🔗 {event_link}' if event_link else ''}
"""
    return post

def generate_whatsapp_post(event_name, event_date, event_description, event_link=None):
    """Generate a WhatsApp-friendly post"""
    post = f"""📱 *{event_name}*

📅 *Date:* {event_date}

ℹ️ *Event Details:*
{event_description}

{f'🔗 *Registration Link:*\n{event_link}' if event_link else ''}

_Please share with interested colleagues!_"""
    return post

def main():
    st.set_page_config(page_title="Social Media Post Generator", layout="wide")
    
    # Header
    st.title("📱 Professional Social Media Post Generator")
    st.write("Generate professional posts for multiple social media platforms")
    
    # Input Section
    st.header("Event Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        event_name = st.text_input("Event Name", placeholder="e.g., Annual Tech Conference 2025")
        event_date = st.date_input("Event Date")
        event_link = st.text_input("Event Link (optional)", placeholder="https://yourevent.com")
    
    with col2:
        event_description = st.text_area(
            "Event Description",
            placeholder="Describe your event in detail...",
            height=150
        )
    
    # Generate posts when button is clicked
    if st.button("Generate Posts"):
        if not event_name or not event_description:
            st.error("Please fill in both event name and description.")
            return
        
        # Format date
        formatted_date = event_date.strftime("%B %d, %Y")
        
        # Create three columns for different platforms
        linkedin_col, twitter_col, whatsapp_col = st.columns(3)
        
        # LinkedIn Post
        with linkedin_col:
            st.subheader("LinkedIn Post")
            linkedin_post = generate_linkedin_post(
                event_name, formatted_date, event_description, event_link
            )
            st.text_area("", linkedin_post, height=300, key="linkedin")
            st.button("Copy LinkedIn Post", key="copy_linkedin",
                     on_click=lambda: st.write("Post copied to clipboard!"))
        
        # Twitter Post
        with twitter_col:
            st.subheader("Twitter Post")
            twitter_post = generate_twitter_post(
                event_name, formatted_date, event_description, event_link
            )
            st.text_area("", twitter_post, height=300, key="twitter")
            st.button("Copy Twitter Post", key="copy_twitter",
                     on_click=lambda: st.write("Post copied to clipboard!"))
        
        # WhatsApp Post
        with whatsapp_col:
            st.subheader("WhatsApp Post")
            whatsapp_post = generate_whatsapp_post(
                event_name, formatted_date, event_description, event_link
            )
            st.text_area("", whatsapp_post, height=300, key="whatsapp")
            st.button("Copy WhatsApp Post", key="copy_whatsapp",
                     on_click=lambda: st.write("Post copied to clipboard!"))
        
        # Tips section
        with st.expander("📝 Tips for Professional Social Media Posts"):
            st.markdown("""
            * **LinkedIn**: Focus on professional aspects and industry relevance
            * **Twitter**: Keep it concise and use relevant hashtags
            * **WhatsApp**: Maintain a clear structure and use formatting wisely
            * **General Tips**:
                * Proofread before posting
                * Use appropriate emojis sparingly
                * Include a clear call-to-action
                * Keep your audience in mind
            """)

if __name__ == "__main__":
    main()