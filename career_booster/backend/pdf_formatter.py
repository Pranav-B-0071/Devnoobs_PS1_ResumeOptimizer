import os
from fpdf import FPDF

def save_resume_as_pdf(optimized_resume, filename="Optimized_Resume.pdf"):
    save_dir = "S:/career_booster/generated_resumes"  # Ensure correct path

    # ✅ Create the directory if it doesn’t exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    pdf_path = os.path.join(save_dir, filename)

    # ✅ Create PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # ✅ Add content to the PDF
    pdf.multi_cell(0, 10, optimized_resume)

    # ✅ Save PDF
    pdf.output(pdf_path)
    return pdf_path
