def generate_report(area_name):
    report = f"""
    ### Groundwater Report for {area_name}

    - **Ground Water Resource Assessment**: Moderate extraction with recharge from rainfall and surface flow.
    - **Categorization**: Semi-critical based on declining trends.
    - **Management Practices**:
        - Artificial recharge structures
        - Drip irrigation for agriculture
    - **NOC Conditions**:
        - Mandatory digital water meter
        - Submission of annual abstraction reports
    - **How to Obtain NOC**:
        1. Register on CGWA portal
        2. Submit hydrogeological report
        3. Upload land ownership documents
        4. Get environmental clearance
    """
    return report
