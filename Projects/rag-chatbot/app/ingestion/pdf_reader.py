import fitz


def read_pdf(pdf_path):
    """
    Reads a PDF file page by page.

    Args:
        pdf_path (str): Path to the PDF file.

    Returns:
        list: A list of dictionaries containing page numbers and extracted text.
    """

    document = fitz.open(pdf_path)

    pages = []

    for page_number in range(len(document)):
        page = document.load_page(page_number)

        text = page.get_text()

        pages.append(
            {
                "page": page_number + 1,
                "text": text
            }
        )

    document.close()

    return pages