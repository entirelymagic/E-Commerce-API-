import random
import string

generated_so_far: list = []


def random_string_generator(
        size: int = 10,
        chars: list = string.ascii_lowercase + string.digits,
        reset: bool = True
) -> string:
    """[Create a string that as long as the reset is 0 will not generate the same value]

    Args:
        size (int, mandatory): [string length]. Defaults to 10.
        chars ([type], optional): [containing char type]. Defaults to string.ascii_lowercase+string.digits.
        reset (int, optional): [reset the generated strings so far]. Defaults to 0.

    Returns:
        [str]: [a random string of size=size]
    """

    global generated_so_far
    if reset:
        # reset the list with generated elements
        generated_so_far.clear(),

    # generation of the new object
    new_generated_object = ''.join(random.choice(chars) for _ in range(size))

    # validate the generated object to make sure it is not a duplicate
    if new_generated_object not in generated_so_far:
        generated_so_far.append(new_generated_object)
        return new_generated_object
    else:
        # generate a new object and validate as the generated object was a duplicate
        random_string_generator(size, chars, reset)
