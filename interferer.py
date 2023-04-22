import os, sys, subprocess
from utils.settings_helper import Settings

arguments = sys.argv[1:]

profile_id_index = arguments.index("--multiprofile")
arguments.pop(profile_id_index)
profile_id = arguments.pop(profile_id_index)
print("Profile ID: " + profile_id)
# TODO: Modify folders

# Can't use os.getenv("JAVA_HOME")
settings = Settings()
java_path = settings.get("java_path")
print("Java path: " + java_path)

print("Starting Minecraft")
process = subprocess.run(["java", *arguments], executable=java_path)
print("Minecraft exited with code: " + str(process.returncode))

# TODO: Restore folders
print("Restored old state of folders")
