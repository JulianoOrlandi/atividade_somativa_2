from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    ano = request.args.get("ano", "")
    if ano:
        resposta = is_leap(ano)
    else:
        resposta = ""

    return (
        	"""<h2> Você sabia que nem todos os anos bissextos ocorrem no intervalo de 4 em 4 anos? </h2>"""
		"""<br>"""
		"""<form action="" method="get">
                <input type="text" name="ano">
                <input type="submit" value="Convert">
            </form>"""
        + "É bissexto? "
        + '<a id="resposta">' +resposta+ '</a>'

    )
 
@app.route("/<int:ano>")
def is_leap(ano):
    year = int(ano)
    resposta = ""
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                resposta = 'Sim!'
            else:
                resposta = 'Não!'
        else:
            resposta = 'Sim!'
    else:
        resposta = 'Não!'
    return resposta

@app.route("/<string:script>")
def run(script):
    script=request.args.get("script", "")
    return (
	"""<h2> RUN! 🕸 </h2>"""
	"""<form action="" method="get">
                <input type="text" name="script">
                <input type="submit" value="Run">
            </form>"""
    + '<a id="script">' + script + '</a>'
) 


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
     #app.run(host="0.0.0.0", port=8080, debug=False)
