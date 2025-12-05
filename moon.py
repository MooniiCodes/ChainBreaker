from jb.lib.sh import shtools

# Functions
def showAlert(title, message):
  print("\n=|" + title + "|==============================")
  print("==========================")
  print(message)
  print("==========================\n")

# Configuration
version = "1.01"
safetyLock = False
# Loader
if safetyLock == True:
  print("Press EXE 3 times.")
  input()
  input()
  input()
print("MoonLoader" + version + "\n")
while True:
  i = input("> ")
  shtools.shexec(i)
