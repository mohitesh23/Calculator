from flask import Flask,request,render_template
app = Flask(__name__)


@app.route("/calculator/",methods=["GET","POST"])


def calculator_main():
    if request.method=="POST":
        result = 0
        resp = request.form
        a = resp.get('fnum')
        b = resp.get('snum')

        if resp.get('calc')==1:
            try:
                result = int(a)+int(b)
            except:
                result = 'Please Enter Valid Number'

        elif resp.get('calc') == 2:
            try:
                result = int(a)-int(b)
            except:
                result = 'Please Enter Valid Number'

        elif resp.get('calc') == 3:
            try:
                result = int(a)*int(b)
            except:
                result = 'Please Enter Valid Number'

        elif resp.get('calc') == 4:
            try:
                result = int(a)/int(b)
            except:
                result = 'Please Enter Valid Number'

        return render_template("calci1.html",resp=result,num1=a,num2=b)

    else:

        return render_template("calci.html")

if __name__ == '__main__':
    app.run(debug=True)