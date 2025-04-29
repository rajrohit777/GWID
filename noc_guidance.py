def get_noc_guidance(entity_type):
    if entity_type.lower() == "industry":
        return """
        ### NOC Guidelines for Industry
        1. Apply via CGWA portal
        2. Submit water requirement justification
        3. Include groundwater recharge plan
        4. Install piezometers and flow meters
        """
    elif entity_type.lower() == "agriculture":
        return """
        ### NOC for Agriculture
        - Usually exempt if traditional farming
        - Must avoid overexploited zones
        """
    else:
        return "Please specify either 'industry' or 'agriculture'."
