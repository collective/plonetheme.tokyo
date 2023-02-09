from plone import api


def crop(text, max_char_length):
    """
    Crop given text by full words to given count of chars.
    """

    if len(text) > max_char_length:
        cleared_text = text
        special_chars = [u'.', u',', u':', u';']
        for s in special_chars:
            cleared_text = cleared_text.replace(s, u' ')
        cropped_text = u' '.join((cleared_text[0:max_char_length].strip()).split(u' ')[:-1])  # noqa
        if len(cropped_text) == 0:
            cropped_text = cleared_text[0:max_char_length].strip()
        return cropped_text + u'...'
    return text
