from flask import Flask, render_template

app = Flask(__name__)
import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname) 
class dataset:
	
	def __init__(self):
		self.cand1dat = 0
		self.cand2dat = 0
		self.cand3dat = 0
		self.cand4dat = 0
		self.cand5dat = 0
		self.cand6dat = 0
		self.cand7dat = 0
		self.cand8dat = 0
		self.cand9dat = 0
		self.cand10dat = 0
		self.cand11dat = 0
		self.cand12dat = 0
		
		self.cand1 = 0
		self.cand2 = 0
		self.cand3 = 0
		self.cand4 = 0
		self.cand5 = 0
		self.cand6 = 0
		self.cand7 = 0
		self.cand8 = 0
		self.cand9 = 0
		self.cand10 = 0
		self.cand11 = 0
		self.cand12 = 0
		
		self.data = [
		self.cand1,
		self.cand2,
		self.cand3,
		self.cand4,
		self.cand5,
		self.cand6,
		self.cand7,
		self.cand8,
		self.cand9,
		self.cand10,
		self.cand11,
		self.cand12]
		
		self.dat = (
		self.cand1dat,
		self.cand2dat,
		self.cand3dat,
		self.cand4dat,
		self.cand5dat,
		self.cand6dat,
		self.cand7dat,
		self.cand8dat,
		self.cand9dat,
		self.cand10dat,
		self.cand11dat,
		self.cand12dat)
		
	def putinfile(self, value, name):
		f = open("{}.txt".format(name), 'w')
		f.write(str(value))
		f.close()
	
	def readfromfile(self, name):
		f = open("{}.txt".format(name), 'r')
		x = f.read()
		f.close()
		return int(x)
	
	def registervalues(self, dat):
		for x in range(0, 12):
			y = self.readfromfile("cand{}".format(str(x+1)))
			self.putinfile(dat[x]+y, "cand{}".format(str(x+1)))
			
		print("Values registered succesfully")


def set_results(dat):

	a = dataset()
	dat = dat.replace(",", "")
	dat = dat.replace(" ", "")
	dat = str(dat)
	print(dat)
	a.cand1 = dat[0:2+1]
	a.cand2 = dat[3:5+1]
	a.cand3 = dat[6:8+1]
	a.cand4 = dat[9:11+1]
	a.cand5 = dat[12:14+1]
	a.cand6 = dat[15:17+1]
	a.cand7 = dat[18:20+1]
	a.cand8 = dat[21:23+1]
	a.cand9 = dat[24:26+1]
	a.cand10 = dat[27:29+1]
	a.cand11 = dat[30:32+1]
	a.cand12 = dat[33:35+1]
	
	a.cand1dat += int(a.cand1)
	a.cand2dat += int(a.cand2)
	a.cand3dat += int(a.cand3)
	a.cand4dat += int(a.cand4)
	a.cand5dat += int(a.cand5)
	a.cand6dat += int(a.cand6)
	a.cand7dat += int(a.cand7)
	a.cand8dat += int(a.cand8)
	a.cand9dat += int(a.cand9)
	a.cand10dat += int(a.cand10)
	a.cand11dat += int(a.cand11)
	a.cand12dat += int(a.cand12)
	

	dat = (
		a.cand1dat,
		a.cand2dat,
		a.cand3dat,
		a.cand4dat,
		a.cand5dat,
		a.cand6dat,
		a.cand7dat,
		a.cand8dat,
		a.cand9dat,
		a.cand10dat,
		a.cand11dat,
		a.cand12dat)
	print(a.data)
	print(dat)
	a.registervalues(dat)
	
	

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/submit/<values>')
def submit(values):
	set_results(values)
	return "submitted succesfully"
	
	
def returnval(name):
	a = open(name, 'r')
	x = a.read()
	a.close()
	return x

@app.route('/show')
def show():
	playerscores = []
	for x in range(1, 13):
		naam = "cand{}.txt".format(str(x))
		vall = returnval(naam)
		playerscores.append(vall)

	candlist = []
	file = open("candidatelist.txt", 'r')
	data = file.read()
	file.close()
	data = data.split(",")
	for x in data: candlist.append(x)


	lol = """<!DOCTYPE html><html><head><title>Results</title><style type="text/css">table{{border: 0px solid black; background-color: black;}}td{{width: 100px;text-align: center;}}table tr:nth-child(even){{background-color: #eee;}}table tr:nth-child(odd){{background-color: #ddd;}}table th {{color: white;background-color: black;}}
	</style></head>
<body>
	<table style="border: 1px solid black; table-layout: auto;padding: 2px;">
		<tr>
			<td style = "font-size: 20px; color: red">Candidate</td>
			<td style = "font-size: 20px; color: red">Score</td>
		</tr>
		<tr>
			<td>{cand1}</td>
			<td>{score1}</td>
		</tr>
		<tr>
			<td>{cand2}</td>
			<td>{score2}</td>
		</tr>
		<tr>
			<td>{cand3}</td>
			<td>{score3}</td>
		</tr>
		<tr>
			<td>{cand4}</td>
			<td>{score4}</td>
		</tr>


		<tr>
			<td>{cand5}</td>
			<td>{score5}</td>
		</tr>
		<tr>
			<td>{cand6}</td>
			<td>{score6}</td>
		</tr>
		<tr>
			<td>{cand7}</td>
			<td>{score7}</td>
		</tr>
		<tr>
			<td>{cand8}</td>
			<td>{score8}</td>
		</tr>



		<tr>
			<td>{cand9}</td>
			<td>{score9}</td>
		</tr>
		<tr>
			<td>{cand10}</td>
			<td>{score10}</td>
		</tr>
		<tr>
			<td>{cand11}</td>
			<td>{score11}</td>
		</tr>
		<tr>
			<td>{cand12}</td>
			<td>{score12}</td>
		</tr></table></body></html>""".format(cand1 = candlist[0],
                                                      score1 = playerscores[0],

                                                      cand2 = candlist[1],
                                                      score2 = playerscores[1],

                                                      cand3 = candlist[2],
                                                      score3 = playerscores[2],

                                                      cand4 = candlist[3],
                                                      score4 = playerscores[3],

                                                      cand5 = candlist[4],
                                                      score5 = playerscores[4],

                                                      cand6 = candlist[5],
                                                      score6 = playerscores[5],

                                                      cand7 = candlist[6],
                                                      score7 = playerscores[6],

                                                      cand8 = candlist[7],
                                                      score8 = playerscores[7],

                                                      cand9 = candlist[8],
                                                      score9 = playerscores[8],

                                                      cand10 = candlist[9],
                                                      score10 = playerscores[9],

                                                      cand11 = candlist[10],
                                                      score11 = playerscores[10],

                                                      cand12 = candlist[11],
                                                      score12 = playerscores[11],

                                                      )
	return lol
	
	

if __name__ == '__main__':
    app.run(debug = True, host = str(IPAddr), port = 80)
    del socket
