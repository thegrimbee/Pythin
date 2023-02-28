from flask import render_template, redirect, url_for, request, Flask
from random import shuffle, randint
import json
import os

f = open('C:/Users/gabri/Downloads/ngrok-v3-stable-windows-amd64/html/data.json')
data = json.loads(f.read())
f.close()
app = Flask(__name__, static_url_path='/static')

def smoothen(f):
     lf = list(f)
     count = lf.count('\n')
     for i in range(count):
          lf.remove('\n')
     return "".join(lf)
def level_generate(level, rand):
     if not rand:
          return data["examples"][level]
     length = 20
     if level == 0:
          return randint(3, length+1)*['rat']
     elif level == 1:
          items = ['rat', 'tiger']
          level_items = []
          num_of_items = randint(3, length)
          for i in range(num_of_items):
               level_items.append(items[randint(0,1)])
          return level_items
     
@app.route('/')
def root():
	return redirect('/level0')

@app.route('/level<int:level_number>', methods = ['GET', 'POST'])
def game(level_number):
     if request.method == "GET":
          items = level_generate(level_number, False)
          level_description = data["levelDescription"][level_number]
          examples = data["examples"][level_number]
          images = []
          f = open(f"C:\\Users\\gabri\\Downloads\\ngrok-v3-stable-windows-amd64\\html\\solutions\\level{level_number}_submission_solution.py")
          starting_code = f.read()
          f.close()
          for example in examples:
               images.append(data["images"][example])
          return render_template('game.html',
                                   items=items,
                                   level_number=level_number,
                                   level_description=level_description,
                                   images=images,
                                   examples=examples,
                                   code=starting_code
                                   )
     else:
          items = level_generate(level_number, True)
          images = []
          for item in items:
               images.append(data["images"][item])
          smoothened_code = smoothen(request.form["code"])
          f = open(f"C:\\Users\\gabri\\Downloads\\ngrok-v3-stable-windows-amd64\\html\\solutions\\level{level_number}_submission_solution.py", "w")
          f.write(smoothened_code)
          f.close()
          from solutions.solve import solve
          moves, submission_count, real_count, status = solve(items, level_number)
          if status == "success":
               if submission_count <= real_count:
                    status = "win"
               else:
                    status = "suboptimal"
          print(items, moves)
          return render_template("gamepreview.html",
                                   level_number=level_number,
                                   moves=moves,
                                   images=images,
                                   status=status
                                   )

    
app.run(debug=True)