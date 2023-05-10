import treepoem

def generate_qr_code_and_bar_code(seller_tax_id: str, suffix: str, ref1: str, ref2: str, amount: str) -> tuple:
    """Generate a QR code image.

    Args:
        seller_tax_id (str): The tax ID of the seller, 13 digits.
        suffix (str): A suffix for the tax ID, 2 digits.
        ref1 (str): A reference code.
        ref2 (str): Another reference code.
        amount (str): The payment amount in satang, not baht.

    Returns:
        tuple: A tuple containing the QR code image.
    """
    message = f"|{seller_tax_id}{suffix}\r{ref1}\r{ref2}\r{amount}"
    img_qrcode = treepoem.generate_barcode(barcode_type='qrcode', data=message)
    return img_qrcode
