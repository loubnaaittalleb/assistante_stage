import streamlit as st
from app import main as app
from form_recup import main as form_recup
from form_reparation import main as form_reparation
from form_ordre import main as form_ordre
from form_stage import main as form_stage
from streamlit_app import email_generator

# Configuration de la page
st.set_page_config(page_title="Page Principale", page_icon=":sparkles:", layout="wide")

# Style CSS amélioré pour une mise en page sophistiquée
st.markdown("""
    <style>
        .footer {
            background-color: #003d7a;
            color: white;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            width: 100%;
            bottom: 0;
            box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.2);
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .footer p {
            margin: 0;
            font-size: 16px;
        }

        .footer-links {
            margin-top: 10px;
            display: flex;
            gap: 15px;
            font-size: 14px;
        }

        .footer-links a {
            color: white;
            text-decoration: none;
        }

        .footer-links a:hover {
            text-decoration: underline;
        }

        .circle-border {
            background-color: #FFA500;
            color: #003d7a;
            padding: 70px;
            border-radius: 50%;
            text-align: center;
            max-width: 400px;
            margin: 50px auto;
            border: 4px solid #003d7a; /* Couleur de la bordure */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .section-title {
            font-size: 28px;
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 20px;
            color: #003d7a;
            text-align: center;
        }

        .contact-section {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            align-items: center;
            text-align: center;
            margin: auto;
            background-color: #ffffff;
        }

        .contact-info, .social-media {
            flex: 1;
            padding: 20px;
            box-sizing: border-box;
        }

        .contact-info h3, .social-media h3 {
            font-size: 22px;
            color: #003d7a;
        }

        .contact-info p {
            font-size: 16px;
            margin: 10px 0;
        }

        .social-media {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .social-icons {
            display: flex;
            gap: 20px;
            justify-content: center;
        }

        .social-icons img {
            width: 24px; /* Ajustez la taille des icônes */
            height: 24px;
        }

        .about-section {
            background-color: #ffffff;
            color: #003d7a;
            padding: 20px;
            border-radius: 8px;
            margin-top: 20px;
            text-align: center;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        .about-section h2 {
            font-size: 32px;
            margin-bottom: 20px;
        }

        .about-section p {
            font-size: 18px;
            line-height: 1.6;
        }

        .highlight {
            background-color: #f0f8ff;
            border-left: 4px solid #003d7a;
            padding: 10px;
            margin-top: 20px;
        }

        body {
            background-color: #f9f9f9; /* Couleur de fond */
            color: #003d7a;
            font-family: 'Arial', sans-serif;
        }

        .nav-wrapper {
            position: fixed;
            top: 0;
            width: 100%;
            background-color: #FFA500; /* Couleur orange de la barre de navigation */
            z-index: 1000;
            border-bottom: 2px solid #ddd;
        }

        .nav-bar {
            display: flex;
            justify-content: center; /* Centrer les boutons horizontalement */
            align-items: center;
            position: relative;
        }

        .nav-button {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-decoration: none;
            cursor: pointer;
            padding: 10px 20px;
            border-radius: 5px;
            background-color: #003d7a; 
            transition: background-color 0.3s, transform 0.3s;
            margin: 0; 
            border: none; 
        }

        .nav-button:hover {
            background-color: #FFA500; 
            transform: scale(1.05);
        }

        .nav-button:active {
            background-color: #003d7a; 
            transform: scale(0.95);
        }

        .page-container {
            width: 100%; 
            margin-top: 70px; 
            box-sizing: border-box;
        }
    </style>
""", unsafe_allow_html=True)

# Pied de page
st.markdown("""
    <div class="footer">
        <div class="footer-content">
            <p>© 2024 Votre Assistante Virtuelle. Tous droits réservés.</p>
            <div class="footer-links">
                <a href="#">Politique de confidentialité</a> |
                <a href="#">Conditions d'utilisation</a> |
                <a href="#">Mentions légales</a>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Barre de navigation avec fond orange fixe
st.markdown('<div class="nav-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="nav-bar">', unsafe_allow_html=True)

# Variables de session pour la navigation
if 'section' not in st.session_state:
    st.session_state['section'] = 'documents'

# Navigation horizontale
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)
with nav_col1:
    if st.button('Documents', key='docs', help="Accédez aux documents"):
        st.session_state['section'] = 'documents'
with nav_col2:
    if st.button('Générateur d\'emails', key='email-gen', help="Créez des emails"):
        st.session_state['section'] = 'email-generator'
with nav_col3:
    if st.button('Contactez-nous', key='contact', help="Nous contacter"):
        st.session_state['section'] = 'contactez-nous'
with nav_col4:
    if st.button('Qui nous sommes', key='about', help="En savoir plus sur nous"):
        st.session_state['section'] = 'qui-nous-sommes'

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Contenu de la page
st.markdown('<div class="page-container">', unsafe_allow_html=True)  # Add margin-top to avoid content overlapping with navbar

# Message de bienvenue simplifié
st.markdown('<div class="section-title">Bienvenue sur notre plateforme d\'assistance administrative virtuelle</div>', unsafe_allow_html=True)

# Vérifier l'état de la section actuelle
section = st.session_state['section']

# Section Documents
if section == "documents":
    st.markdown('<div class="section-title">Documents</div>', unsafe_allow_html=True)
    doc_page = st.selectbox("Choisissez un formulaire", [
        "Formulaire du départ en Congé", 
        "Formulaire Récupération pièces sur matériel", 
        "Formulaire de passer matériel sous Réparation",
        "Ordre de Mission",
        "Attestation de Stage"
    ])
    if doc_page == "Formulaire du départ en Congé":
        form_recup()
    elif doc_page == "Formulaire Récupération pièces sur matériel":
        form_reparation()
    elif doc_page == "Formulaire de passer matériel sous Réparation":
        form_ordre()
    elif doc_page == "Ordre de Mission":
        form_stage()
    elif doc_page == "Attestation de Stage":
        app()

# Section Générateur d'emails
elif section == "email-generator":
    st.markdown('<div class="section-title">Générateur d\'emails</div>', unsafe_allow_html=True)
    email_generator()

# Section Contactez-nous
elif section == "contactez-nous":
    st.markdown('<div class="section-title">Contactez-nous</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="contact-section">
            <div class="contact-info">
                <h3>Informations de Contact</h3>
                <div class="contact-details">
                    <p><strong>Email :</strong> contact@forgesdebazas.com</p>
                    <p><strong>Téléphone :</strong> 05 22 66 98 59</p>
                    <p><strong>Adresse :</strong>Route Zenata 111 KM 11,5 Aïn Sebaâ, Casablanca</p>
                </div>
            </div>
            <div class="social-media">
                <h3>Suivez-nous</h3>
                <div class="social-icons">
                    <a href="https://facebook.com" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook">
                    </a>
                    <a href="https://whatsapp.com" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp">
                    </a>
                    <a href="https://instagram.com" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
                    </a>
                </div>
            </div>
        </div>
        <style>
            .contact-section {
                display: flex;
                justify-content: space-between;
                align-items: flex-start;
                background-color: #f9f9f9;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 1000px;
                margin: 0 auto;
            }
            .contact-info {
                flex: 1;
                padding: 10px;
            }
            .contact-info h3 {
                font-size: 24px;
                color: #003d7a;
                margin-bottom: 10px;
            }
            .contact-details {
                display: flex;
                flex-direction: column;
                gap: 10px;
                margin: 0;
            }
            .contact-details p {
                font-size: 18px;
                margin: 0; /* Remove default margin to ensure alignment */
                color: #555;
            }
            .social-media {
                flex: 1;
                display: flex;
                flex-direction: column;
                align-items: center;
                padding: 10px;
            }
            .social-media h3 {
                font-size: 24px;
                color: #003d7a;
                margin-bottom: 20px;
            }
            .social-icons {
                display: flex;
                gap: 20px;
            }
            .social-icons img {
                width: 40px;
                height: 40px;
                transition: transform 0.3s ease;
            }
            .social-icons img:hover {
                transform: scale(1.1);
            }
        </style>
    """, unsafe_allow_html=True)

# Section Qui nous sommes
elif section == "qui-nous-sommes":
    st.markdown('<div class="about-section">', unsafe_allow_html=True)
    st.markdown("""
        <h2>À propos de nous</h2>
        <p>Nous sommes une équipe dévouée à fournir les meilleurs services d'assistance administrative. Notre plateforme offre des solutions rapides et efficaces pour vos besoins quotidiens.</p>
    """, unsafe_allow_html=True)
    st.markdown("""
        <div class="highlight">
            <p>Notre mission est de simplifier vos tâches administratives en vous offrant des outils puissants et faciles à utiliser. Nous croyons que la technologie doit être au service de l'humain, et non l'inverse.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # End about section

st.markdown('</div>', unsafe_allow_html=True)  # Close page container
