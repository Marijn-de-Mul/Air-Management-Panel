from flask import Flask

app = Flask(__name__) 

import routers.login 
import routers.index    

if __name__ == '__main__': 
    app.run(debug = True)
    
