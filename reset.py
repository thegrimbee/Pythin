LEVEL_COUNT = 2

def reset(level):
    f = open(f"C:\\Users\\gabri\\Downloads\\ngrok-v3-stable-windows-amd64\\html\\solutions\\level{level}_submission_solution.py", "w")
    f.write("def clear_yard(pythin):\n\treturn")
    f.close()

def reset_all():
    for level in range(LEVEL_COUNT):
        reset(level)

x = input("Enter a level to reset: ")
if (x.lower()[0] == "a"):
    reset_all()
else:
    reset(int(x))