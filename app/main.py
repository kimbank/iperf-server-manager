from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

aback = "<br/><a href='/'>Back</a>"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_iperf():
    try:
        subprocess.Popen(['iperf3', '-s'])
        return "iperf3 server started!" + aback
    except Exception as e:
        return f"Failed to start server: {str(e)}" + aback

@app.route('/stop', methods=['POST'])
def stop_iperf():
    try:
        subprocess.run(['pkill', 'iperf3'])
        return "iperf3 server stopped!" + aback
    except Exception as e:
        return f"Failed to stop server: {str(e)}" + aback

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
