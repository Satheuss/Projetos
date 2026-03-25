import speedtest as st

def Speed_Test():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("Download Speed in Mbps: ", down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload Speed un Mbps: ", up_speed)

    ping = test.results.ping
    print("Ping: ", ping)

    return ping

ping = Speed_Test()

if ping <= 25:
    print("Internet: Rápida")

else:
    print("Internet: Lenta")