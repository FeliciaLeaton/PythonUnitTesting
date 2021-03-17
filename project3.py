import pygal
import lxml
import requests
import time

api_key = "65210ZZ38CVFIWM4"
#api docs https://www.alphavantage.co/documentation/
def getData(time_series, symbol, api_key):
    #Daily Time Series API Func
    #https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
    #TIME_SERIES = TIME_SERIES_DAILY
    #symbol = symbol 
    #apikey = api_key

    #Intraday Time Series API Func
    #https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
    #time_series = TIME_SERIES_INTRADAY
    #symbol = symbol
    #apikey = api_key
    #interval = interaval? api required interval 

    #Weekly Time Series API Func
    #https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo
    #time_series = TIME_SERIES_WEEKLY
    #symbol = symbol 
    #apikey = api_key 

    #Monthly Time Series API Func
    #https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo
    #time_series = TIME_SERIES_MONTHLY
    #symbol = symbol
    #apikey = api_key
    #create string
    
    ##STRING ADDITION NOT WORKING, probably doing it wrong 
    apistring = "https://www.alphavatage.co/query?function="
    if (time_series == 1):
        time_series = "TIME_SERIES_INTRADAY"
    elif (time_series == 2):
        time_series = "TIME_SERIES_DAILY"
    elif (time_series == 3):
        time_series = "TIME_SERIES_WEEKLY"
    elif (time_series == 4):
        time_series = "TIME_SERIES_MONTHLY"

    apistring += (time_series + "&symbol=" + symbol)
    if (time_series == "TIME_SERIES_INTRADAY"):
        apistring += "&interval=30min"
    apistring +="&apikey=" + api_key
    
    apistring = "https://www.alphavatage.co/query?function="
    print(apistring)

print("Stock Data Visualizer\n======================")

symbol = input("\nEnter the stock symbol are looking for: ")
#check and see if symbol exist > error handling
#probably just hit the api with a constant time_series value and input the requested symbol
#see if we get a good respone



print("\nChart Types\n==================\n1. Bar\n2. Line")
chart_type = input("Enter the chart type you want (1 , 2): ")
# make sure it's 1 or 2, while loop > error handling
while (chart_type != "1" and chart_type != "2"):
    print("Enter a 1 or 2 for the chart type")
    chart_type = input("Enter the chart type you want (1 , 2): ")

if (chart_type == "1"):
    #implement function to get bar chart > API integration
    print("1")
if (chart_type == "2"):
    #implement function to get line chart > API inegration
    print("2")




print("\nSelect the Time Series of chart you want to Generate\n=================================================================")
print("\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
time_series = input("Enter the time series option (1, 2, 3, 4): ")
# error check option picked > error handling
while time_series not in ('1','2','3','4'):
    print("Enter a 1, 2, 3, or 4 for the time series option")
    time_series = input("Enter the time series option (1, 2, 3, 4): ")

if (time_series == '1'):
    #implement function to get bar chart > API integration
    print("1")
if (time_series == '2'):
    #implement function to get line chart > API inegration
    print("2")
if (time_series == '3'):
    #implement function to get bar chart > API integration
    print("3")
if (time_series == '4'):
    #implement function to get line chart > API inegration
    print("4")





# start_date = input("Enter the start Date (YYYY-MM-DD):")
# error handling > check valid date in YYYY-MM-DD


valid = False
while not valid:
    start_date = input("Enter the start Date (YYYY-MM-DD): ")
    try:
        time.strptime(start_date, "%Y-%m-%d")
        valid = True
        break
    except ValueError:
        print("Enter a valid start date")
        valid = False

print(start_date)

# end_date = input("Enter the end Date (YYYY-MM-DD):")
# error hadling > check valid date in YYYY-MM-DD and that it is after the start date

valid = False
while not valid:
    end_date = input("Enter the end Date (YYYY-MM-DD): ")
    try:
        time.strptime(end_date, "%Y-%m-%d")
        if time.strptime(end_date, "%Y-%m-%d") > time.strptime(start_date, "%Y-%m-%d"):
            valid = True
        else:
            print("End date must be later than start date.")
            valid = False
    except ValueError:
        print("Enter a valid end date")
        valid = False

print(end_date)


getData(time_series,symbol,api_key)



#parse out json data that comes back from API

#use that data to create graph data 
#create lmxl file with graph data

#send lxml to http and open file



#after everything is pretty much toss it all in a while loop so user can re run a visualizaiton