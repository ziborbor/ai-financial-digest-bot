print("TRANSFORM MODULE LOADED")
def normalize_portfolio(rows):
    """
    Convert simplified Google Sheets portfolio into structured dataset.

    Expected input columns:
        Category | Holding | Quantity | USD Value | NZD Value

    Output:
        List of structured asset dictionaries
    """

    structured = []

    for r in rows:

        # ----------------------------
        # STEP 1: read columns clearly
        # ----------------------------
        category = r.get("Category")
        asset = r.get("Holding")
        qty = r.get("Quantity")
        usd = r.get("USD Value")
        nzd = r.get("NZD Value")

        # ----------------------------
        # STEP 2: skip empty rows
        # ----------------------------
        # These are blank separator rows in your sheet
        if not category or not asset:
            continue

        # ----------------------------
        # STEP 3: clean values safely
        # ----------------------------
        def clean_number(x):
            """
            Convert empty strings into None,
            otherwise ensure numeric type where possible.
            """
            if x == "" or x is None:
                return None
            return x

        qty = clean_number(qty)
        usd = clean_number(usd)
        nzd = clean_number(nzd)

        # ----------------------------
        # STEP 4: build structured record
        # ----------------------------
        structured.append({
            "category": category,
            "asset": asset,
            "quantity": qty,
            "usd": usd,
            "nzd": nzd
        })

    return structured