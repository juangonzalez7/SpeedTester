import speedtest  # pip install speedtest-cli
from time import sleep
from tqdm import tqdm   # pip install tqdm
from colorama import Fore, init

init(autoreset=True)

print(Fore.MAGENTA + "GETTING BEST AVAILABLE SERVERS, UPLOADING & DOWNLOADING SPEED.....")

# initializing the SpeedTest instance
st = speedtest.Speedtest()

st.get_best_server()  # Most optimal server available
for i in tqdm(range(10), colour="white", desc="Finding Optimal Server"):
    sleep(0.05)

st.download()  # Downloading speed
for i in tqdm(range(10), colour="green", desc="Getting Download Speed"):
    sleep(0.05)

st.upload()  # Uploading Speed
for i in tqdm(range(10), colour="cyan", desc="Getting Upload Speed"):
    sleep(0.05)

# Put all elements in a dictionary
res_dict = st.results.dict()

# Create variables with an specific format
dwnl = str(res_dict['download'])[:2] + "." + \
    str(res_dict['download'])[2:4]

upl = str(res_dict['upload'])[:2] + "." + str(res_dict['upload'])[2:4]

# Display results in a table using colorama 
print("")

print(Fore.MAGENTA + "="*80)
print(Fore.LIGHTMAGENTA_EX + "SPEED TEST RESULTS:".center(80))
print(Fore.MAGENTA + "="*80)
print(Fore.LIGHTRED_EX +
      f"Download: {dwnl}mbps({float(dwnl)*0.125:.2f}MBs) | Upload: {upl}mbps ({float(upl)*0.125:.2f}MBs) | Ping: {res_dict['ping']:.2f}ms".center(80))
print(Fore.YELLOW + "-"*80)
print(Fore.LIGHTYELLOW_EX +
      f"HOST: {res_dict['server']['host']} | SPONSOR: {res_dict['server']['sponsor']} | LATENCY: {res_dict['server']['latency']:.2f}".center(80))
print(Fore.YELLOW + "-"*80)