# =============================================================================
# Planet Class Lab
# freeCodeCamp Python Certification
# =============================================================================


# Define the Planet class — a blueprint for creating planet objects
class Planet:

    # -------------------------------------------------------------------------
    # __init__ is the constructor method. It runs automatically when you create
    # a new Planet instance, e.g. Planet("Earth", "Terrestrial", "Sun")
    # Parameters:
    #   self       → refers to the instance being created (always first)
    #   name       → the planet's name (e.g. "Earth")
    #   planet_type → the category of planet (e.g. "Terrestrial")
    #   star       → the star it orbits (e.g. "Sun")
    # -------------------------------------------------------------------------
    def __init__(self, name, planet_type, star):

        # --- Type Validation ---
        # isinstance(x, str) checks whether x is a string.
        # We check all three arguments at once using 'not ... or not ... or not ...'
        # If ANY of them is not a string, we raise a TypeError immediately.
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError("name, planet type, and star must be strings")

        # --- Value Validation ---
        # Even if the arguments are strings, they must not be empty ("").
        # An empty string is falsy in Python, so 'not name' is True when name == "".
        # If ANY of them is empty, we raise a ValueError immediately.
        if not name or not planet_type or not star:
            raise ValueError("name, planet_type, and star must be non-empty strings")

        # --- Assign Instance Attributes ---
        # If all validations pass, we store the values on the instance.
        # self.name means "this planet's name", accessible later as planet.name
        self.name = name
        self.planet_type = planet_type
        self.star = star

    # -------------------------------------------------------------------------
    # orbit() is a regular instance method.
    # It returns a formatted string describing the planet's orbit.
    # f-strings let us embed self.name and self.star directly inside the string.
    # -------------------------------------------------------------------------
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."

    # -------------------------------------------------------------------------
    # __str__ is a dunder (double-underscore) method that Python calls
    # automatically when you print() an object or convert it to a string.
    # Without this, print(planet) would show something like <Planet object at 0x...>
    # -------------------------------------------------------------------------
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"


# =============================================================================
# Create three Planet instances
# Each call to Planet(...) triggers __init__ with the given arguments.
# =============================================================================

planet_1 = Planet("Earth", "Terrestrial", "Sun")
planet_2 = Planet("Jupiter", "Gas Giant", "Sun")
planet_3 = Planet("Proxima Centauri b", "Terrestrial", "Proxima Centauri")


# =============================================================================
# Print each planet — this triggers __str__ on each object
# =============================================================================

print(planet_1)   # Planet: Earth | Type: Terrestrial | Star: Sun
print(planet_2)   # Planet: Jupiter | Type: Gas Giant | Star: Sun
print(planet_3)   # Planet: Proxima Centauri b | Type: Terrestrial | Star: Proxima Centauri


# =============================================================================
# Call orbit() on each planet and print the result
# =============================================================================

print(planet_1.orbit())   # Earth is orbiting around Sun...
print(planet_2.orbit())   # Jupiter is orbiting around Sun...
print(planet_3.orbit())   # Proxima Centauri b is orbiting around Proxima Centauri...