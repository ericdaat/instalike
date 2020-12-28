import babel


def format_datetime(value, format="medium"):
    """Format a datetime as a prettier string.

    Args:
        value (datetime.datetime): the datetime value
        format (str, optional): full or medium. Defaults to "medium".

    Returns:
        [type]: [description]
    """
    if format == "full":
        format="EEEE, d. MMMM y 'at' HH:mm"
    elif format == "medium":
        format="EE dd.MM.y HH:mm"

    return babel.dates.format_datetime(value, format)
