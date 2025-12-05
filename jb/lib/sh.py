class shtools:
  def shexec(cmd):
    if cmd == "exit":
      while True:
        print("Press AC!")
    elif cmd == "test":
      print("Test works!")
    else:
      print("Invalid command.")
