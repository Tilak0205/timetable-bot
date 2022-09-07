# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask,request

'''
{
    "B171325":{telegram_id:175256527,class=302},
    "B152626":{telegram_id:175256527,class=303}
}

'''


# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    args = request.args
    cls = args.get('class')
    day = args.get('day')
    print(cls,day)
    # cls = req.params["class"]
    # day = req.params["day"]
    def switch_day_302(day):
        if day=='monday':
            # print("09:00 AM TO 09:55 AM - ES(BS2201)")
            # print("10:00 AM TO 10:55 AM - DAA(CS2203)")
            # print("11:00 AM TO 11:55 AM - COA(CS2201)")
            result = "09:00 AM TO 09:55 AM - ES(BS2201)<br> 10:00 AM TO 10:55 AM - DAA(CS2203)<br> 11:00 AM TO 11:55 AM - COA(CS2201)"
            return result
        elif day=='tuesday':
            # print("09:00 AM TO 09:55 AM - DA(CS2204)")
            # print("10:00 AM TO 10:55 AM - DAA(CS2203)")
            # print("11:00 AM TO 11:55 AM - ES(BS2201)")
            # print("12:00 PM TO 12:55 PM - ME(BM2201)")
            # print("02:00 PM TO 05:55 PM - COA LAB(CS2801)")
            result ="09:00 AM TO 09:55 AM - DA(CS2204)<br>10:00 AM TO 10:55 AM - DAA(CS2203)<br>11:00 AM TO 11:55 AM - ES(BS2201)<br>12:00 PM TO 12:55 PM - ME(BM2201)<br>02:00 PM TO 05:55 PM - COA LAB(CS2801)"
            return result
        elif day=='wednesday':
            # print("09:00 AM TO 09:55 AM - DBMS(CS2202)")
            # print("10:00 AM TO 10:55 AM - DA(CS2204)")
            # print("11:00 AM TO 11:55 AM - COA(CS2201)")
            # print("02:00 PM TO 05:55 PM - DAA LAB(CS2803)")
            result="09:00 AM TO 09:55 AM - DBMS(CS2202)<br>10:00 AM TO 10:55 AM - DA(CS2204)<br>11:00 AM TO 11:55 AM - COA(CS2201)<br>02:00 PM TO 05:55 PM - DAA LAB(CS2803)"
            return result
        elif day=='thursday':
            # print("09:00 AM TO 09:55 AM - DA(CS2204)")
            # print("10:00 AM TO 10:55 AM - DAA(CS2203)")
            # print("11:00 AM TO 11:55 AM - DBMS(CS2202)")
            # print("02:00 PM TO 02:55 PM - ME(BM2201)")
            result="09:00 AM TO 09:55 AM - DA(CS2204)<br>10:00 AM TO 10:55 AM - DAA(CS2203)<br>11:00 AM TO 11:55 AM - DBMS(CS2202)<br>02:00 PM TO 02:55 PM - ME(BM2201)"
            return result
        elif day=='friday':
            # print("09:00 AM TO 09:55 AM - ES(BS2201)")
            # print("10:00 AM TO 10:55 AM - COA(CS2201)")
            # print("11:00 AM TO 11:55 AM - DBMS(CS2202)")
            # print("02:00 PM TO 05:55 PM - DBMS LAB(CS2802)")
            result= "09:00 AM TO 09:55 AM - ES(BS2201)<br>10:00 AM TO 10:55 AM - COA(CS2201)<br>11:00 AM TO 11:55 AM - DBMS(CS2202)<br>02:00 PM TO 05:55 PM - DBMS LAB(CS2802)"
            return result
        elif day=='saturday':
            # print("02:00 PM TO 02:55 PM - ME(BM2201)")
            result="02:00 PM TO 02:55 PM - ME(BM2201)"
            return result
        elif day=='sunday':
            # print("You don't have any classes today... Enjoy and Be productive in the weekend...")
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result

    def switch_day_303(day):
        if day=='monday':
            # print("09:00 AM TO 09:55 AM - DA(CS2204)")
            # print("10:00 AM TO 10:55 AM - COA(CS2201)")
            # print("11:00 AM TO 11:55 AM - DAA(CS2203)")
            # print("12:00 PM TO 12:55 PM - ES(BS2201)")
            # print("02:00 PM TO 05:55 PM - DBMS LAB(CS2802)")
            result ="09:00 AM TO 09:55 AM - DA(CS2204)<br>10:00 AM TO 10:55 AM - COA(CS2201)<br>11:00 AM TO 11:55 AM - DAA(CS2203)<br>12:00 PM TO 12:55 PM - ES(BS2201)<br>02:00 PM TO 05:55 PM - DBMS LAB(CS2802)"
            return result
        elif day=='tuesday':
            # print("09:00 AM TO 09:55 AM - DBMS(CS2202)")
            # print("10:00 AM TO 10:55 AM - COA(CS2201)")
            # print("11:00 AM TO 11:55 AM - DAA(CS2203)")
            # print("12:00 PM TO 12:55 PM - DA(CS2204)")
            result = "09:00 AM TO 09:55 AM - DBMS(CS2202)<br>10:00 AM TO 10:55 AM - COA(CS2201)<br>11:00 AM TO 11:55 AM - DAA(CS2203)<br>12:00 PM TO 12:55 PM - DA(CS2204)"
            return result
        elif day=='wednesday':
            # print("09:00 AM TO 09:55 AM - ES(BS2201)")
            # print("10:00 AM TO 10:55 AM - DBMS(CS2202)")
            # print("11:00 AM TO 11:55 AM - ME(BM2201)")
            # print("02:00 PM TO 05:55 PM - DAA LAB(CS2803)")
            result= "09:00 AM TO 09:55 AM - ES(BS2201)<br>10:00 AM TO 10:55 AM - DBMS(CS2202)<br>11:00 AM TO 11:55 AM - ME(BM2201)<br>02:00 PM TO 05:55 PM - DAA LAB(CS2803)"
            return result
        elif day=='thursday':
            # print("10:00 AM TO 10:55 AM - DBMS(CS2202)")
            # print("12:00 PM TO 12:55 PM - DAA(CS2203)")
            # print("02:00 PM TO 05:55 PM - COA LAB(CS2801)")
            result = "10:00 AM TO 10:55 AM - DBMS(CS2202)<br>12:00 PM TO 12:55 PM - DAA(CS2203)<br>02:00 PM TO 05:55 PM - COA LAB(CS2801)"
            return result
        elif day=='friday':
            # print("10:00 AM TO 10:55 AM - DA(CS2204)")
            # print("11:00 AM TO 11:55 AM - COA(CS2201)")
            # print("02:00 PM TO 02:55 PM - ME(BM2201)")
            result="10:00 AM TO 10:55 AM - DA(CS2204)<br>11:00 AM TO 11:55 AM - COA(CS2201)<br>02:00 PM TO 02:55 PM - ME(BM2201)\n"
            return result
        elif day=='saturday':
            # print("10:00 AM TO 10:55 AM - ME(BM2201)")
            # print("12:00 PM TO 12:55 PM - ES(BS2201)")
            result="10:00 AM TO 10:55 AM - ME(BM2201)<br>12:00 PM TO 12:55 PM - ES(BS2201)"
            return result
        elif day=='sunday':
            print("You don't have any classes today... Enjoy and Be productive in the weekend...")
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result
        
    def switch_day_304(day):
        if day=='monday':
            # print("09:00 AM TO 09:55 AM - ME(BM2201)")
            # print("10:00 AM TO 10:55 AM - ES(BS2201)")
            # print("11:00 AM TO 11:55 AM - DA(CS2204)")
            # print("12:00 PM TO 12:55 PM - DAA(CS2203)")
            # print("02:00 PM TO 05:55 PM - COA LAB(CS2801)")
            result="09:00 AM TO 09:55 AM - ME(BM2201)<br>10:00 AM TO 10:55 AM - ES(BS2201)<br>11:00 AM TO 11:55 AM - DA(CS2204)<br>12:00 PM TO 12:55 PM - DAA(CS2203)<br>02:00 PM TO 05:55 PM - COA LAB(CS2801)"
            return result
        elif day=='tuesday':
            # print("10:00 AM TO 10:55 AM - DBMS(CS2202)")
            # print("11:00 AM TO 11:55 AM - COA(CS2201)")
            # print("12:00 PM TO 12:55 PM - DAA(CS2203)")
            # print("02:00 PM TO 02:55 PM - ES(BS2201)")
            result = "10:00 AM TO 10:55 AM - DBMS(CS2202)<br>11:00 AM TO 11:55 AM - COA(CS2201)<br>12:00 PM TO 12:55 PM - DAA(CS2203)<br>02:00 PM TO 02:55 PM - ES(BS2201)"
            return result
        elif day=='wednesday':
            # print("09:00 AM TO 09:55 AM - DA(CS2204)")
            # print("10:00 AM TO 10:55 AM - COA(CS2201)")
            # print("11:00 AM TO 11:55 AM - DBMS(CS2202)")
            # print("12:00 PM TO 12:55 PM - ME(BM2201)")
            # print("02:00 PM TO 05:55 PM - DBMS LAB(CS2802)")
            result="09:00 AM TO 09:55 AM - DA(CS2204)<br>10:00 AM TO 10:55 AM - COA(CS2201)<br>11:00 AM TO 11:55 AM - DBMS(CS2202)<br>12:00 PM TO 12:55 PM - ME(BM2201)"
            return result
        elif day=='thursday':
            # print("09:00 AM TO 09:55 AM - ME(BM2201)")
            # print("10:00 AM TO 10:55 AM - ES(BS2201)")
            # print("11:00 AM TO 11:55 AM - DAA(CS2203)")
            # print("12:00 PM TO 12:55 PM - DA(CS2204)")
            result ="09:00 AM TO 09:55 AM - ME(BM2201)<br>10:00 AM TO 10:55 AM - ES(BS2201)<br>11:00 AM TO 11:55 AM - DAA(CS2203)<br>12:00 PM TO 12:55 PM - DA(CS2204)"
            return result
        elif day=='friday':
            # print("09:00 AM TO 09:55 AM - COA(CS2201)")
            # print("10:00 AM TO 10:55 AM - DBMS(CS2202)")
            # print("02:00 PM TO 05:55 PM - DAA LAB(CS2803)")
            result = "09:00 AM TO 09:55 AM - COA(CS2201)<br>10:00 AM TO 10:55 AM - DBMS(CS2202)<br>02:00 PM TO 05:55 PM - DAA LAB(CS2803)"
            return result
        elif day=='saturday':
            # print("04:00 PM TO 04:55 PM - ES(BS2201)")
            result="04:00 PM TO 04:55 PM - ES(BS2201)"
            return result
        elif day=='sunday':
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result


    def switch_day_305(day):
        if day=='monday':
            # print("10:00 AM TO 10:55 AM - COA(CS2201)")
            # print("11:00 AM TO 11:55 AM - DAA(CS2203)")
            # print("02:00 PM TO 02:55 PM - ES(BS2201)")
            # print("03:00 PM TO 03:55 PM - ME(BM2201)")
            result="10:00 AM TO 10:55 AM - COA(CS2201)<br>11:00 AM TO 11:55 AM - DAA(CS2203)<br>02:00 PM TO 02:55 PM - ES(BS2201)<br>03:00 PM TO 03:55 PM - ME(BM2201)"
            return result
        elif day=='tuesday':
            # print("09:00 AM TO 09:55 AM - DBMS(CS2202)")
            # print("10:00 AM TO 10:55 AM - DA(CS2204)")
            # print("11:00 AM TO 11:55 AM - COA(CS2201)")
            # print("02:00 PM TO 05:55 PM - DAA LAB(CS2803)")
            result="09:00 AM TO 09:55 AM - DBMS(CS2202)<br>10:00 AM TO 10:55 AM - DA(CS2204)<br>11:00 AM TO 11:55 AM - COA(CS2201)<br>02:00 PM TO 05:55 PM - DAA LAB(CS2803)"
            return result
        elif day=='wednesday':
            # print("09:00 AM TO 09:55 AM - DBMS(CS2202)")
            # print("10:00 AM TO 10:55 AM - COA(CS2201)")
            # print("11:00 AM TO 11:55 AM - DAA(CS2203)")
            # print("12:00 PM TO 12:55 PM - DA(CS2204)")
            # print("02:00 PM TO 05:55 PM - COA LAB(CS2801)")
            result="09:00 AM TO 09:55 AM - DBMS(CS2202)<br>10:00 AM TO 10:55 AM - COA(CS2201)<br>11:00 AM TO 11:55 AM - DAA(CS2203)<br>12:00 PM TO 12:55 PM - DA(CS2204)<br>02:00 PM TO 05:55 PM - COA LAB(CS2801)"
            return result
        elif day=='thursday':
            # print("09:00 AM TO 12:55 PM - DBMS LAB(CS2802)")
            # print("03:00 PM TO 03:55 PM - ME(BM2201)")
            result="09:00 AM TO 12:55 PM - DBMS LAB(CS2802)<br>03:00 PM TO 03:55 PM - ME(BM2201)"
            return result
        elif day=='friday':
            # print("09:00 AM TO 09:55 AM - DBMS(CS2202)")
            # print("11:00 AM TO 11:55 AM - DA(CS2204)")
            # print("12:00 AM TO 12:55 PM - DAA(CS2203)")
            # print("03:00 PM TO 03:55 PM - ES(BS2201)")
            # print("04:00 PM TO 04:55 PM - ME(BM2201)")
            result="09:00 AM TO 09:55 AM - DBMS(CS2202)<br>11:00 AM TO 11:55 AM - DA(CS2204)<br>12:00 AM TO 12:55 PM - DAA(CS2203)<br>03:00 PM TO 03:55 PM - ES(BS2201)<br>04:00 PM TO 04:55 PM - ME(BM2201)"
            return result
        elif day=='saturday':
            # print("02:00 PM TO 02:55 PM - ES(BS2201)")
            result="02:00 PM TO 02:55 PM - ES(BS2201)"
            return result
        elif day=='sunday':
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result
            
    def switch_day_012(day):
        if day=='monday':
            # print("10:00 AM TO 10:55 AM - DA(CS2204)")
            # print("11:00 AM TO 11:55 AM - COA(CS2201)")
            # print("12:00 PM TO 12:55 PM - ES(BS2201)")
            result="10:00 AM TO 10:55 AM - DA(CS2204)<br>11:00 AM TO 11:55 AM - COA(CS2201)<br>12:00 PM TO 12:55 PM - ES(BS2201)"
            return result
        elif day=='tuesday':
            # print("09:00 AM TO 09:55 AM - DAA(CS2203)")
            # print("10:00 AM TO 10:55 AM - DBMS(CS2202)")
            # print("11:00 AM TO 11:55 AM - DA(CS2204)")
            # print("12:00 PM TO 12:55 PM - COA(CS2201)")
            # print("02:00 PM TO 05:55 PM - DBMS LAB(CS2802)")
            result="09:00 AM TO 09:55 AM - DAA(CS2203)<br>10:00 AM TO 10:55 AM - DBMS(CS2202)<br>11:00 AM TO 11:55 AM - DA(CS2204)<br>12:00 PM TO 12:55 PM - COA(CS2201)<br>02:00 PM TO 05:55 PM - DBMS LAB(CS2802)"
            return result
        elif day=='wednesday':
            # print("09:00 AM TO 09:55 AM - ME(BM2201)")
            # print("10:00 AM TO 10:55 AM - DBMS(CS2202)")
            # print("11:00 AM TO 11:55 AM - COA(CS2201)")
            # print("12:00 PM TO 12:55 PM - DAA(CS2203)")
            # print("03:00 PM TO 03:55 PM - ES(BS2201)")
            result="09:00 AM TO 09:55 AM - ME(BM2201)<br>10:00 AM TO 10:55 AM - DBMS(CS2202)<br>11:00 AM TO 11:55 AM - COA(CS2201)<br>12:00 PM TO 12:55 PM - DAA(CS2203)<br>03:00 PM TO 03:55 PM - ES(BS2201)"
            return result
        elif day=='thursday':
            # print("09:00 AM TO 09:55 AM - ES(BS2201)")
            # print("10:00 AM TO 11:55 AM - ME(BM2201)")
            # print("02:00 PM TO 05:55 PM - DAA LAB(CS2803)")
            result="09:00 AM TO 09:55 AM - ES(BS2201)<br>10:00 AM TO 11:55 AM - ME(BM2201)<br>02:00 PM TO 05:55 PM - DAA LAB(CS2803)"
            return result
        elif day=='friday':
            # print("09:00 AM TO 09:55 AM - DA(CS2204)")
            # print("10:00 AM TO 10:55 AM - DBMS(CS2202)")
            # print("11:00 AM TO 11:55 AM - DAA(CS2203)")
            # print("12:00 PM TO 12:55 PM - ME(BM2201)")
            # print("02:00 PM TO 05:55 PM - COA LAB(CS2801)")
            result="09:00 AM TO 09:55 AM - DA(CS2204)<br>10:00 AM TO 10:55 AM - DBMS(CS2202)<br>11:00 AM TO 11:55 AM - DAA(CS2203)<br>12:00 PM TO 12:55 PM - ME(BM2201)<br>02:00 PM TO 05:55 PM - COA LAB(CS2801)"
            return result
        elif day=='saturday':
            # print("Chill bro")
            result="Chill bro"
            return result
        elif day=='sunday':
            # print("You don't have any classes today... Enjoy and Be productive in the weekend...")   
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."      
            return result

    def switch_cls(cls,day):
        if cls == "302":
            # day=input("Select Day: \n")
            return switch_day_302(day)
        elif cls == "303":
            # day=input("Select Day: \n")
            return switch_day_303(day)
        elif cls == "304":
            # day=input("Select Day: \n")
            return switch_day_304(day)
        elif cls == "305":
            # day=input("Select Day: \n")
            return switch_day_305(day)
        elif cls == "012":
            # day=input("Select Day: \n")
            return switch_day_012(day)

    # cls=input("Enter Class: \n")
    res = switch_cls(cls,day)
    print(res)
    return res
# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)
