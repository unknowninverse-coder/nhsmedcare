import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="CareFinder ",
    page_icon="🏥",
    layout="centered",
    initial_sidebar_state="expanded"
)

# --- State Management ---
# This helps the app remember which "page" we are on.
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- Helper Functions to Change Page ---
def go_to_home():
    st.session_state.page = 'home'

def go_to_guidance():
    st.session_state.page = 'guidance'

def go_to_questionnaire():
    st.session_state.page = 'questionnaire'

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("CareFinder")
    st.button("Home", on_click=go_to_home, use_container_width=True, type="primary" if st.session_state.page == 'home' else "secondary")
    st.button("Guidance", on_click=go_to_guidance, use_container_width=True, type="primary" if st.session_state.page == 'guidance' else "secondary")
    st.button("Questionnaire", on_click=go_to_questionnaire, use_container_width=True, type="primary" if st.session_state.page == 'questionnaire' else "secondary")
    
    st.info("Created by Jayden Siluvaimani")


# --- Main Content ---

# --- Home Page ---
if st.session_state.page == 'home':
    st.title("Get the Right Care, Right Away")
    st.markdown("""
    A&E wait times are long.This is partly due to many people making trips to the A&E when this is not needed. To help combat this issue, this tool has been created to help you decide if you need to go to A&E, 
    book a GP appointment, or visit a local pharmacy, ensuring you get the appropriate 
    care and help reduce pressure on the NHS.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.button("Start Questionnaire", on_click=go_to_questionnaire, use_container_width=True, type="primary")
    with col2:
        st.button("Read Guidance", on_click=go_to_guidance, use_container_width=True)

# --- Guidance Page ---
elif st.session_state.page == 'guidance':
    st.title("Choosing the Right NHS Service")
    st.markdown("Understanding where to go for medical help can be confusing. Here’s a simple guide.")

    st.error("**When to go to A&E (or call 999)**")
    st.markdown("""
    A&E is for serious injuries and life-threatening emergencies only.
    - Loss of consciousness or signs of a stroke (FAST)
    - Severe chest pain or difficulty breathing
    - Heavy bleeding that won't stop
    - Severe burns, allergic reactions, or seizures
    """)

    st.info("**When to book a GP appointment**")
    st.markdown("""
    Your GP is your main point of contact for ongoing health issues and non-emergency illnesses.
    - Symptoms that are persistent, severe, or affecting your daily life
    - Mental health concerns like anxiety or depression
    - Managing long-term conditions like asthma or diabetes
    """)

    st.success("**When a Pharmacy is enough**")
    st.markdown("""
    Pharmacists are trained medical professionals who can provide advice and over-the-counter medicines for minor illnesses.
    - Coughs, colds, and sore throats
    - Minor rashes or skin conditions
    - Aches, pains, and upset stomachs
    - Questions about your medication
    """)
    
    st.warning("**If you're still unsure...**")
    st.markdown("If it's not a 999 emergency but you need medical help fast, you can contact **NHS 111** online or by phone. They are available 24/7.")


# --- Questionnaire Page ---
elif st.session_state.page == 'questionnaire':
    st.title("Symptom Questionnaire")
    st.markdown("Answer a few questions to get guidance on where to seek help. This is not a diagnosis.")

    with st.form("symptom_form"):
        st.subheader("1. Are you experiencing any emergency symptoms?")
        red_flag_chest_pain = st.checkbox("Severe chest pain or pressure")
        red_flag_breathing = st.checkbox("Severe difficulty breathing")
        red_flag_stroke = st.checkbox("Signs of a stroke (e.g., face drooping, arm weakness)")
        red_flag_bleeding = st.checkbox("Heavy bleeding that won't stop")
        red_flag_injury = st.checkbox("Severe head injury")
        red_flag_seizures = st.checkbox("Seizures or fits")

        st.subheader("2. How severe is your main symptom?")
        severity = st.radio(
            "Severity",
            ["Mild", "Moderate", "Severe"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        st.subheader("3. How long have you had this symptom?")
        duration = st.radio(
            "Duration",
            ["Less than a day", "A few days (1-3)", "More than 3 days"],
            horizontal=True,
            label_visibility="collapsed"
        )

        submitted = st.form_submit_button("Get Guidance", use_container_width=True, type="primary")

        if submitted:
            # --- DECISION LOGIC ---
            red_flags_present = any([
                red_flag_chest_pain, red_flag_breathing, red_flag_stroke, 
                red_flag_bleeding, red_flag_injury, red_flag_seizures
            ])

            # Rule 1: Any red-flag symptom immediately suggests A&E.
            if red_flags_present:
                st.error("### Go to A&E immediately.\nYour symptoms may indicate a medical emergency. If it is life-threatening, please call 999.")
            # Rule 2: Severe symptoms, or moderate symptoms for >3 days, suggest a GP.
            elif severity == 'Severe' or (severity == 'Moderate' and duration == 'More than 3 days'):
                st.info("### Book a GP appointment.\nYour symptoms are persistent or severe and should be checked by a doctor. Contact your GP surgery to make an appointment.")
            # Rule 3: Otherwise, a pharmacy is the first port of call.
            else:
                st.success("### Visit your local pharmacy.\nA pharmacist can offer clinical advice and over-the-counter medicines for a range of minor illnesses.")
            
            st.warning("If you’re unsure, you can call **NHS 111** for advice or visit **111.nhs.uk**.")

# --- Disclaimer (shows on all pages) ---
st.markdown("---")
st.markdown("""
<div style="text-align: center; font-size: 0.75rem; color: grey;">
This site provides general guidance only and is not a medical diagnosis. 
If symptoms are severe or life-threatening, call 999 or go to A&E. 
For non-emergency advice, contact NHS 111.
</div>

""", unsafe_allow_html=True)

