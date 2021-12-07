
def compute_tax(cost):
    """This function computes the tax
    of a purchase and returns it
    Args:
        cost - cost of purchase
    Returns:
        tax - the total tax"""
    return round(cost * 0.078, 2)

print(compute_tax(157.87876876))