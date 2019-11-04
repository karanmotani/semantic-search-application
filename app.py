from flask import Flask, request, render_template, jsonify
import subprocess
import sys
import json
import nlp_project

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/getData/', methods=['POST'])
# def getData():
# 	output = {}
#     # text = request.json['query']
# 	text = request.get_data()
# 	output['key'] = subprocess.check_output([sys.executable, "nlp_project.py", text])
#     # print(output)
# 	return jsonify(output)
#     # return json.dumps({'result': output});
#     # return render_template('index.html')


@app.route("/getInfo/", methods=['POST'])
def getInfo():
    query = request.args.get('query')
    print(query)
    # response = subprocess.check_output([sys.executable, "nlp_project.py", query])
    response = nlp_project.getResults(query)
    print(response)
    # answer, link = qna.getAnswer(query)
    d = {
        'query': query,
        'answer': response,
        # 'link': link
    }
    return jsonify(d)


if __name__ == '__main__':
    # app.debug = True
    app.run(debug=True) #app run