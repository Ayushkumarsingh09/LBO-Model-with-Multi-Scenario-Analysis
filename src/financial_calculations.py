def calculate_enterprise_value(ebitda, multiple):
    """
    Calculate the enterprise value based on EBITDA and a multiple.
    """
    return ebitda * multiple


def calculate_equity_value(enterprise_value, net_debt):
    """
    Calculate the equity value by subtracting net debt from enterprise value.
    """
    return enterprise_value - net_debt
