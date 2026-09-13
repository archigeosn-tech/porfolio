import streamlit as st

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="CV - Fallou DIATTA | Hydraulicien & Géomaticien",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# 2. CUSTOM CSS STYLING (THEME: BLEU CIEL & DORÉ)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Poppins:wght@300;400;500;600&display=swap');

    :root {
        --bg-dark: #05111e;
        --card-bg: #0a1e36;
        --card-bg-hover: #102a4c;
        
        /* COULEURS PRINCIPALES : DORÉ & BLEU CIEL */
        --gold-primary: #d4af37;
        --gold-light: #f3e5ab;
        --gold-glow: rgba(212, 175, 55, 0.35);
        
        --sky-blue: #38bdf8;        /* Bleu ciel lumineux */
        --sky-blue-light: #bae6fd;  /* Bleu ciel doux */
        --sky-blue-glow: rgba(56, 189, 248, 0.25);
        
        --text-bright: #ffffff;
        --text-sub: #cbd5e1;
    }

    .stApp {
        background: linear-gradient(135deg, #030a14 0%, #061527 50%, #0a1e36 100%);
        color: var(--text-sub);
        font-family: 'Poppins', sans-serif;
    }

    [data-testid="stSidebar"] {
        background-color: #020710 !important;
        border-right: 2px solid var(--sky-blue);
    }

    h1, h2, h3, h4 {
        font-family: 'Montserrat', sans-serif !important;
    }

    .header-name {
        color: var(--gold-primary);
        font-size: 2.8rem;
        font-weight: 800;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 0px;
        text-shadow: 0 2px 12px var(--gold-glow);
    }

    .header-title {
        color: var(--sky-blue);
        font-size: 1.35rem;
        font-weight: 600;
        margin-top: -5px;
        margin-bottom: 20px;
        text-shadow: 0 0 10px var(--sky-blue-glow);
    }

    .summary-box {
        background: linear-gradient(135deg, rgba(10, 30, 54, 0.85) 0%, rgba(5, 17, 30, 0.95) 100%);
        border: 1px solid var(--gold-primary);
        border-left: 6px solid var(--sky-blue);
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 25px;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.5);
        line-height: 1.7;
        color: var(--text-bright);
        font-size: 1.05rem;
    }

    .card-item {
        background-color: var(--card-bg);
        border: 1px solid rgba(56, 189, 248, 0.25);
        border-radius: 12px;
        padding: 22px;
        margin-bottom: 18px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.4);
        transition: all 0.3s ease-in-out;
    }

    .card-item:hover {
        border-color: var(--gold-primary);
        transform: translateY(-3px);
        box-shadow: 0 10px 25px var(--gold-glow);
    }

    .card-title {
        color: var(--gold-primary);
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .card-subtitle {
        color: var(--sky-blue);
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 12px;
    }

    /* BADGES HARMONISÉS EN BLEU CIEL & DORÉ */
    .gold-badge {
        background: rgba(212, 175, 55, 0.15);
        color: var(--gold-light);
        border: 1px solid var(--gold-primary);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
        margin: 4px 3px;
    }

    .blue-badge {
        background: rgba(56, 189, 248, 0.15);
        color: var(--sky-blue-light);
        border: 1px solid var(--sky-blue);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        display: inline-block;
        margin: 4px 3px;
    }

    .metric-card {
        background: linear-gradient(145deg, #0a1e36, #05111e);
        border: 1px solid var(--sky-blue);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }

    .metric-number {
        color: var(--gold-primary);
        font-size: 1.8rem;
        font-weight: 800;
    }

    .metric-label {
        color: var(--sky-blue-light);
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .gold-divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, var(--sky-blue), var(--gold-primary), transparent);
        margin: 25px 0;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        background-color: rgba(10, 30, 54, 0.7);
        border-radius: 8px 8px 0 0;
        color: var(--text-sub);
        border: 1px solid rgba(56, 189, 248, 0.2);
        padding: 10px 20px;
        font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
        background-color: var(--card-bg) !important;
        color: var(--sky-blue) !important;
        border-bottom: 3px solid var(--gold-primary) !important;
        border-top: 1px solid var(--sky-blue) !important;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 3. SIDEBAR (PROFIL & CONTACT)
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# 3. SIDEBAR (PROFIL & CONTACT)
# -----------------------------------------------------------------------------
with st.sidebar:
    # Conteneur pour centrer la photo et le texte
    col_center1, col_center2, col_center3 = st.columns([1, 2, 1])
    with col_center2:
        # Affichage de ta photo de CV
        st.image("FD.png", use_container_width=True)

    st.markdown("""
        <div style="text-align: center;">
            <h2 style="color: #d4af37; margin-top: 10px; margin-bottom: 2px; font-size: 1.5rem;">Fallou DIATTA</h2>
            <p style="color: #38bdf8; font-size: 0.9rem; font-weight: 600;">Hydraulicien & Géomaticien</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

    st.subheader("📍 Coordonnées")
    st.markdown("""
    * 🏠 **Adresse :** Dakar, Sénégal
    * ✉️ **Email :** [archigeosn@gmail.com](mailto:archigeosn@gmail.com)
    * 📞 **Contact :** +221 77 238 99 68
    """)

    st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

    st.subheader("🌐 Langues & Logiciels")
    st.markdown("""
    * 🇫🇷 **Français :** Courant
    * 🇬🇧 **Anglais :** Technique
    * 💻 **Outils Clés :** QGIS, ArcMap, Streamlit, AutoCAD, SketchUp
    """)

# -----------------------------------------------------------------------------
# 4. MAIN CONTENT
# -----------------------------------------------------------------------------
st.markdown('<div class="header-name">Fallou DIATTA</div>', unsafe_allow_html=True)
st.markdown('<div class="header-title">Technicien Supérieur en Hydraulique & Géomaticien / Géomètre / Topographe</div>', unsafe_allow_html=True)

st.markdown("""
<div class="summary-box">
    <strong style="color:#38bdf8;">✨ Profil Professionnel :</strong><br>
    Géomètre-Topographe, Hydraulicien & Concepteur de Solutions Spatiales.<br>
    Passionné par l'aménagement du territoire et le bâtiment, j'allie la rigueur des levés de terrain à la puissance de la cartographie numérique et du WebGIS. De la modélisation de plans d'architecture résidentielle au dimensionnement des réseaux d'eau potable et à l'étude des sols, je transforme les données terrain en outils de décision fiables et durables.
</div>
""", unsafe_allow_html=True)

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">2+</div>
        <div class="metric-label">Stages Ingénierie</div>
    </div>
    """, unsafe_allow_html=True)
with col_m2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">10+</div>
        <div class="metric-label">Outils SIG & DAO</div>
    </div>
    """, unsafe_allow_html=True)
with col_m3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">100m</div>
        <div class="metric-label">Suivi Forage AEP</div>
    </div>
    """, unsafe_allow_html=True)
with col_m4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-number">3D</div>
        <div class="metric-label">WebGIS & Sols</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)

tab_exp, tab_comp, tab_edu = st.tabs([
    "🏗️ Expériences Professionnelles", 
    "🛠️ Compétences Techniques", 
    "📚 Formations & Diplômes"
])

# TAB 1: EXPÉRIENCES
with tab_exp:
    st.markdown("<h3 style='color:#38bdf8;'>Parcours en Entreprise</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-item">
        <div class="card-title">🛠️ STAGE EN INGÉNIERIE BTP, SIG & GÉOTECHNIQUE</div>
        <div class="card-subtitle">🏢 Technosol Ingénierie BTP | 📌 Dakar, Sénégal</div>
        <ul>
            <li><strong>SIG Web & Développement :</strong> Conception d'applications cartographiques sous Jupyter Notebook et Streamlit avec GeoPandas/Folium.</li>
            <li><strong>Modélisation 3D Stratigraphique :</strong> Visualisation et modélisation 3D des couches de sol à partir des données d'essais géotechniques.</li>
            <li><strong>Cartographie Fluviale :</strong> Analyse spatiale et cartographie du défluent de cours d'eau.</li>
            <li><strong>Essais Géotechniques :</strong> Essais de laboratoire pour l'identification des sols et caractérisation mécanique.</li>
            <li><strong>Rapports d'Ingénierie :</strong> Rédaction de synthèses techniques et rapports d'essais terrain.</li>
        </ul>
        <span class="gold-badge">Streamlit / Python</span>
        <span class="gold-badge">Stratigraphie 3D</span>
        <span class="blue-badge">Essais de Sol</span>
        <span class="blue-badge">Cartographie Fluviale</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card-item">
        <div class="card-title">🛠️ STAGE EN HYDRAULIQUE URBAINE & AGRICOLE</div>
        <div class="card-subtitle">🏢 SOLSO HYDROBAT | 📌 Thiès, Sénégal</div>
        <ul>
            <li><strong>Étude & Dimensionnement AEP :</strong> Calcul et dimensionnement des réseaux d'adduction d'eau potable.</li>
            <li><strong>Diagnostic du Réseau :</strong> Stratégies de réduction des fuites d’eau et optimisation de la distribution.</li>
            <li><strong>Ouvrages de Captage :</strong> Suivi technique complet de la réalisation d'un forage hydraulique de 100m.</li>
            <li><strong>Gestion de la Ressource :</strong> Évaluation des débits, diagnostics d'ouvrages et gestion des stocks en eau.</li>
        </ul>
        <span class="gold-badge">Dimensionnement AEP</span>
        <span class="gold-badge">Forage 100m</span>
        <span class="blue-badge">Diagnostic Réseau</span>
        <span class="blue-badge">Gestion Hydraulique</span>
    </div>
    """, unsafe_allow_html=True)

# TAB 2: COMPÉTENCES
with tab_comp:
    st.markdown("<h3 style='color:#38bdf8;'>Expertise Technique</h3>", unsafe_allow_html=True)
    col_c1, col_c2, col_c3 = st.columns(3)

    with col_c1:
        st.markdown("""
        <div class="card-item" style="height: 100%;">
            <h4 style="color:#38bdf8; margin-top:0;">🌐 Géomatique & WebGIS</h4>
            <ul>
                <li>QGIS & ArcMap (Traitement avancé)</li>
                <li>Python Spatiale (GeoPandas, Folium, Rasterio)</li>
                <li>Levés Topographiques (Station Totale, GNSS RTK, Niveau optique)</li>
                <li>Photogrammétrie Drone (Agisoft Metashape, CloudCompare)</li>
                <li>Collecte mobile (Mobile Topo)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_c2:
        st.markdown("""
        <div class="card-item" style="height: 100%;">
            <h4 style="color:#38bdf8; margin-top:0;">💧 Hydraulique & Géotechnique</h4>
            <ul>
                <li>Dimensionnement réseaux AEP & Surface libre</li>
                <li>Diagnostic d'ouvrages & Réduction de fuites</li>
                <li>Qualité de l'eau & Traitement physico-chimique</li>
                <li>Essais géotechniques & Caractérisation des sols</li>
                <li>Réalisation d'ouvrages de captage (Forages)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_c3:
        st.markdown("""
        <div class="card-item" style="height: 100%;">
            <h4 style="color:#38bdf8; margin-top:0;">🏗️ DAO, 3D & Structures</h4>
            <ul>
                <li>AutoCAD (Plans 2D)</li>
                <li>SketchUp (Modélisation 3D)</li>
                <li>Robot Structural Analysis (RSA)</li>
                <li>Métrés & Calculs de terrassement</li>
                <li>Visualisation d'extérieurs BTP</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# TAB 3: FORMATIONS
with tab_edu:
    st.markdown("<h3 style='color:#38bdf8;'>Diplômes & Titres Académiques</h3>", unsafe_allow_html=True)
    col_e1, col_e2 = st.columns(2)

    with col_e1:
        st.markdown("""
        <div class="card-item">
            <div class="card-title">Diplôme de Technicien Supérieur (DTS)</div>
            <div class="card-subtitle">🏛️ ISEP-Thiès | Spécialité Hydraulique</div>
            <p><strong>Option :</strong> Eau ,Infrastructure et Assainnissement Suivi Technique et Gestion des Ouvrages Hydrauliques</p>
        </div>
        """, unsafe_allow_html=True)

    with col_e2:
        st.markdown("""
        <div class="card-item">
            <div class="card-title">Brevet de Technicien Supérieur (BTS)</div>
            <div class="card-subtitle">🏛️ CEDT Le G15 - Dakar | Spécialité Géomatique</div>
            <p><strong>Option :</strong> Analyste spatiale, Aménagement du territoire & Topographie</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div class="gold-divider"></div>', unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #cbd5e1; font-size: 0.85rem; padding-bottom: 20px;">
    © Fallou DIATTA — Hydraulicien | Géomaticien | Géomètre | Topographe
</div>
""", unsafe_allow_html=True)
