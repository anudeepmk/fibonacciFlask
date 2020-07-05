from flask import Flask,jsonify,abort
from itertools import combinations_with_replacement

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.errorhandler(404) 
def invalid_route(e): 
    return jsonify({'errorCode' : 404, 'message' : 'Invalid value entered'})


@app.route("/fib/<int:num>")
def fibCalculate(num):
    if num < 0:
        print("enter proper input")

    fiblist = []
    newfiblist = []

    f1, f2 = 1, 1

    if num > 0:
        fiblist.append(f1)

    for i in range(1,num):
        fiblist.append(f2)
        f3 = f1 + f2
        f1, f2 = f2, f3

    for i in fiblist[2:]:
        if i < num:
            newfiblist.append(i)



    return jsonify([x for l in range(1, len(newfiblist)) for x in combinations_with_replacement(newfiblist, l + 2) if sum(x) == num]),200



@app.route("/health")
def healthCheck():
    return jsonify("service is UP"),200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') 