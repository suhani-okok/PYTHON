import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import colorama
import csv
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

df = pd.read_csv('DailyDelhiClimateTest.csv')
df['date'] = pd.to_datetime(df['date'])

file_path = "DailyDelhiClimateTest.csv"




## LINE PLOTS    


def plot_temperature():
    plt.figure()
    plt.plot(df['date'], df['meantemp'], c = 'green')
    plt.xlabel('DATE')
    plt.ylabel("MEAN TEMPERATURE")
    plt.title("TEMP vs DATE")
    cursor= mplcursors.cursor(hover = True)
    plt.show()


def plot_humidity():
    plt.figure()
    plt.plot(df['date'], df['humidity'], c = 'red')
    plt.xlabel('date')
    plt.ylabel("humidity")
    plt.title("humidity to date variation")
    cursor= mplcursors.cursor(hover = True)
    plt.show()
    

def plot_windspeed():
    plt.figure()
    plt.plot(df['date'], df['wind_speed'], c = 'yellow')
    plt.xlabel('date')
    plt.ylabel("wind_speed")
    plt.title("windspeed to date variation")
    cursor= mplcursors.cursor(hover = True)
    plt.show()


def plot_meanpressure():
    plt.figure()
    plt.plot(df['date'], df['meanpressure'], c = 'blue')
    plt.xlabel('date')
    plt.ylabel("meanpressure")
    plt.title("mean pressure to date variation")
    cursor= mplcursors.cursor(hover = True)
    plt.show()



##HISTOGRAMS

    
def hist_meantemp():
    df['month'] = df['date'].dt.month
    plt.figure(figsize=(10, 6))
    for month in range(1, 13):
        plt.hist(df[df['month'] == month]['meantemp'], bins=20, alpha=0.5, label=f'Month {month}')

    plt.xlabel('Mean Temperature')
    plt.ylabel('Frequency')
    plt.title('Temperature Distribution by Month')
    plt.legend()
    plt.show()


def hist_humidity():
    df['month'] = df['date'].dt.month
    plt.figure(figsize=(10, 6))
    plt.hist(df['humidity'], bins=30, alpha=0.7)

    plt.xlabel('Humidity')
    plt.ylabel('Frequency')
    plt.title('Humidity Distribution Over Time')
    plt.show()


def hist_meanpressure():
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year

    plt.figure(figsize=(10, 6))
    for year in df['year'].unique():
        plt.hist(df[df['year'] == year]['meanpressure'], bins=20, alpha=0.5, label=f'Year {year}')

    plt.xlabel('Mean Pressure')
    plt.ylabel('Frequency')
    plt.title('Mean Pressure Distribution by Year')
    plt.legend()
    plt.show()




#queries section


def extreme_weather():
    meantemp_threshold = 30
    windspeed_threshold = 5
    extreme_meantemp_events = df[df['meantemp'] > meantemp_threshold]
    extreme_windspeed_events = df[df['wind_speed'] > windspeed_threshold]
    print('EXTREME TEMPREATURE EVENTS')
    print(extreme_meantemp_events)
    print('EXTRENME WINDSPEED EVENTS')
    print(extreme_windspeed_events)


def rain():
    print("Note: It is significantly noticed that higher humidity often leads to higher chances of rain.")
    df['month'] = df['date'].dt.month.round().fillna(0).astype(int)
    high_humidity_months = df.loc[df['humidity'].gt(70),'month'].unique()
    high_humidity_entries = df[df['humidity'].gt(70)]
    
    print("here is the list of data where there was likely a rainy month")
    print(high_humidity_entries[['date', 'humidity']])

def windiest_month():
    df['month'] = df['date'].dt.month.round().fillna(0).astype(int)
    windiest_months = df.loc[df['wind_speed'].gt(9),'month'].unique()
    windy_entries = df[df['wind_speed'].gt(9)]
    print("here is the list of data where there was likely a windy month")
    print(windy_entries[['date', 'humidity']])


def drought_months():
    drought_months = df[(df['humidity'] < 30) & (df['meantemp'] > 35)]


    if not drought_months.empty:
        print("List of months indicating potential drought (Low Humidity & High Temperature):")
        print(drought_months[['date', 'humidity', 'meantemp']])
    else:
        print("No months found indicating potential drought.")


def statistics_temp():
    mean_temp_mean = df['meantemp'].mean()
    mean_temp_median = df['meantemp'].median()
    mean_temp_max = df['meantemp'].max()
    mean_temp_min = df['meantemp'].min()

    print(f"Mean Temperature - Mean: {mean_temp_mean}, Median: {mean_temp_median}, Max: {mean_temp_max}, Min: {mean_temp_min}")


def statistics_humidity():
    humidity_mean = df['humidity'].mean()
    humidity_median = df['humidity'].median()
    humidity_max = df['humidity'].max()
    humidity_min = df['humidity'].min()

    print(f"Mean humidity - Mean: {humidity_mean}, Median: {humidity_median}, Max: {humidity_max}, Min: {humidity_min}")

def statistics_windspeed():
    mean_wind_speed = df['wind_speed'].mean()
    median_wind_speed = df['wind_speed'].median()
    max_wind_speed = df['wind_speed'].max()
    min_wind_speed = df['wind_speed'].min()

    print(f"Mean Temperature - Mean: {mean_wind_speed}, Median: {median_wind_speed}, Max: {max_wind_speed}, Min: {min_wind_speed}")

def statistics_meanpressure():
    mean_meanpressure = df['meanpressure'].mean()
    median_meanpressure = df['meanpressure'].median()
    max_meanpressure = df['meanpressure'].max()
    min_meanpressure = df['meanpressure'].min()

    print(f"Mean Temperature - Mean: {mean_meanpressure}, Median: {median_meanpressure}, Max: {max_meanpressure}, Min: {min_meanpressure}")


def queries():
    print("PLEASE ENTER YOUR CHOICE CAREFULLY")
    while True:
        print("-----------------------------------------------------------------------------")
        print()
        print("PRESS ONE FOR VIEWING THE EXTREME WEATHER CONDITION MONTH IN THE YEARS OF DATA")
        print()
        print("PRESS TWO FOR VIEWING THOSE MONTHS WEHRE THE CHANCES OF PRECIPITATION WERE SIGNIFICANTLY HIGHER THAN OTHERS")
        print()
        print("PRESS THREE FOR VIEWING THE WINDIEST MONTHS IN THE YEARS OF DATA")
        print()
        print("PRESS FOUR FOR VIEWING THE MONTHS SHOWING THE SIGNS OF DROUGHT YEARS OF DATA")
        print()
        print("PRESS FIVE FOR VIEWING THE STATICS OF TEMPERATURE IN MONTHS IN THE YEARS OF DATA")
        print()
        print("PRESS SIX FOR VIEWING THE STATICS OF HUMIDITY IN MONTHS IN THE YEARS OF DATA")
        print()
        print("PRESS SEVEN FOR VIEWING THE STATICS OF MEAN PRESSURE IN MONTHS IN THE YEARS OF DATA")
        print()
        print("-----------------------------------------------------------------------------")

        query_choice= int(input("PLEASE ENTER YOUR CHOICE:"))
        if query_choice == 1:
            extreme_weather()

        elif query_choice == 2:
            rain()

        elif query_choice == 3:
            windiest_month()

        elif query_choice == 4:
            drought_months()

        elif query_choice == 5:
            statistics_temp()

        elif query_choice == 6:
            statistics_humidity()

        elif query_choice == 7:
            statistics_meanpressure()

        else:
            print("YOU ENTERED WRONG CHOICE. EXITING PROGRAM")
            exit()

            
            
def gui():
    root = tk.Tk()
    root.title("CLIMATE ANALYSIS")

    background_image = Image.open(r"C:\Users\suhan\OneDrive\Desktop\23913.jpg")
    background_photo = ImageTk.PhotoImage(background_image)

    image_width, image_height = background_image.size

    background_label = tk.Label(root, image = background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)            
            

#clickable button

    button = tk.Button(root, text="TO VIEW THE MEAN TEMPERATURE AND DATE ANALYSIS", command = plot_temperature, bg="#4CAF50", fg="white", font=("Arial", 14))
    button.place(x=100, y=100)

    button = tk.Button(root, text="VIEW THE HUMIDITY AND DATE ANALYSIS", command = plot_humidity, bg="#4CAF50", fg="white", font=("Arial", 14))
    button.place(x=100, y=180)

    button = tk.Button(root, text="VIEW THE WIND SPEED AND DATE ANALYSIS", command = plot_windspeed, bg="#4CAF50", fg="white", font=("Arial", 14))
    button.place(x=100, y=260)


    button = tk.Button(root, text="VIEW THE MEAN PRESSURE AND DATE ANALYSIS", command = plot_meanpressure, bg="#4CAF50", fg="white", font=("Arial", 14))
    button.place(x=100, y=340)


    root.mainloop()

while True:
    print("****************************************************************************")
    print("****************************************************************************")
    print("**                 WELCOME TO OUR CLIMATE ANALYSIS PROJECT                **")
    print("**                                                                        **")
    print("**                                                                        **") 
    print("**                   ENTER YOU CHOICE ACCORDINGLY:                        **")
    print("**                                                                        **")
    print("**                                                                        **")
    print("**    PRESS ONE FOR VIEWING THE DATAS ON LINE PLOT (MATPLOTLIB IN PROJECT)**")
    print("**                                                                        **")
    print("**    PRESS TWO FOR ENTERING THE QUERIES SECTION (PANDAS IN PROJECT)      **")
    print("**                                                                        **")
    print("**                                                                        **")
    print("****************************************************************************")
    print("****************************************************************************")
    
    choice= int(input("PLEASE ENTER YOUR CHOICE CAREFULLY:"))
    

    if choice == 1:
        gui()

    elif choice == 2:
        queries()

    else:
        exit()

                

