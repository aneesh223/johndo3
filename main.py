from flask import Flask, redirect, url_for, render_template
app = Flask('app')

# me websit!!

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')

@app.route('/contact')
def contsct():
  return render_template('contact.html')

@app.route('/github')
def github():
  return redirect('https://github.com/johndoe434')

@app.route('/youtube')
def youtube():
  return redirect('https://www.youtube.com/channel/UC6vusNTseRpomq7ruox9_0g')

@app.route('/discord')
def discord():
  return redirect('https://discord.gg/6GPjN8C')

app.run(host='0.0.0.0', port=8080)