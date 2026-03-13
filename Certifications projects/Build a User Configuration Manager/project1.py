# Add a new setting to the dictionary.
# Blocks duplicates — if the key already exists, returns an error message.
def add_setting(settings, key_value):
    key, value = key_value[0].lower(), key_value[1].lower()  # normalize to lowercase
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


# Update the value of an existing setting.
# If the key doesn't exist, returns an error message instead of creating it.
def update_setting(settings, key_value):
    key, value = key_value[0].lower(), key_value[1].lower()  # normalize to lowercase
    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


# Remove a setting from the dictionary by key.
# Returns an error message if the key is not found.
def delete_setting(settings, key):
    key = key.lower()  # normalize to lowercase
    if key not in settings:
        return "Setting not found!"
    del settings[key]
    return f"Setting '{key}' deleted successfully!"


# Display all current settings as a formatted string.
# Returns a fallback message if the dictionary is empty.
def view_settings(settings):
    if not settings:
        return "No settings available."
    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{key.capitalize()}: {value}")  # capitalize key for display only
    return "\n".join(lines) + "\n"  # trailing newline required by spec


# Test dictionary — sample user configuration for testing the functions above
test_settings = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}