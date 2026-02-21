import streamlit as st

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="ARCHIGEO | Devis en Temps Réel", page_icon="🏛️", layout="wide")

# --- PARAMÈTRE DE PRIX ---
PRIX_PAR_M2 = 1500  # 1500 FCFA / m²

# --- STYLE CSS (BLEU CIEL & GOLD ROYAL) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #F4F9FF 0%, #FFFFFF 100%);
        color: #2C3E50;
    }
    
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #1A5276 !important;
    }

    .villa-card {
        background: white;
        border: 1px solid #E0E0E0;
        border-top: 4px solid #D4AF37; /* Ligne d'accent or en haut */
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.05);
        transition: transform 0.3s ease;
    }
    
    .villa-card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 15px 30px rgba(212, 175, 55, 0.15);
    }

    .price-tag {
        background-color: #FDF9E7;
        color: #B8860B;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.9em;
        border: 1px solid #D4AF37;
    }

    [data-testid="stSidebar"] {
        background-color: #EBF5FB !important;
        border-right: 1px solid #D4AF37;
    }

    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #B8860B 100%);
        color: white !important;
        width: 100%;
        border-radius: 8px;
        border: none;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
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

# --- DONNÉES DES VILLAS (Surfaces modifiées pour le calcul) ---
villas = [
    {"nom": "Villa Horizon", "image": "ARCHIGEO3D.jpg", "surface": 250, "style": "Moderne"},
    {"nom": "Résidence Emeraude", "image": "ARCHIGEO3D 1.jpg", "surface": 180, "style": "Traditionnel"},
    {"nom": "Le Loft Urbain", "image": "ARCHIGEO3D 2.jpg", "surface": 300, "style": "Moderne"},
    {"nom": "Villa Panoramique", "image": "ARCHIGEO3D 3.jpg", "surface": 220, "style": "Moderne"}
]

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>ARCHIGEO.SN</h1>", unsafe_allow_html=True)
    st.image("google.jpg", width=180)
    st.markdown("---")
    
    st.subheader("🔍Voir les Projets")
    f_style = st.selectbox("Style d'architecture", ["Tous", "Moderne", "Traditionnel"])
    
    st.markdown("### 📞 Contactez moi")
    st.info(f"**Tarif Standard :** \n{PRIX_PAR_M2:,} FCFA / m²".replace(',', ' '))
    st.write("👤 **Fallou DIATTA**")
    st.write("📍 Dakar, Sénégal")
    st.write("📧 [archigeosn@gmail.com](mailto:archigeosn@gmail.com)")
    st.write("📞 +221 77 238 99 68")

# --- SECTION PRINCIPALE ---
st.markdown("<h1 style='color: #1A5276;'>Nos Conceptions 3D</h1>", unsafe_allow_html=True)
st.subheader("La vision spatiale🌍 au service du design durable🏗️🏠🏬.")

# Filtrage
filtered = [v for v in villas if (f_style == "Tous" or v["style"] == f_style)]

# Affichage des cartes
cols = st.columns(2)
for idx, v in enumerate(filtered):
    # Calcul dynamique du prix
    prix_total = v['surface'] * PRIX_PAR_M2
    
    with cols[idx % 2]:
        st.markdown(f'<div class="villa-card">', unsafe_allow_html=True)
        st.subheader(v["nom"])
        
        try:
            st.image(v["image"], use_container_width=True)
        except:
            st.warning(f"Image {v['image']} en attente de téléchargement...")
            
        c1, c2 = st.columns([1, 1.2])
        c1.markdown(f"📏 **Surface :** {v['surface']} m²")
        
        # Affichage du prix calculé
        c2.markdown(f'<span class="price-tag">💰 {prix_total:,} FCFA</span>'.replace(',', ' '), unsafe_allow_html=True)
        
        st.write("") # Espacement
        if st.button(f"Demander le plan technique", key=f"btn_{idx}"):
            st.success(f"Demande pour la {v['nom']} reçue ! Nous vous recontacterons.")
            st.balloons()
            
        st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<br><p style='text-align: center; opacity: 0.7;'>ARCHIGEO | L'art de bâtir</p>", unsafe_allow_html=True)
