from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.utils import ImageReader

def generate_pdf(data, output_stream, logo_path='C:/Users/loubna/Desktop/app_finale/app_finale2/logo.jpg'):
    c = canvas.Canvas(output_stream, pagesize=letter)
    width, height = letter

    # Add logo to the PDF
    try:
        logo = ImageReader(logo_path)
        logo_width = 100
        logo_height = 50
        logo_x = (width - logo_width) / 2  # Center the logo horizontally
        logo_y = height - logo_height - 20  # Position logo 20 units below the top of the page
        c.drawImage(logo, logo_x, logo_y, width=logo_width, height=logo_height)
    except Exception as e:
        print(f"Error adding logo: {e}")


    # Add Company Information
    c.setFont("Helvetica-Bold", 12)
    c.drawString(72, height - 72, "Forges de Bazas")
    c.setFont("Helvetica", 10)
    c.drawString(72, height - 90, "Lotissement Polygone, 13-14 & 15 Route des Zenata, Casablanca 20250")
    c.drawString(72, height - 105, "Téléphone de l'entreprise : 05226-69850")
    
    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 150, "Attestation de Stage")

    # Define styles for Paragraphs
    styles = getSampleStyleSheet()
    styleN = styles['Normal']
    styleN.fontName = 'Helvetica'
    styleN.fontSize = 12
    styleN.leading = 14  # Line height
    styleN.spaceBefore = 10  # Space before paragraph
    styleN.spaceAfter = 20  # Space after paragraph

    # Body text with spacing
    text_lines = [
        f"Nous, soussignés, Forges de Bazas, certifions par la présente que {data.get('genre', '')} {data.get('nom', '')} {data.get('prenom', '')} a effectué un {data.get('type_stage', '')} au sein de notre entreprise du {data.get('date_debut', '')} jusqu'au {data.get('date_fin', '')}.",
        "",  # Empty line
        f"Durant cette période, {data.get('genre', '')} {data.get('nom', '')} {data.get('prenom', '')} a été affecté au {data.get('service', '')}. Son intitulé de stage était : {data.get('stage_intitule', '')}.",
        f"{data.get('genre', '')} {data.get('nom', '')} {data.get('prenom', '')} a fait preuve de plusieurs qualités professionnelles notamment rigueur, dynamisme et a su s’intégrer parfaitement à notre équipe.",
        "",
        "En foi de quoi, nous délivrons cette attestation pour servir et valoir ce que de droit.",
        "",
        f"Fait à Casablanca, le {data.get('date_attestation', '')}",
        "",
        f"Nom et Prénom du Responsable : {data.get('responsable_nom', '')}",
        f"Titre du Responsable : {data.get('responsable_titre', '')}",
        "Signature :"
    ]
    

    # Create a Frame to contain the paragraphs
    frame = Frame(72, 72, width - 144, height - 250, showBoundary=0)  # Adjusted margins

    # Convert text lines to Paragraphs
    paragraphs = [Paragraph(line, styleN) for line in text_lines]

    # Add Paragraphs to the Frame
    frame.addFromList(paragraphs, c)



    c.save()
