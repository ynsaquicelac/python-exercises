def getFactorial(n: int):
    """Calculate factorial of a given number

    Args:
        n (int): number integer to calculate factorial

    Returns:
        [type]: [description]
    """
    result = 1
    for c in range(n) :
        result = result * (c+1)
    return result