from flask import Flask, request, render_template, send_file
     import os
     from spleeter.separator import Separator

     app = Flask(__name__)

     @app.route('/')
     def index():
         return render_template('index.html')

     @app.route('/upload', methods=['POST'])
     def upload():
         file = request.files['file']
         file_path = f"uploads/{file.filename}"
         file.save(file_path)

         # Separate vocals using Spleeter
         separator = Separator('spleeter:2stems')
         separator.separate_to_file(file_path, 'output')

         # Return the processed file
         return send_file(f"output/{file.filename}/accompaniment.wav", as_attachment=True)

     if __name__ == '__main__':
         os.makedirs('uploads', exist_ok=True)
         os.makedirs('output', exist_ok=True)
         app.run(debug=True)
