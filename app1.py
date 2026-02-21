st.markdown("""
    <style>
    /* Fond principal clair */
    .stApp {
        background: linear-gradient(135deg, #F0F7FF 0%, #FFFFFF 100%);
        color: #2C3E50;
    }
    
    /* --- CORRECTION SIDEBAR --- */
    [data-testid="stSidebar"] {
        background-color: #EBF5FB !important; /* Bleu ciel clair */
        border-right: 2px solid #D4AF37;
    }

    /* Force la couleur du texte dans le sidebar en bleu nuit */
    [data-testid="stSidebar"] .stMarkdown, 
    [data-testid="stSidebar"] p, 
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #001f3f !important;
        font-weight: 500;
    }

    /* Titres du sidebar en Or */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #B8860B !important;
    }
    /* -------------------------- */

    /* Cartes et contenus */
    .villa-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #D4AF37;
    }

    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #B8860B 100%);
        color: white !important;
        font-weight: bold;
        border: none;
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)
