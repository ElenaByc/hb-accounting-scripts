"""Print out all the melons in our inventory."""


from melons import melons


def print_melon(melon_name, melon_attributes):
    """Print each melon with corresponding attribute information."""
    melon_name = melon_name.upper()
    print(melon_name)
    for attr, value in melon_attributes.items():
        print(f"{attr}: {value}")


for melon_name, melon_attributes in melons.items():
    print_melon(melon_name, melon_attributes)
    print()
