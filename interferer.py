import sys, subprocess
from utils.advanced_profiles_helper import AdvancedProfileHelper
from utils.settings_helper import SettingsHelper

# Get Profile ID
arguments = sys.argv[1:]
profile_id_index = arguments.index("--multiprofile")
arguments.pop(profile_id_index)
profile_id = arguments.pop(profile_id_index)
print("Profile ID: " + profile_id)

# Init profile
advanced_profiles_helper = AdvancedProfileHelper()
advanced_profiles_helper.initialize_profile(profile_id)

# Add direct play to arguments
quickplay_server = advanced_profiles_helper.get_profile_server(profile_id)
if quickplay_server is not None:
    arguments.append("--quickPlayMultiplayer")
    arguments.append(f'"{quickplay_server}"')

# Can't use os.getenv("JAVA_HOME")
settings = SettingsHelper()
java_path = settings.get("java_path")
print("Java path: " + java_path)

print("Starting Minecraft")
process = subprocess.run(["java", *arguments], executable=java_path)
print("Minecraft exited with code: " + str(process.returncode))

# Restore folders
advanced_profiles_helper.restore_default_profile()
print("Restored old state of folders")
