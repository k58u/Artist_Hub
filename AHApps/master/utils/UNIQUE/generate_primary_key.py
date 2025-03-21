import uuid

def create_primary_key(postfix):
    """
    Generate a unique primary key or filename using UUID and a postfix.

    The generated primary key or filename will be in the format: <uuid>_<postfix>.

    Args:
        instance (models.Model): The model instance for which the primary key is being generated.
        postfix (str): A string to append to the unique UUID to form the primary key or filename.

    Returns:
        str: A unique primary key or filename combining a UUID and the provided postfix.

    Example:
        >>> create_primary_key(instance=None, postfix='image')
        'd9b2d63b8b9d4a64975dbedbd93f0f08_image'
    """
    # Generate a unique UUID
    unique_id = uuid.uuid4().hex
    # Create the primary key or filename by appending the postfix to the UUID
    primary_key = f"{unique_id}_{postfix}"
    return primary_key