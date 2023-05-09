import functools

def rgetattr(obj: object, attr: str, default: object = None) -> object:
    """A recursive implementation of `getattr()` that can retrieve nested attributes of an object.

    Args:
        obj (object): The object to get the attribute from.
        attr (str): The attribute to get. Can be a nested attribute, separated by dots.
        default (object, optional): The value to return if the attribute is not found. Defaults to None.

    Returns:
        object: The value of the attribute.
    """
    # Define a helper function to get the value of a single attribute
    def _getattr(obj, attr):
        return getattr(obj, attr, default)

    # Split the attribute string into a list of attribute names
    attrs = attr.split('.')

    # Use functools.reduce() to apply the _getattr() function to each attribute in turn
    # The initial value is the object we want to get the attribute from
    # For example, if attr is "a.b.c", then reduce(_getattr, [obj, "a", "b", "c"]) will be equivalent to
    # _getattr(_getattr(_getattr(obj, "a"), "b"), "c")
    return functools.reduce(_getattr, [obj] + attrs)


def rgetdict(obj: dict, attr: str, default: object = None) -> object:
    """A recursive implementation of getting values from a nested dictionary.

    Args:
        obj (dict): The dictionary to get the value from.
        attr (str): The key to get. Can be a nested key, separated by dots.
        default (object, optional): The value to return if the key is not found. Defaults to None.

    Returns:
        object: The value of the key.
    """
    # Define a helper function to get the value of a single key
    def _getdict(obj, key):
        if obj == default:
            return default

        return obj.get(key, default)

    # Split the key string into a list of key names
    keys = attr.split('.')

    # Use functools.reduce() to apply the _getdict() function to each key in turn
    # The initial value is the dictionary we want to get the value from
    # For example, if attr is "a.b.c", then reduce(_getdict, [obj, "a", "b", "c"]) will be equivalent to
    # _getdict(_getdict(_getdict(obj, "a"), "b"), "c")
    return functools.reduce(_getdict, [obj] + keys)


class A:
    def __init__(self):
        self.b = B()


class B:
    def __init__(self):
        self.c = "Hello, world! rgetattr"

# Example usage of rgetattr()
a = A()
name_of_attr = 'c'
value = rgetattr(a, f'b.{name_of_attr}')
print(value)  # Output: "Hello, world!"


# Example usage of rgetdict()
a = {
    "b": {
        "c": "Hello, world! rgetdict"
    }
}
name_of_attr = "c"
value = rgetdict(a, f"b.{name_of_attr}")
print(value)  # Output: "Hello, world!"
