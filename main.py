# This is a sample Python script.
import mysql.connector
from flask import Flask, request, render_template

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ujwala#13",
    database="bank"
)

mycursor = mydb.cursor()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/operations',methods=['POST'])
def operations():
    return render_template('operations.html')

@app.route('/branch',methods=['POST'])
def branch():
    return render_template('branch.html')

@app.route('/employee',methods=['POST'])
def employee():
    return render_template('employee.html')

@app.route('/customer',methods=['POST'])
def customer():
    return render_template('customer.html')

@app.route('/loan',methods=['POST'])
def loan():
    return render_template('loan.html')

@app.route('/viewE',methods=['POST'])
def viewE():
    return render_template('viewE.html')

@app.route('/viewEBr', methods=['POST'])
def viewEBr():
    if request.method=='POST':
        input1 = str(request.form.get('input1'))
        try:
            mycursor.execute("SELECT * FROM Employee where BId=%s",(input1,))
            myresult = mycursor.fetchall()
            if myresult==[] and input1!="None":
                return render_template('viewEBr.html',result="Data Not Found")
            return render_template('viewEBr.html',result=myresult)
             
        except mysql.connector.ProgrammingError as err:
            return render_template('viewEBr.html',result=myresult)     

    return render_template('viewEBr.html')

@app.route('/updateE', methods=['POST'])
def updateE():
    return render_template('updateE.html')

@app.route('/viewC', methods=['POST'])
def viewC():
    return render_template('viewC.html')

@app.route('/updateC', methods=['POST'])
def updateC():
    return render_template('updateC.html')

@app.route('/viewL', methods=['POST'])
def viewL():
    return render_template('viewL.html')

@app.route('/viewB',methods=['GET','POST'])
def viewB():
    if request.method=='POST':
        input1 = str(request.form.get('input1'))
        try:
            if input1:
                if input1=="all":
                    mycursor.execute("SELECT * FROM Branch")
                    myresult = mycursor.fetchall()
                    return render_template('viewB.html',result=myresult)
                else:
                    mycursor.execute("SELECT * FROM Branch where BName=%s",(input1,))
                    myresult = mycursor.fetchall()
                    if myresult==[] and input1!="None":
                        return render_template('viewB.html',result="Data Not Found")
                    return render_template('viewB.html',result=myresult)
        except mysql.connector.ProgrammingError as err:
            return render_template('viewB.html')     
    return render_template('viewB.html')

@app.route('/insertB',methods=['GET','POST'])
def insertB():
    try:
        if request.method=='POST':
            input1 = str(request.form.get('input1'))
            input2 = str(request.form.get('input2'))
            input3 = str(request.form.get('input3'))
            input4 = str(request.form.get('input4'))
            input5 = str(request.form.get('input5'))
            input6 = str(request.form.get('input6'))
            
            if (input1!="None") and (input2!="None") and (input3!="None") and (input4!= "None") and (input5!="None") and (input6!="None"):
                q = "Insert into branch Values (%s,%s,%s,%s,%s,%s)"
                v = (input1,input2,input3,input4,input5,input6)
                
                mycursor.execute(q,v)
                mydb.commit()
                
                mycursor.execute("Select * from Branch")
                data = mycursor.fetchall()
                return render_template('insertB.html',result=data)
        
    except mysql.connector.Error as err:
        return render_template('insertB.html',result="Found duplicate branch data")
        # if err.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
        #     # return "Error adding branch: BranchId already exists"
        #     return render_template('insertB.html',result="Found duplicate branch data")
        # else:
        #     # return "Error adding branch: {}".format(err)
        #     return render_template('insertB.html',result="Found duplicate branch data")
    return render_template('insertB.html')

@app.route('/updateB',methods=['GET','POST'])
def updateB():
    if request.method=='POST':
        input1 = str(request.form.get('input1'))
        input2 = str(request.form.get('input2'))
        if (input1!="None") and (input2!="None"):
            q = "Update branch set TelePh=%s where BranchId=%s"
            v = (input2,input1)

            mycursor.execute(q,v)
            mydb.commit()

            mycursor.execute("SELECT * FROM Branch where BranchId=%s",(input1,))
            data = mycursor.fetchall()
            return render_template('updateB.html',result=data)

    return render_template('updateB.html')

@app.route('/viewEAll',methods=['GET','POST'])
def viewEAll():
    if request.method=='POST':
        input1 = str(request.form.get('input1'))
        try:
            if input1=="all":
                mycursor.execute("SELECT * FROM employee")
                myresult = mycursor.fetchall()
                return render_template('viewEAll.html',result=myresult)
            else:
                mycursor.execute("SELECT * FROM employee where EmpId=%s",(input1,))
                myresult = mycursor.fetchall()
                if myresult==[] and input1!="None":
                    return render_template('viewEAll.html',result="Data Not Found")
                return render_template('viewEAll.html',result=myresult)
             
        except mysql.connector.ProgrammingError as err:
            return render_template('viewEAll.html',result="Data Not Found")     
    return render_template('viewEAll.html')

@app.route('/viewEBr1', methods=['GET', 'POST'])
def viewEBr1():
    if request.method == 'POST':
        input1 = str(request.form.get('input1'))
        try:

            mycursor.execute("SELECT * FROM Employee where BId=%s", (input1,))
            myresult = mycursor.fetchall()
            if myresult is None:
                return "Employee not found"
            return render_template('viewEBr1.html', result=myresult)

        except mysql.connector.ProgrammingError as err:
            return "Error finding Employee: Employee NOT Found"
    return render_template('viewEBr1.html')

@app.route('/viewEDept', methods=['GET', 'POST'])
def viewEDept():
    if request.method == 'POST':
        input1 = str(request.form.get('input1'))
        input2 = str(request.form.get('input2'))
        try:

            mycursor.execute("SELECT * FROM Employee where BId=%s  and dept=%s", (input1, input2))
            myresult = mycursor.fetchall()
            if myresult is None:
                return "Employee not found"
            return render_template('viewEDept.html', result=myresult)

        except mysql.connector.ProgrammingError as err:
            return "Error finding Employee: Employee NOT Found"
    return render_template('viewEDept.html')

@app.route('/insertE', methods=['GET', 'POST'])
def insertE():
    try:
        if request.method == 'POST':
            input1 = str(request.form.get('input1'))
            input2 = str(request.form.get('input2'))
            input3 = str(request.form.get('input3'))
            input4 = str(request.form.get('input4'))
            input5 = str(request.form.get('input5'))
            input6 = str(request.form.get('input6'))
            input7 = str(request.form.get('input7'))

            if (input1 != "None") and (input2 != "None") and (input3 != "None") and (input4 != "None") and (
                    input5 != "None") and (input6 != "None") and (input7 != "None"):
                q = "Insert into employee Values (%s,%s,%s,%s,%s,%s,%s)"
                v = (input1, input2, input3, input4, input5, input6, input7)

                mycursor.execute(q, v)
                mydb.commit()

                mycursor.execute("Select * from employee")
                data = mycursor.fetchall()
                return render_template('insertE.html', result=data)

    except mysql.connector.Error as err:
        return render_template('insertE.html',result="Found duplicate employee data")
    return render_template('insertE.html')

@app.route('/updateEPhno', methods=['GET', 'POST'])
def updateEPhno():
    try:
        if request.method == 'POST':
            input1 = str(request.form.get('input1'))
            input2 = str(request.form.get('input2'))
            if (input1 != "None") and (input2 != "None"):
                q = "Update Employee set PhNo=%s where EmpId=%s"
                v = (input2, input1)

                mycursor.execute(q, v)
                mydb.commit()

                mycursor.execute("SELECT * FROM Employee where EmpId=%s", (input1,))
                data = mycursor.fetchall()
                if data==[] and input1!="None" and input2!="None":
                    return render_template('updateEPhno.html',result="Could not update")
                return render_template('updateEPhno.html', result=data)
    except:
        return render_template('updateEPhno.html',result="Could not update")

    return render_template('updateEPhno.html')

@app.route('/updateESal', methods=['GET', 'POST'])
def updateESal():
    try:
        if request.method == 'POST':
            input1 = str(request.form.get('input1'))
            input2 = str(request.form.get('input2'))
            if (input1 != "None") and (input2 != "None"):
                q = "Update employee set salary=%s where EmpId=%s"
                v = (input2, input1)

                mycursor.execute(q, v)
                mydb.commit()

                mycursor.execute("SELECT * FROM Employee where EmpId=%s", (input1,))
                data = mycursor.fetchall()
                if data==[] and input1!="None" and input2!="None":
                    return render_template('updateESal.html',result="Could not update")
                return render_template('updateESal.html', result=data)
    except:
        return render_template('updateESal.html',result="Could not update")
    return render_template('updateESal.html')

# @app.route('/viewEC', methods=['GET', 'POST'])
# def viewEC():
#     mycursor.execute("SELECT count(*) FROM Employee")
#     myresult = mycursor.fetchone()[0]
#     if myresult is None:
#         return "Employee not found"
#     return render_template('viewEC.html', result=myresult)

#     # return render_template('viewEC.html')


# @app.route('/viewECBr', methods=['GET', 'POST'])
# def viewECBr():
#     if request.method == 'POST':
#         input1 = str(request.form.get('input1'))
#         try:

#             mycursor.execute("SELECT count(*) FROM employee where BId=%s", (input1,))
#             myresult = mycursor.fetchone()[0]
#             if myresult is None:
#                 return "No Employees"
#             return render_template('viewECBr.html', result=myresult)

#         except mysql.connector.ProgrammingError as err:
#             return "Error finding Employee: Employee NOT Found"
#     return render_template('viewECBr.html')

@app.route('/updateEdp', methods=['GET', 'POST'])
def updateEdp():
    try: 
        if request.method == 'POST':
            input1 = str(request.form.get('input1'))
            input2 = str(request.form.get('input2'))
            if (input1 != "None") and (input2 != "None"):
                q = "Update employee set dept=%s where EmpId=%s"
                v = (input2, input1)

                mycursor.execute(q, v)
                mydb.commit()

                mycursor.execute("SELECT * FROM employee where EmpId=%s", (input1,))
                data = mycursor.fetchall()
                if data==[] and input1!="None" and input2!="None":
                    return render_template('updateEdp.html',result="Could not update")
                return render_template('updateEdp.html', result=data)
    except:
        return render_template('updateEdp.html',result="Could not update")
    return render_template('updateEdp.html')

@app.route('/deleteE', methods=['GET', 'POST'])
def deleteE():
    try:
        if request.method == 'POST':
            input1 = str(request.form.get('input1'))
            if (input1 != "None"):
                
                mycursor.execute("select EName from Employee where EmpId=%s",(input1,))
                name = mycursor.fetchall()
                print(name)

                q = "delete from Employee where EmpId=%s"
                v = (input1,)

                data2=mycursor.execute(q, v)
                mydb.commit()
                
                print(data2)
                print(input1)
                if name==[]:
                    return render_template('deleteE.html',result="Employee does not exist")
                else:
                    mycursor.execute("SELECT * FROM employee")
                    data = mycursor.fetchall()
                    return render_template('deleteE.html', result=data)
    except:
        return render_template('deleteE.html',result="Employee does not exist")
    return render_template('deleteE.html')

@app.route('/insertC', methods=['GET', 'POST'])
def insertC():
    try:
        if request.method == 'POST':
            input1 = str(request.form.get('input1'))
            input2 = str(request.form.get('input2'))
            input3 = str(request.form.get('input3'))
            input4 = str(request.form.get('input4'))
            input5 = str(request.form.get('input5'))
            input6 = str(request.form.get('input6'))
            input7 = str(request.form.get('input7'))
            input8 = str(request.form.get('input8'))
            input9 = str(request.form.get('input9'))

            if (input1 != "None") and (input2 != "None") and (input3 != "None") and (input4 != "None") and (
                    input5 != "None") and (input6 != "None") and (input7 != "None") and (input8 != "None") and (input9 != "None"):
                q = "Insert into customer(AccNo,BrId,Name,Age,Gender,PhNo,AadharNo,Balance,City,PIN) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                v = (input1, input2, input3, input4, input5, input6,input7,input8,input9)

                mycursor.execute(q, v)
                mydb.commit()

                mycursor.execute("Select * from customer")
                data = mycursor.fetchall()
                return render_template('insertC.html', result=data)

    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
            return "Error adding branch: BranchId already exists"
        else:
            return "Error adding branch:{}".format(err)
    return render_template('insertC.html')

@app.route('/viewCBr', methods=['GET', 'POST'])
def viewCBr():
    if request.method == 'POST':
        input1 = str(request.form.get('input1'))
        try:
            mycursor.execute("SELECT * FROM customer where BrId=%s", (input1,))
            myresult = mycursor.fetchall()
            if myresult==[] and input1!="None":
                return render_template('viewCBr.html',result="Data Not Found")
            return render_template('viewCBr.html', result=myresult)

        except mysql.connector.ProgrammingError as err:
            return render_template('viewCBr.html',result="Data Not Found")
    return render_template('viewCBr.html')

@app.route('/viewCAll', methods=['GET', 'POST'])
def viewCAll():
    if request.method == 'POST':
        input1 = str(request.form.get('input1'))
        try:
            if input1 == "all":
                mycursor.execute("SELECT * FROM customer")
                myresult = mycursor.fetchall()
                return render_template('viewCAll.html', result=myresult)
            else:
                mycursor.execute("SELECT * FROM customer where AccNo=%s", (input1,))
                myresult = mycursor.fetchall()
                if myresult==[] and input1!="None":
                    return render_template('viewCAll.html',result="Data Not Found")
                return render_template('viewCAll.html', result=myresult)

        except mysql.connector.ProgrammingError as err:
            return render_template('viewCAll.html', result="Data Not Found")
    return render_template('viewCAll.html')

@app.route('/updateCPh', methods=['GET', 'POST'])
def updateCPh():
    try:
        if request.method == 'POST':
            input1 = str(request.form.get('input1'))
            input2 = str(request.form.get('input2'))
            if (input1 != "None") and (input2 != "None"):
                q = "Update customer set PhNo=%s where AccNo=%s"
                v = (input2, input1)

                mycursor.execute(q, v)
                mydb.commit()

                mycursor.execute("SELECT * FROM customer where AccNo=%s", (input1,))
                data = mycursor.fetchall()
                if data==[] and input1!="None" and input2!="None":
                    return render_template('updateCPh.html',result="Could not update")
                return render_template('updateCPh.html', result=data)
    except:
        return render_template('updateCPh.html',result="Could not update")

    return render_template('updateCPh.html')

@app.route('/updateCBr', methods=['GET', 'POST'])
def updateCBr():
    if request.method == 'POST':
        input1 = str(request.form.get('input1'))
        input2 = str(request.form.get('input2'))
        if (input1 != "None") and (input2 != "None"):
            q = "Update customer set BrId=%s where AccNo=%s"
            v = (input2, input1)

            mycursor.execute(q, v)
            mydb.commit()

            mycursor.execute("SELECT * FROM customer where AccNo=%s", (input1,))
            data = mycursor.fetchall()
            return render_template('updateCBr.html', result=data)

    return render_template('updateCBr.html')

@app.route('/deleteC', methods=['GET', 'POST'])
def deleteC():
    if request.method == 'POST':
        input1 = str(request.form.get('input1'))
        if (input1 != "None"):
            q = "delete from customer where AccNo=%s"
            v = (input1,)

            mycursor.execute(q, v)
            mydb.commit()

            mycursor.execute("SELECT * FROM customer ")
            data = mycursor.fetchall()
            return render_template('deleteC.html', result=data)

    return render_template('deleteC.html')

@app.route('/viewEC', methods=['GET', 'POST'])
def viewEC():
    mycursor.execute("SELECT count(*) FROM Employee")
    myresult = mycursor.fetchone()[0]
    if myresult is None:
        return "Employee not found"
    return render_template('viewEC.html', result=myresult)

    # return render_template('viewEC.html')


@app.route('/viewECBr', methods=['GET', 'POST'])
def viewECBr():
    if request.method == 'POST':
        input1 = str(request.form.get('input1'))
        try:
            mycursor.execute("SELECT count(*) FROM employee where BId=%s", (input1,))
            myresult = mycursor.fetchone()[0]
            if myresult==0 and input1!="None":
                return render_template('viewECBr.html', result="Data Not Found")
            return render_template('viewECBr.html', result=myresult)

        except mysql.connector.ProgrammingError as err:
            return render_template('viewECBr.html', result="Data Not Found")
    return render_template('viewECBr.html')

@app.route('/viewLAll', methods=['GET', 'POST'])
def viewLAll():
    mycursor.execute("SELECT * FROM applied Inner Join loan on LNo=LoanId")
    myresult = mycursor.fetchall()
    if myresult is None:
        return "Employee not found"
    return render_template('viewLAll.html', result=myresult)

@app.route('/viewLC', methods=['GET', 'POST'])
def viewLC():
    mycursor.execute("select substr(LoanId,1,1) as BranchNo, count(*) as loans from loan group by substr(LoanId,1,1) order by BranchNo asc;")
    myresult = mycursor.fetchall()
    if myresult is None:
        return render_template('viewLC.html')
    return render_template('viewLC.html', result=myresult)


@app.route('/viewLBr', methods=['GET', 'POST'])
def viewLBr():
    if request.method == 'POST':
        input1 = str(request.form.get('input1'))
        if input1=="1":
            mycursor.execute("SELECT * FROM loan WHERE SUBSTRING(LoanId, 1, 1) = '1'")
            myresult = mycursor.fetchall()
            return render_template('viewLBr.html',result=myresult)
        elif input1=="2":
            mycursor.execute("SELECT * FROM loan WHERE SUBSTRING(LoanId, 1, 1) = '2'")
            myresult = mycursor.fetchall()
            return render_template('viewLBr.html',result=myresult)
        elif input1=="3":
            mycursor.execute("SELECT * FROM loan WHERE SUBSTRING(LoanId, 1, 1) = '3'")
            myresult = mycursor.fetchall()
            return render_template('viewLBr.html',result=myresult)
        elif input1=="4":
            mycursor.execute("SELECT * FROM loan WHERE SUBSTRING(LoanId, 1, 1) = '4'")
            myresult = mycursor.fetchall()
            return render_template('viewLBr.html',result=myresult)
        elif input1=="5":
            mycursor.execute("SELECT * FROM loan WHERE SUBSTRING(LoanId, 1, 1) = '5'")
            myresult = mycursor.fetchall()
            return render_template('viewLBr.html',result=myresult)
        elif input1=="6":
            mycursor.execute("SELECT * FROM loan WHERE SUBSTRING(LoanId, 1, 1) = '6'")
            myresult = mycursor.fetchall()
            return render_template('viewLBr.html',result=myresult)
        else:
            return render_template('viewLBr.html')
    return render_template('viewLBr.html')

# @app.route('/viewLBr', methods=['GET', 'POST'])
# def viewLBr():
#     if request.method == 'POST':
#         input1 = str(request.form.get('input1'))
#         mycursor.execute("SELECT * FROM loan WHERE SUBSTRING(LoanId, 1, 1) = '%s'",(input1,))
#         myresult = mycursor.fetchall()
#         if myresult is None:
#             return render_template('viewLBr.html', result="Data Not Found")
#         return render_template('viewLBr.html', result=myresult)

# @app.route('/viewLBr', methods=['GET', 'POST'])
# def viewLBr():
#     if request.method == 'POST':
#         # input1 = str(request.form.get('input1'))

#         mycursor.execute("SELECT * FROM loan WHERE SUBSTRING(LoanId, 1, 1) = '1'")
#         myresult = mycursor.fetchall()
#         print(myresult)
#         # if myresult is None:
#         #     return render_template("viewLBr.html", result="Data Not Found")
#         render_template("viewLBr.html", result=myresult)


#         # try:
#         #     mycursor.execute("SELECT * FROM loan WHERE SUBSTRING(LoanId, 1, 1) = '1'")
#         #     myresult = mycursor.fetchall()
#         #     print(myresult)
#         #     # if myresult is None:
#         #     #     return render_template("viewLBr.html", result="Data Not Found")
#         #     render_template("viewLBr.html", result=myresult)
#         # except:
#         #     return render_template("viewLBr.html", result="Data Not Found")
#     render_template("viewLBr.html")

if __name__=='__main__':
    app.run(debug=True)