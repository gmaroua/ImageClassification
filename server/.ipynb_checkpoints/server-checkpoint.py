from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/')
def classify_image():
    return "Hello"
  #   image_data = request.form['image_data']

  #   response = jsonify(util.classify_image(image_data))

  #   response.headers.add('Access-Control-Allow-Origin', '*')

  #    return response

if __name__ == "__main__":
   #  print("Starting Python Flask Server For Tennis Celebrity Image Classification")
 #  util.load_saved_artifacts()
   app.run(port=5000)

#if __name__ == "__main__":
#    from waitress import serve
#    serve(app, host="0.0.0.0", port=8080)