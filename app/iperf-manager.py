import subprocess

def start_iperf_server():
    subprocess.Popen(['iperf3', '-s'])

def stop_iperf_server():
    subprocess.run(['pkill', 'iperf3'])
