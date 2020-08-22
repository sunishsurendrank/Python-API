#Author of this Document : Sunish Surendran Kannembath
#Developer : Sunish Surendran Kannembath
#Reach Sunish in LinkedIn : https://www.linkedin.com/in/sunishsurendrank/
#Reach Sunish in Twitter : @sunishsurendran


from abc import ABC, abstractmethod
from flask import Flask, jsonify

app = Flask(__name__)

#Declaring Abstract Class
class Execute(ABC):

    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def ExecuteCode(self):
        pass

class ExecuteParallel(Execute):

    def __init__(self,count):
        self.count = count

   
    def ExecuteCode(self):
        return jsonify({"Result": "Executed Code Parallel"})


    #Magic method
    def __repr__(self):
        return f"{self.count}"

class ExecuteSerial(Execute):

    def __init__(self,count):
        self.count = count
    
   
    def ExecuteCode(self):
        return jsonify({"Result": "Executed Code Serial"})
    
    #Magic method
    def __repr__(self):
        return f"{self.count}"

@app.route('/serial')
def serial():
    ObjectExecuteSerial  = ExecuteSerial(4)
    ExecuteSerialResult = ObjectExecuteSerial.ExecuteCode()
    return ExecuteSerialResult


@app.route("/parallel")
def parallel():
    ObjectExecuteParallel =  ExecuteParallel(4)
    ExecuteParallelResult = ObjectExecuteParallel.ExecuteCode()
    return ExecuteParallelResult
    

if __name__ == "__main__":

    app.run(debug=True, port=5500)





