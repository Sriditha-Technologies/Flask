from flask import Flask,render_template,request,flash
import os

app=Flask(__name__)
app.config['UPLOAD-FOLDER1']="static/pdf"
app.config['UPLOAD-FOLDER2']="static/videos"
app.config['UPLOAD-FOLDER3']="static/document"
app.secret_key="123"

@app.route("/",methods=["GET","POST"])

def upload():
    if request.method=="POST":
       upload_pdf=request.files['upload_pdf']
       upload_videos=request.files['upload_videos']
       upload_document=request.files['upload_document']

       if upload_pdf.filename!='' and upload_videos.filename!='' and upload_document.filename!='':
          filepath1=os.path.join(app.config["UPLOAD-FOLDER1"],upload_pdf.filename)
          filepath2=os.path.join(app.config["UPLOAD-FOLDER2"],upload_videos.filename)
          filepath3=os.path.join(app.config["UPLOAD-FOLDER3"],upload_document.filename)

          upload_pdf.save(filepath1)
          upload_videos.save(filepath2)
          upload_document.save(filepath3)
          flash("File upload successfully","success")

    return render_template("upload.html")

if __name__ == '__main__':
    app.run(debug=True)