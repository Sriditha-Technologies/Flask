from flask import Flask,render_template,request,flash

app=Flask(__name__)
app.secret_key="123"

@app.route("/",methods=['GET','POST'])
def home():
   if request.method=="POST":
      if request.form.get("success"):
         flash("Success Message","success")
      elif request.form.get("warning"):
         flash("warning Message","warning")
      elif request.form.get("primary"):
         flash("primary Message","primary")
      elif request.form.get("secondary"):
         flash("secondary Message","secondary")
      elif request.form.get("info"):
         flash("info Message","info")
      elif request.form.get("danger"):
         flash("danger Message","danger")
      elif request.form.get("dark"):
         flash("dark Message","dark")
    
   return render_template("index.html")

if __name__=='__main__':
   app.run(debug=True)