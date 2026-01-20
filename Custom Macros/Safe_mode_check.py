try:
    is_safe = Settings.safe_mode_editor
except:
    is_safe = "<class 'function'>" in str(type(open))

if is_safe:
    log("SYSTEM: Safe Mode is ON")
else:
    log("SYSTEM: Safe Mode is OFF")
