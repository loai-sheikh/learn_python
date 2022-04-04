#pip install speedtest-cli
#pip install git+https://github.com/sivel/speedtest-cli.git
import speedtest

st = speedtest.Speedtest()
#Bytpes for conversion
bytes_num = 1000000

#Get download speed
dws = round(st.download()/bytes_num, 2)

#Get upload speed
ups = round(st.upload()/bytes_num, 2)

#Print internet speed
print(f'My download speed is: {dws} Mbps')
print(f'My upload speed is: {ups} Mbps')