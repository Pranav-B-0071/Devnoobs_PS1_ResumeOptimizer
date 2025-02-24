from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap

def generate_pdf_resume(optimized_resume_text, output_filename="optimized_resume.pdf"):
    """
    Generates a properly formatted PDF from the optimized resume text.
    """
    try:
        pdf_canvas = canvas.Canvas(output_filename, pagesize=letter)
        width, height = letter

        pdf_canvas.setFont("Helvetica-Bold", 16)
        pdf_canvas.drawString(50, height - 50, "Optimized Resume")

        pdf_canvas.setFont("Helvetica", 12)
        y_position = height - 80  # Start below the title

        for line in textwrap.wrap(optimized_resume_text, width=100):
            pdf_canvas.drawString(50, y_position, line)
            y_position -= 20  # Move down for next line

            if y_position < 50:  # If page is full, create a new one
                pdf_canvas.showPage()
                pdf_canvas.setFont("Helvetica", 12)
                y_position = height - 50

        pdf_canvas.save()
        return output_filename

    except Exception as e:
        return f"Error generating PDF: {str(e)}"
