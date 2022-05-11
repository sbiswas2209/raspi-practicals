from bottle import route, run, template
tem=input("Enter temparature value: ")
@route('/')
def getsens():
    sensor_log = [ {'sensor': 'temp', 'value': tem},
        {'sensor': 'humitity', 'value': 20},
        {'sensor': 'windspeed', 'value': 90},
        {'sensor': 'rain', 'price':0} ]
    return dict(data=sensor_log)
    # return template('<b>Hello, the temperature today is {{tem}}!, Humidity is 20, Windspeed is 90, and Rain is 0</b>', tem=tem)
run(host='localhost', port=7000, debug=True)
