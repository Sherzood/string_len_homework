def main(s):
    """
    Given variable type string s. Return the character in the muddle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    lens=len(s)
    if lens%2==0:
        return s[lens//2-1:lens//2+1]
    else:
        return s[lens//2]    
    