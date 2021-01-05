from flask import Flask

app= Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World !"

if __name__ == "__main__":
    app.run()

    
   # intentionally Changing 
   # change 1
<<<<<<< HEAD:Tutorial1/app1.py
   # added from branch 
   # added in master
   # change in branch again

   # merge on branch 
=======
   # leave - Ille
>>>>>>> br1:Tutorial1/app.py
