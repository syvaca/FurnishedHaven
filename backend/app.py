###########################################################################
print('Content-Type:text/html') #HTML is following
print("")                          #Leave a blank line

###########################################################################

from flask import Flask, request, render_template
import mysql.connector
from mysql.connector import Error
from flask_mail import Mail, Message

#app = Flask(__name__)

# Configure mail
'''
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-password'
mail = Mail(app)
'''

@app.route('/')
def booking_form():
    return render_template('booking.html')

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        style = request.form['style']
        service = request.form['service']

        # Save to MySQL database
        try: 
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Admin',
                database='FurnishedHaven'
             )
            if conn.is_connected():
                print('<p>Connected to MySQL database</p>')

                try:
                    cursor = conn.cursor()
                    query = ("INSERT INTO bookings (name, email, style, service)" # booking should maybe be called FurnishedHaven , idk
                    "VALUES (%s, %s, %s, %s)")
                    values = (name, email, style, service)
            
                    #cursor.execute("SELECT * FROM books")
                    cursor.execute(query, values)
                    conn.commit()
                   # row = cursor.fetchone()
                    #while row is not None:
                      #  print('<p>',row,'</p>')
                      #  row = cursor.fetchone()
                except Error as e:
                    print('<p>',e,'</p>')
                #finally:
                   # cursor.close()
                  #  print('<p>Cursor closed</p>')
              
        except mysql.connector.Error as err:
            print("Something went wrong: {}".format(err))
            # Handle the error appropriately in a real project
        finally:
            cursor.close()
            conn.close()
        
        
        # Send confirmation email - not needed for rn, this will send a persoanlized email to the user
        '''
        msg = Message('Booking Confirmation',
                      sender='useremail@example.com',
                      recipients=[email])
        msg.body = f"""
        Hello {name},

        Thank you for your booking.

        Booking Details:
        Name: {name}
        Email: {email}
        Style: {style}
        Service: {service}

        We will contact you shortly with more details.

        Best regards,
        Your Company Name
        """
        mail.send(msg)
        '''

        return 'Booking submitted and email sent successfully!'

if __name__ == '__main__':
    app.run(debug=True)

##################################################################

import cgi
import cgitb
cgitb.enable()

input_data=cgi.FieldStorage()

print('<h1>Thank you for your interest! A representative will reach out to you soon.</h1>')
