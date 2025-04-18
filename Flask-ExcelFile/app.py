import os
from flask import Flask, render_template,request,flash
import pandas as pd

app=Flask(__name__)
app.secret_key="123"

app.config["UPLOAD FOLDER1"]="static/Excelfile"

@app.route("/",methods=['GET','POST'])
def upload():
    if request.method=='POST':
       upload_Excelfile=request.file["upload-ExcelFile"]
    if upload_Excelfile.filename!='':
       file_path=os.path.join(app.config["UPLOAD FOLDER1"],upload_Excelfile.filename)
       upload_Excelfile.save(file_path)
       data=pd.read_Excelfile(upload_Excelfile)
    return render_template("ExcelFile.html",data=data.to_html(index=False).replace)
    flash("File upload successfully",'success')
    return render_template("UploadExcelFile.html")

if __name__ == "__main__":
    app.run(debug=True)