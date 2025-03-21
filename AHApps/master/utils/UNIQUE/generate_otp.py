import random
import time

def create_otp(length=6) -> str:
    """
    Generate a numeric OTP of specified length.
    
    Args:
        length (int): The length of the OTP. Default is 6 digits.
        
    Returns:
        str: A numeric OTP of the specified length.
    """
    otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
    return otp