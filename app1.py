import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="ARCHIGEO | Devis en Temps Réel", page_icon="🏛️", layout="wide")

# --- PARAMÈTRE DE PRIX ---
PRIX_PAR_M2 = 1500  # 1500 FCFA / m²

# --- STYLE CSS (BLEU CIEL & GOLD ROYAL) — bloc unique fusionné ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #F0F7FF 0%, #FFFFFF 100%);
        color: #2C3E50;
    }

    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #1A5276 !important;
    }

    /* --- SIDEBAR --- */
    [data-testid="stSidebar"] {
        background-color: #EBF5FB !important;
        border-right: 2px solid #D4AF37;
    }
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #001f3f !important;
        font-weight: 500;
    }
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #B8860B !important;
    }

    /* --- CARTES VILLA --- */
    .villa-card {
        background: white;
        border: 1px solid #E0E0E0;
        border-top: 4px solid #D4AF37;
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

    /* --- BADGE PRIX --- */
    .price-tag {
        background-color: #FDF9E7;
        color: #B8860B;
        padding: 5px 12px;
        border-radius: 20px;
        font-weight: bold;
        font-size: 0.9em;
        border: 1px solid #D4AF37;
    }

    /* --- BOUTONS --- */
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37 0%, #B8860B 100%);
        color: white !important;
        font-weight: bold;
        width: 100%;
        border-radius: 8px;
        border: none;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)


# --- FONCTION D'ENVOI D'EMAIL ---
def envoyer_email(villa_nom, client_nom, client_email, client_tel="Non renseigné"):
    """Envoie un email de notification à ARCHIGEO lors d'une demande de plan."""
    try:
        cfg = st.secrets["email"]

        sujet = f"📐 Nouvelle demande de plan — {villa_nom}"
        corps_html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; color: #2C3E50;">
            <div style="max-width: 600px; margin: auto; border: 1px solid #D4AF37; border-radius: 10px; overflow: hidden;">
                <div style="background: linear-gradient(90deg, #1A5276, #2E86C1); padding: 20px; text-align: center;">
                    <h1 style="color: #D4AF37; margin: 0;">ARCHIGEO.SN</h1>
                    <p style="color: white; margin: 5px 0;">Nouvelle demande de plan technique</p>
                </div>
                <div style="padding: 30px;">
                    <h2 style="color: #1A5276;">Détails de la demande</h2>
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr style="background: #F4F9FF;">
                            <td style="padding: 10px; font-weight: bold; color: #B8860B;">Villa :</td>
                            <td style="padding: 10px;">{villa_nom}</td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; font-weight: bold; color: #B8860B;">Client :</td>
                            <td style="padding: 10px;">{client_nom}</td>
                        </tr>
                        <tr style="background: #F4F9FF;">
                            <td style="padding: 10px; font-weight: bold; color: #B8860B;">Email :</td>
                            <td style="padding: 10px;"><a href="mailto:{client_email}">{client_email}</a></td>
                        </tr>
                        <tr>
                            <td style="padding: 10px; font-weight: bold; color: #B8860B;">Téléphone :</td>
                            <td style="padding: 10px;">{client_tel}</td>
                        </tr>
                    </table>
                </div>
                <div style="background: #EBF5FB; padding: 15px; text-align: center; border-top: 1px solid #D4AF37;">
                    <p style="margin: 0; font-size: 0.85em; color: #1A5276;">ARCHIGEO | L'art de bâtir — Dakar, Sénégal</p>
                </div>
            </div>
        </body>
        </html>
        """

        msg = MIMEMultipart("alternative")
        msg["Subject"] = sujet
        msg["From"] = cfg["sender"]
        msg["To"] = cfg["receiver"]
        msg.attach(MIMEText(corps_html, "html"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(cfg["sender"], cfg["password"])
            server.send_message(msg)

        return True

    except Exception as e:
        st.error(f"Erreur lors de l'envoi de l'email : {e}")
        return False


# --- DONNÉES DES VILLAS ---
villas = [
    {"nom": "Villa Horizon",       "image": "ARCHIGEO3D.jpg",   "surface": 250, "style": "Moderne"},
    {"nom": "Résidence Emeraude",  "image": "ARCHIGEO3D 1.jpg", "surface": 180, "style": "Traditionnel"},
    {"nom": "Le Loft Urbain",      "image": "ARCHIGEO3D 2.jpg", "surface": 300, "style": "Moderne"},
    {"nom": "Villa Panoramique",   "image": "ARCHIGEO3D 3.jpg", "surface": 220, "style": "Moderne"},
]

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #D4AF37;'>ARCHIGEO.SN</h1>", unsafe_allow_html=True)
    st.image("logo_archigeo.jpg", width=180)  # renommé depuis google.jpg
    st.markdown("---")

    st.subheader("🔍 Voir les Projets")
    f_style = st.selectbox("Style d'architecture", ["Tous", "Moderne", "Traditionnel"])

    st.markdown("### 📞 Contactez Nous")
    st.info(f"**Tarif :** \n{PRIX_PAR_M2:,} FCFA / m²".replace(",", " "))
    st.write("👤 **Fallou**")
    st.write("📍 Dakar, Sénégal")
    st.write("📧 [archigeosn@gmail.com](mailto:archigeosn@gmail.com)")
    st.write("📞 +221 77 238 99 68")

# --- SECTION PRINCIPALE ---
st.markdown("<h1 style='color: #1A5276;'>Nos Conceptions 3D</h1>", unsafe_allow_html=True)
st.subheader("La vision spatiale 🌍 au service du design durable 🏗️🏠🏬.")

# Filtrage
filtered = [v for v in villas if (f_style == "Tous" or v["style"] == f_style)]

# Affichage des cartes
cols = st.columns(2)

for idx, v in enumerate(filtered):
    prix_total = v["surface"] * PRIX_PAR_M2

    with cols[idx % 2]:
        st.markdown('<div class="villa-card">', unsafe_allow_html=True)
        st.subheader(v["nom"])

        try:
            st.image(v["image"], use_container_width=True)
        except Exception:
            st.warning(f"Image {v['image']} en attente de téléchargement...")

        c1, c2 = st.columns([1, 1.2])
        c1.markdown(f"📏 **Surface :** {v['surface']} m²")
        c2.markdown(
            f'<span class="price-tag">💰 {prix_total:,} FCFA</span>'.replace(",", " "),
            unsafe_allow_html=True,
        )

        # --- FORMULAIRE DE DEMANDE ---
        with st.form(key=f"form_{idx}"):
            st.markdown("#### Demander le plan technique")
            client_nom   = st.text_input("Votre nom complet",  key=f"nom_{idx}")
            client_email = st.text_input("Votre email",        key=f"email_{idx}")
            client_tel   = st.text_input("Votre téléphone (optionnel)", key=f"tel_{idx}")
            submitted    = st.form_submit_button("📩 Envoyer la demande")

            if submitted:
                if not client_nom or not client_email:
                    st.warning("Merci de renseigner votre nom et votre email.")
                else:
                    with st.spinner("Envoi de votre demande en cours..."):
                        succes = envoyer_email(v["nom"], client_nom, client_email, client_tel)
                    if succes:
                        st.success(f"✅ Demande pour **{v['nom']}** envoyée ! Nous vous recontacterons sous 24h.")
                        st.balloons()

        st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown(
    "<br><p style='text-align: center; opacity: 0.7;'>ARCHIGEO | L'art de bâtir</p>",
    unsafe_allow_html=True,
)
