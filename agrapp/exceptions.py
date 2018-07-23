"""
Agrapp exceptions classes
"""


class AgrappError(Exception):
    """
    Creating user which already exist.
    """

    def __init__(self, *args, **kwargs):
        super(AgrappError, self).__init__(*args, **kwargs)