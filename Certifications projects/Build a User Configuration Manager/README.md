# User Configuration Manager

A small Python module for managing user settings (theme, language, notifications, etc.) stored in a plain dictionary.

## Functions

### `add_setting(settings, key_value)`
Adds a new key-value pair to the settings dictionary.
- `key_value` is a tuple `(key, value)` — both are lowercased automatically.
- Returns an error message if the key already exists.

```python
add_setting(settings, ("theme", "dark"))
# → "Setting 'theme' added with value 'dark' successfully!"
```

---

### `update_setting(settings, key_value)`
Updates the value of an existing setting.
- Returns an error message if the key does not exist.

```python
update_setting(settings, ("theme", "light"))
# → "Setting 'theme' updated to 'light' successfully!"
```

---

### `delete_setting(settings, key)`
Removes a setting by key.
- Returns `"Setting not found!"` if the key does not exist.

```python
delete_setting(settings, "theme")
# → "Setting 'theme' deleted successfully!"
```

---

### `view_settings(settings)`
Returns a formatted string of all current settings.
- Returns `"No settings available."` if the dictionary is empty.

```python
view_settings({"theme": "dark", "language": "english"})
# → "Current User Settings:\nTheme: dark\nLanguage: english\n"
```

---

## `test_settings`

A sample dictionary included for testing:

```python
test_settings = {
    "theme": "dark",
    "language": "english",
    "notifications": "enabled"
}
```

## File Structure

```
user_config_manager.py   # All functions + test_settings
README.md                # This file
```