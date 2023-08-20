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
settings = SettingsHelper()
advanced_profiles_helper = AdvancedProfileHelper()

minecraft_path = settings.get("minecraft_path")
advanced_profiles_helper.initialize_profile(minecraft_path, profile_id)

# Add custom arguments
custom_run_arguments = advanced_profiles_helper.get_profile_run_arguments(profile_id).split(" ")
arguments.extend(custom_run_arguments)

# Can't use os.getenv("JAVA_HOME")
java_path = settings.get("java_path")
print("Java path: " + java_path)

print("Starting Minecraft")
process = subprocess.run(["java", *arguments], executable=java_path)
print("Minecraft exited with code: " + str(process.returncode))

# Restore folders
advanced_profiles_helper.restore_default_profile(minecraft_path)
print("Restored old state of folders")
