from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GET','POST'])
def classify_image():
   util.load_saved_artifacts()
   image_data = request.form['image_data']
   print('image_data',image_data)
   response = jsonify(util.classify_image(image_data))
   print('response classification',response)
   response.headers.add('Access-Control-Allow-Origin', '*')
   return response

#if __name__ == "__main__":
#   print("Starting Python Flask Server For Tennis Celebrity Image Classification")
#   util.load_saved_artifacts()
#   app.run(port=5000)

