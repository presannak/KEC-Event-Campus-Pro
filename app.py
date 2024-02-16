from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

admin_authenticated = False
user_authenticated = False

import pymysql
def connector():
    conn=pymysql.connect(user='root',
                         host='localhost',
                         db='agilepro',
                         password='Rajdeepak_SQL',
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor)
    c=conn.cursor()
    return conn,c

  
    # dob = db.Column(db.String(10))
    # gender = db.Column(db.String(10))
    # address = db.Column(db.String(200))
    # city = db.Column(db.String(50))
    # state = db.Column(db.String(50))


# Simulated database of available halls with associated data
available_halls = [
    
    {"name": "EEE Seminar Hall13d", "event": "---", "date": "---", "status": "Available"},
    {"name": "IT Seminar Hall-24e", "event": "Guest Lecture", "date": "31 Aug 2023", "status": "Available"},
    {"name": "IT Park Seminar Hall-17h", "event": "---", "date": "---", "status": "Available"},
]



@app.route("/")
def login():
    return render_template("fp.html")

@app.route("/FrontLogin.html")
def FrontLogin():
    return render_template("FrontLogin.html")

@app.route("/UserFrontLogin.html")
def UserFrontLogin():
    return render_template("UserFrontLogin.html")






# @app.route('/index')
# def index():
#     hall_name = "MBA Seminar Hall"
#     hall_data = None

#     for hall in available_halls:
#         if hall["name"] == hall_name:
#             hall_data = hall
#             break


#     for hall in available_halls:
#         if hall["name"] == hall_name and hall["status"] == "Booked":
#             return render_template('index.html', message="MBA Seminar Hall is already booked.")

#     if hall_data:
#         hall_event = hall_data["event"]
#         hall_date = hall_data["date"]
#         hall_status = hall_data["status"]
#     else:
#         hall_event = "--"
#         hall_date = "--"
#         hall_status = "Available"


@app.route('/index')
def index():
    hall_name = "MBA Seminar Hall"
    hall_data = None

    for hall in available_halls:
        if hall["name"] == hall_name:
            hall_data = hall
            break

    if hall_data:
        hall_event = hall_data["event"]
        hall_date = hall_data["date"]
        hall_status = hall_data["status"]
    else:
        hall_event = "--"
        hall_date = "--"
        hall_status = "Available"



    hall_name1 = "EEE Seminar Hall"
    hall_data1 = None

    for hall1 in available_halls:
        if hall1["name"] == hall_name1:
            hall_data1 = hall1
            break

    if hall_data1:
        hall_event1 = hall_data1["event"]
        hall_date1 = hall_data1["date"]
        hall_status1 = hall_data1["status"]
    else:
        hall_event1 = "--"
        hall_date1 = "--"
        hall_status1 = "Available"


    # hall_name2 = "IT Seminar Hall-2"
    # hall_data2 = None

    # for hall2 in available_halls:
    #     if hall2["name"] == hall_name2:
    #         hall_data2 = hall2
    #         break

    # if hall_data2:
    #     hall_event2 = hall_data2["event"]
    #     hall_data2 = hall_data2["date"]
    #     hall_status2 = hall_data2["status"]
    # else:
    #     hall_event2 = "--"
    #     hall_date2 = "--"
    #     hall_status2 = "Available"

    hall_name2 = "IT Seminar Hall-2"
    hall_data2 = None

    for hall2 in available_halls:
        if hall2["name"] == hall_name2:
            hall_data2 = hall2
            break

    if hall_data2:
        hall_event2 = hall_data2.get("event", "--")
        hall_date2 = hall_data2.get("date", "--")
        hall_status2 = hall_data2.get("status", "Available")
    else:
        hall_event2 = "--"
        hall_date2 = "--"
        hall_status2 = "Available"




    hall_name3 = "IT Seminar Hall-1"
    hall_data3 = None

    for hall3 in available_halls:
        if hall3["name"] == hall_name3:
            hall_data3 = hall3
            break

    if hall_data3:
        hall_event3 = hall_data3.get("event", "--")
        hall_date3 = hall_data3.get("date", "--")
        hall_status3 = hall_data3.get("status", "Available")
    else:
        hall_event3 = "--"
        hall_date3 = "--"
        hall_status3 = "Available"

    # hall_name3 = "IT Seminar Hall-1"
    # hall_data3 = None
    # hall_event3 = "--"
    # hall_date3 = "--"
    # hall_status3 = "Available"

    # # Check if the hall is already booked
    # hall_already_booked = False
    # for hall3 in available_halls:
    #     if hall3["name"] == hall_name3 and hall3["status"] == "Booked":
    #         hall_already_booked = True
    #         break

    # if not hall_already_booked:
    #     # If the hall is not already booked, proceed with booking
    #     for hall3 in available_halls:
    #         if hall3["name"] == hall_name3:
    #             hall_data3 = hall3
    #             hall_data3["event"] = "New Event"  # Replace "New Event" with your actual event name
    #             hall_data3["date"] = "New Date"    # Replace "New Date" with your actual date
    #             hall_data3["status"] = "Booked"    # Update the status to "Booked"
    #             hall_event3 = hall_data3.get("event", "--")
    #             hall_date3 = hall_data3.get("date", "--")
    #             hall_status3 = hall_data3.get("status", "Available")
    #             break

    #     print(f"Hall booked successfully! Event: {hall_event3}, Date: {hall_date3}, Status: {hall_status3}")
    # else:
    #     # If the hall is already booked, display an alert message
    #     print("Error: The hall is already booked.")




    return render_template('index.html',  hall_event=hall_event, hall_date=hall_date, hall_status=hall_status,hall_event1=hall_event1, hall_date1=hall_date1, hall_status1=hall_status1,hall_event2=hall_event2, hall_date2=hall_date2, hall_status2=hall_status2,hall_event3=hall_event3, hall_date3=hall_date3, hall_status3=hall_status3)



@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route("/blocks.html")
def blocks():
    return render_template("blocks.html")

@app.route("/halls.html")
def halls():
    return render_template("halls.html")


@app.route("/Eventreg.html")
def Eventreg():
    return render_template("Eventreg.html")

@app.route("/RegisterEvent.html")
def RegisterEvent():
    return render_template("RegisterEvent.html")

@app.route("/admin.html")
def admin():
    return render_template("admin.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/cc.html")
def cc():
    return render_template("cc.html")

@app.route("/maha.html")
def maha():
    return render_template("maha.html")

@app.route("/sri.html")
def sri():
    return render_template("sri.html")

@app.route("/ck.html")
def ck():
    return render_template("ck.html")

@app.route("/cv.html")
def cv():
    return render_template("cv.html")

@app.route("/civilblock.html")
def civilblock():
    return render_template("civilblock.html")

@app.route("/mechblock.html")
def mechblock():
    return render_template("mechblock.html")

@app.route("/mhtrsblock.html")
def mhtrsblock():
    return render_template("mhtrsblock.html")

@app.route("/automobileblock.html")
def automobileblock():
    return render_template("automobileblock.html")

@app.route("/chemicalblock.html")
def chemicalblock():
    return render_template("chemicalblock.html")

@app.route("/ftblock.html")
def ftblock():
    return render_template("ftblock.html")

@app.route("/eeeblock.html")
def eeeblock():
    return render_template("eeeblock.html")

@app.route("/eieblock.html")
def eieblock():
    return render_template("eieblock.html")

@app.route("/eceblock.html")
def eceblock():
    return render_template("eceblock.html")

@app.route("/cseblock.html")
def cseblock():
    return render_template("cseblock.html")

@app.route("/itblock.html")
def itblock():
    return render_template("itblock.html")

@app.route("/csdblock.html")
def csdblock():
    return render_template("csdblock.html")

@app.route("/aidsblock.html")
def aidsblock():
    return render_template("aidsblock.html")

@app.route("/aimlblock.html")
def aimlblock():
    return render_template("aimlblock.html")

@app.route("/fp.html")
def fp():
    return render_template("fp.html")

@app.route("/civilevent.html")
def civilevent():
    return render_template("civilevent.html")

@app.route("/mechevent.html")
def mechevent():
    return render_template("mechevent.html")

@app.route("/mhtrsevent.html")
def mhtrsevent():
    return render_template("mhtrsevent.html")

@app.route("/autoevent.html")
def autoevent():
    return render_template("autoevent.html")

@app.route("/chemicalevent.html")
def chemicalevent():
    return render_template("chemicalevent.html")

@app.route("/ftevent.html")
def ftevent():
    return render_template("ftevent.html")

@app.route("/eeeevent.html")
def eeeevent():
    return render_template("eeeevent.html")

@app.route("/eieevent.html")
def eieevent():
    return render_template("eieevent.html")

@app.route("/eceevent.html")
def eceevent():
    return render_template("eceevent.html")

@app.route("/cseevent.html")
def cseevent():
    return render_template("cseevent.html")

@app.route("/itevent.html")
def itevent():
    return render_template("itevent.html")

@app.route("/csdevent.html")
def csdevent():
    return render_template("csdevent.html")

@app.route("/aidsevent.html")
def aidsevent():
    return render_template("aidsevent.html")

@app.route("/aimlevent.html")
def aimlevent():
    return render_template("aimlevent.html")

@app.route("/Bookingform.html")
def Bookingform():
    
    return render_template("Bookingform.html")

@app.route("/feedback.html")
def feedback():
    return render_template("feedback.html")

@app.route('/FrontLogin.html',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('adminfname')
        contact = request.form.get('admincontact')
        email = request.form.get('adminsignupemail')
        password = request.form.get('adminsignuppass')

        try:
            conn, c = connector()
            data = (name, contact, email, password)
            insert_query = "INSERT INTO signup (name, contact, email, password) VALUES (%s, %s, %s, %s)"
            c.execute(insert_query, data)
            conn.commit()
        except pymysql.Error as e:
            print(f"Database error: {e}")
        finally:
            if c:
                c.close()
            if conn:
                conn.close()

        print(name, contact, email, password)
        message1 = "Sign-up successful! You are now signin."
        return render_template('FrontLogin.html',message1=message1)
    return redirect(url_for('index'))

@app.route('/UserFrontLogin',methods=['GET','POST'])
def userform():
    if request.method == 'POST':
        name = request.form.get('userfname')
        contact = request.form.get('usercontact')
        email = request.form.get('usersignupemail')
        password = request.form.get('usersignuppass')

        try:
            conn, c = connector()
            data = (name, contact, email, password)
            insert_query = "INSERT INTO usersignup (name, contact, email, password) VALUES (%s, %s, %s, %s)"
            c.execute(insert_query, data)
            conn.commit()
        except pymysql.Error as e:
            print(f"Database error: {e}")
        finally:
            if c:
                c.close()
            if conn:
                conn.close()
        message2 = "Sign-up successful! You are now signin."
        print(name, contact, email, password)
        return render_template('UserFrontLogin.html',message2=message2)
    return redirect('/index')

@app.route("/Signin", methods=['POST', 'GET'])
def form1():
    if request.method == 'POST':
        email = request.form.get('adminemail')
        password = request.form.get('adminpassword')

        try:
            conn, c = connector()

            # Query to retrieve user data based on email
            select_query = "SELECT * FROM signup WHERE email = %s"
            c.execute(select_query, (email,))
            user = c.fetchone()

            if user and user['password'] == password:
                return redirect(url_for('index'))
            else:
                message = 'Invalid email or password'
                return render_template('FrontLogin.html', message=message)

        except pymysql.Error as e:
            print(f"Database error: {e}")
        finally:
            if c:
                c.close()
            if conn:
                conn.close()

    return render_template("Frontlogin.html")

@app.route("/UserSignin", methods=['POST', 'GET'])
def userform1():
    if request.method == 'POST':
        email = request.form.get('useremail')
        password = request.form.get('userpassword')

        try:
            conn, c = connector()

            # Query to retrieve user data based on email
            select_query = "SELECT * FROM usersignup WHERE email = %s"
            c.execute(select_query, (email,))
            user = c.fetchone()

            if user and user['password'] == password:
                return render_template('index.html')
            else:
                message3 = 'Invalid email or password'
                return render_template('UserFrontLogin.html', message3=message3)

        except pymysql.Error as e:
            print(f"Database error: {e}")
        finally:
            if c:
                c.close()
            if conn:
                conn.close()

    return render_template("Frontlogin.html")

@app.route('/Bookingform',methods=['GET','POST'])
def booking():
    if(request.method=='POST'):
        Hallname=request.form.get('hall')
        Department=request.form.get('dept')
        Eventname=request.form.get('name')
        Clubname=request.form.get('club')
        Phno=request.form.get('phno')
        DOB=request.form.get('dob')
        Start=request.form.get('start')
        End=request.form.get('end')
        conn,c=connector()
        c.execute("INSERT INTO booking VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(Department,Eventname,Clubname,Phno,DOB,Start,End,Hallname))
        conn.commit()
        conn.close()
        c.close()
        print(Department,Eventname,Clubname,Phno,DOB,Start,End,Hallname)
        new_hall = {
        "name": request.form['hall'],
        "event": request.form['name'],
        "date": request.form['dob'],
        "status":"Booked",
        }
        available_halls.append(new_hall)
    return redirect(url_for('index'))


if __name__ == "__main__":
   
   app.run(debug=True)






