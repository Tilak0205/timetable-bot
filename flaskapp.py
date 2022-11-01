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
    def switch_day_114(day):
        if day=='monday':
            result = "09:00 AM TO 09:55 AM - AI(CS31XX)\n10:00 AM TO 10:55 AM - OOPS(CS3102)\n11:00 AM TO 11:55 AM - FLAT(CS3103)\n12:00 PM TO 12:55 PM SS(EC3106)"
            return result
        elif day=='tuesday':
            result ="09:00 AM TO 09:55 AM - SS(EC3106)\n10:00 AM TO 10:55 AM - OOPS(CS3102)\n11:00 AM TO 11:55 AM - AI(CS31XX)\n12:00 PM TO 12:55 PM - OS(CS3101)\n02:00 PM TO 02:55 PM POM(BM002)"
            return result
        elif day=='wednesday':
            result="09:00 AM TO 09:55 AM - POM(BM002)\n10:00 AM TO 10:55 AM - FLAT(CS3103)\n11:00 AM TO 11:55 AM - SOFT SKILLS(HS3101)\n12:00 PM TO 12:55 PM - OS(CS3101)"
            return result
        elif day=='thursday':
            result="09:00 AM TO 09:55 AM - OOPS(CS3102)\n10:00 AM TO 10:55 AM - FLAT(CS3103)n11:00 AM TO 11:55 AM - AI(CS31XX)\n12:00 PM TO 12:55 PM - SOFT SKILLS(HS3101)\n02:00 PM TO 05:55 PM OOPS LAB(CS3702)"
            return result
        elif day=='friday':
            result= "09:00 AM TO 09:55 AM - OS(CS3101)\n10:00 AM TO 10:55 AM - SS(EC3106)\n11:00 AM TO 11:55 AM - POM(BM002)\n02:00 PM TO 05:55 PM - OS LAB(CS3701)"
            return result
        elif day=='saturday':
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result
        elif day=='sunday':
            # print("You don't have any classes today... Enjoy and Be productive in the weekend...")
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result

    def switch_day_103(day):
        if day=='monday':
            result ="09:00 AM TO 09:55 AM - OS(CS3101)\n10:00 AM TO 10:55 AM - AI(CS31XX)\n11:00 AM TO 11:55 AM - OOPS(CS3102)\n12:00 PM TO 12:55 PM - SOFT SKILLS(HS3101)\n02:00 PM TO 02:55 PM - POM(BM002)"
            return result
        elif day=='tuesday':
            result = "09:00 AM TO 09:55 AM - AI(CS31XX)\n10:00 AM TO 10:55 AM - SS(EC3106)\n11:00 AM TO 11:55 AM - OS(CS3101)\n12:00 PM TO 12:55 PM - SOFT SKILLS(HS3101)\n03:00 PM TO 03:55 PM - POM(BM002)"
            return result
        elif day=='wednesday':
            result= "09:00 AM TO 09:55 AM - OOPS(CS3102)\n10:00 AM TO 10:55 AM - OS(CS3101)\n11:00 AM TO 11:55 AM - FLAT(CS3103)\n12:00 PM TO 12:55 PM - SS(EC3106)\n12:00 PM TO 12:55 PM - OS LAB(CS3701)"
            return result
        elif day=='thursday':
            result = "10:00 AM TO 10:55 AM - AI(CS31XX)\n11:00 PM TO 11:55 PM - FLAT(CS3103)"
            return result
        elif day=='friday':
            result="09:00 AM TO 09:55 AM - FLAT(CS3103)\n10:00 AM TO 10:55 AM - OOPS(CS3102)\n11:00 AM TO 11:55 AM - SS(EC3106)\n12:00 PM TO 12:55 PM - POM(BM002)\n02:00 PM TO 05:55 PM - OOPS LAB(CS3702)"
            return result
        elif day=='saturday':
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result
        elif day=='sunday':
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result
        
    def switch_day_112(day):
        if day=='monday':
            result="09:00 AM TO 09:55 AM - SOFT SKILLS(HS3101)\n10:00 AM TO 10:55 AM - OS(CS3101)\n11:00 AM TO 11:55 AM - AI(CS31XX)\n12:00 PM TO 12:55 PM - FLAT(CS3103)\n02:00 PM TO 05:55 PM - OOPS LAB(CS3702)"
            return result
        elif day=='tuesday': 
            result = "09:00 AM TO 09:55 AM - POM(BM002)\n10:00 AM TO 10:55 AM - AI(CS31XX)\n11:00 AM TO 11:55 AM - OOPS(CS3102)\n02:00 PM TO 05:55 PM - OS LAB(BS2201)"
            return result
        elif day=='wednesday':
            result="09:00 AM TO 09:55 AM - AI(CS31XX)\n10:00 AM TO 10:55 AM - OOPS(CS3102)\n11:00 AM TO 11:55 AM - OS(CS3101)\n12:00 PM TO 12:55 PM - FLAT(CS3013)"
            return result
        elif day=='thursday':
            result ="09:00 AM TO 09:55 AM - FLAT(CS3103)<br>10:00 AM TO 10:55 AM - OOPS(CS3102)\n11:00 AM TO 11:55 AM - SS(EC3106)"
            return result
        elif day=='friday':
            result = "09:00 AM TO 09:55 AM - SS(EC3106)\n10:00 AM TO 10:55 AM - OS(CS3101)\n11:00 AM TO 11:55 AM - SOFT SKILLS(HS3101)\n12:00 PM TO 12:55 PM - POM(BM002)"
            return result
        elif day=='saturday':
            result="09:00 AM TO 09:55 AM - SS(EC3106)\n10:00 AM TO 10:55 AM - POM(BM002)"
            return result
        elif day=='sunday':
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result


    def switch_day_113(day):
        if day=='monday': 
            result="09:00 AM TO 09:55 AM - OOPS(CS3102)\n10:00 AM TO 10:55 AM - OS(CS3101)\n11:00 AM TO 11:55 AM - SS(EC3106)\n12:00 PM TO 12:55 PM - POM(BM002)"
            return result
        elif day=='tuesday':
            result="09:00 AM TO 09:55 AM - FLAT(CS3103)\n10:00 AM TO 10:55 AM - OOPS(CS3102)\n11:00 AM TO 11:55 AM - OS(CS3101)\n12:00 PM TO 12:55 PM - AI(CS31XX)\n02:00 AM TO 05:55 PM - OOPS LAB(CS3702)"
            return result
        elif day=='wednesday':
            result="09:00 AM TO 09:55 AM - SOFT SKILLS(HS3101)\n10:00 AM TO 10:55 AM - OS(CS3101)\n11:00 AM TO 11:55 AM - OOPS(CS3102)\n12:00 PM TO 12:55 PM - FLAT(CS3104)"
            return result
        elif day=='thursday':
            result="09:00 AM TO 09:55 AM - FLAT(CS3103)\n10:00 AM TO 10:55 AM - SS(EC3106)\n12:00 PM TO 12:55 PM - AI(CS31XX)\n02:00 AM TO 05:55 PM - OS LAB(CS3702)"
            return result
        elif day=='friday':
            result="09:00 AM TO 09:55 AM - POM(BM002)\n10:00 AM TO 10:55 AM - SOFT SKILLS(HS3101)\n11:00 AM TO 11:55 AM - AI(CS31XX)"
            return result
        elif day=='saturday':
            result="09:00 AM TO 09:55 AM - POM(BM002)\n10:00 AM TO 10:55 AM - SS(EC3106)"
            return result
        elif day=='sunday':
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."
            return result
            
    def switch_day_012(day):
        if day=='monday':
            result="09:00 AM TO 09:55 AM - POM(BM002)\n10:00 AM TO 10:55 AM - OOPS(CS3102)\n11:00 AM TO 11:55 AM - OS(CS3101)\n12:00 PM TO 12:55 PM - AI(CS31XX)\n02:00 AM TO 05:55 PM - OS LAB(CS3701)"
            return result
        elif day=='tuesday':
            result="09:00 AM TO 09:55 AM - SOFT SKILLS(CS3103)\n10:00 AM TO 10:55 AM - FLAT(CS3103)\n11:00 AM TO 11:55 AM - OOPS(CS3102)\n12:00 PM TO 12:55 PM - OS(CS3101)\n02:00 AM TO 02:55 PM - SS(EC3101)"
            return result
        elif day=='wednesday':
            result="09:00 AM TO 09:55 AM - OS(CS3101)\n10:00 AM TO 10:55 AM - OOPS(CS3102)\n11:00 AM TO 11:55 AM - SS(EC3106)\n12:00 PM TO 12:55 PM - SOFT SKILLS(HS3101)\n02:00 AM TO 05:55 PM - OOPS LAB(CS3702)"
            return result
        elif day=='thursday':
            result="09:00 AM TO 09:55 AM - SS(EC3106)\n10:00 AM TO 10:55 AM -FLAT(CS3103)\n11:00 AM TO 11:55 AM - AI(CS31XX)\n12:00 PM TO 12:55 PM - POM(BM002)"
            return result
        elif day=='friday':
            result="10:00 AM TO 10:55 AM - POM(BM002)\n11:00 AM TO 11:55 AM - FLAT(CS3103)\n12:00 PM TO 12:55 PM - AI(CS31XX)"
            return result
        elif day=='saturday':
            result="Chill bro"
            return result
        elif day=='sunday':
            result="You don't have any classes today... Enjoy and Be productive in the weekend..."      
            return result

    def switch_cls(cls,day):
        if cls == "114":
            # day=input("Select Day: \n")
            return switch_day_114(day)
        elif cls == "103":
            # day=input("Select Day: \n")
            return switch_day_103(day)
        elif cls == "112":
            # day=input("Select Day: \n")
            return switch_day_112(day)
        elif cls == "113":
            # day=input("Select Day: \n")
            return switch_day_113(day)
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
