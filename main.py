from bs4 import BeautifulSoup
import requests
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# from datetime import datetime


plt.style.use("seaborn")


def get_price():
    url = "https://www.cryptometer.io/data/binance/btc/usdt"
    HTML = requests.get(url)
    soup = BeautifulSoup(HTML.content, 'html.parser')

    bucket = soup.find("body").find(
        "div", attrs={"class": "app-content content wraper_margin"})
    bucket = bucket.find("div", attrs={
        "class": "content-wrapper"}).find("div", attrs={"class": "content-body"})
    bucket = bucket.find_all(
        "div", attrs={"class": "row justify-content-center"})[1]
    bucket = bucket.find("div", attrs={
        "class": "col-xl-12 col-lg-12 col-12"}).find("div", attrs={"class": "row"})
    bucket = bucket.find("div", attrs={
        "class": "col-xl-5 col-lg-6 col-12 mb-2"}).find("div", attrs={"class": "card h-100"})
    bucket = bucket.find("div", attrs={"class": "card-content"}
                         ).find("div", attrs={"class": "media align-items-stretch"})
    bucket = bucket.find(
        "div", attrs={"class": "p-1 bg-gradient-x-dark white media-body"})
    bucket = bucket.find_all("h5")[0].get_text()

    rate = float(bucket.replace(',', ''))

    return rate


def cli_display():
    perv_rate = 0
    print(" ________________________________________________")

    print("|\tTime-Stamp\t\tBTC-USDT-Rate\t |")
    print(" ________________________________________________")
    while(1):
        rate = get_price()

        if perv_rate != rate:
            time_stamp = time.strftime("%d/%m/%Y %H:%M:%S        ")
            print("| ", time_stamp, "\t  ", "$", rate, "\t |")

        perv_rate = rate
        time.sleep(3)


x = []
y1 = []


def animate(i):

    x.append(time.strftime("%d/%m/%Y\n%H:%M:%S"))
    price = get_price()
    y1.append(price)

    plt.cla()

    plt.plot(x, y1, label="Bitcoin price")

    plt.legend(loc="upper left")

    plt.title("Realtime Bitcoin Price Plot", fontdict={
              'fontsize': 40}, fontweight='bold')
    plt.xlabel("Timestamp", fontdict={'fontsize': 20})
    plt.ylabel("Price in $ (USD)", fontdict={'fontsize': 20})

    print(price)


ani = FuncAnimation(plt.gcf(), animate, interval=3000)


if __name__ == "__main__":
    plt.show()
