# Functions

def showAlert(title, message):
  print(f"\n=|{title}|=")
  print("==========================")
  print(message)
  print("==========================\n")

# Configuration
version = 1.01
safetyLock = False
# Loader
if safetyLock == True:
  print("Press EXE 3 times.")
  input()
  input()
  input()
print(f"MoonLoader {version}\n")
while True:
  i = input("> ")
  if i.lower() == "e" or i.lower() == "exit":
    break
  elif i.lower() == "hw":
    print("Hello, world!")
  elif i.lower() == "example":
    showAlert("Example", "This is a example alert.")
  else:
    print("Invalid command.")
