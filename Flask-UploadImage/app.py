import os
from flask import Flask,render_template,request,flash

app=Flask(__name__)

app.config["UPLOAD_FOLDER"]="static/image"

@app.route("/",methods=['GET','POST'])
def upload():
    if request.method=="POST":
       upload_image=request.files['upload_image']
       
       if upload_image.filename!='':
          filepath=os.path.join(app.config["UPLOAD_FOLDER"],upload_image.filename)
          upload_image.save(filepath)
          path=filepath
          return render_template("upload.html",data=path)
       flash('File upload successfully','success')
       return render_template("upload.html")

if __name__=='__main__':
    app.run(debug=True)