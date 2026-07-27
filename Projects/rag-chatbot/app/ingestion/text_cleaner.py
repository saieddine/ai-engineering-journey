import re


def normalize_whitespace(text):
    """
    Replace tabs and carriage returns with normal spaces.
    """
    text = text.replace("\t", " ")
    text = text.replace("\r", " ")
    return text


def remove_extra_spaces(text):
    """
    Replace multiple spaces with a single space.
    """
    return re.sub(r" {2,}", " ", text)


def remove_blank_lines(text):
    """
    Replace multiple blank lines with a single blank line.
    """
    return re.sub(r"\n\s*\n+", "\n\n", text)


def strip_text(text):
    """
    Remove leading and trailing whitespace.
    """
    return text.strip()


def clean_text(text):
    """
    Apply all cleaning operations to a single text.
    """

    text = normalize_whitespace(text)
    text = remove_extra_spaces(text)
    text = remove_blank_lines(text)
    text = strip_text(text)

    return text


def clean_pages(pages):
    """
    Clean every page returned by the PDF reader.
    """

    cleaned_pages = []

    for page in pages:

        cleaned_page = {
            "page": page["page"],
            "text": clean_text(page["text"])
        }

        cleaned_pages.append(cleaned_page)

    return cleaned_pages