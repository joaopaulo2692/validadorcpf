from flask import Flask, render_template, request




app = Flask(__name__)

app.config['SECRET_KEY'] = '123456'


@app.route("/",methods=['GET','POST'])
def site():
    return render_template('home.html')

@app.route('/resultado', methods=['POST'])
def resultados():
    resultado = request.form.to_dict().values()
    #resultado = request.form.values()
    cpf = []
    for i in resultado:
        cpf.append(i)
    print(cpf)


    count = 10
    count2 = 11
    val1 = 0
    val2 = 0
    val3 = 0
    val4 = 0
    chars = '.,-'
    resposta = 1

    cpf[0] = cpf[0].translate(str.maketrans('', '', chars))

    print(cpf[0])

    while len(cpf[0]) == 11:
        for i in range(9):
            val1 += int(cpf[0][i]) * count
            count -= 1
        val2 = (val1 * 10) % 11

        for i in range(10):
            val3 += int(cpf[0][i]) * count2
            count2 -= 1
        val4 = (val3 * 10) % 11

        if val4 != int(cpf[0][10]) or val2 != int(cpf[0][9]) or len(set(cpf[0])) == 1:
            resposta = 0
            print('CPF inválido')
            break

        print('CPF válido')
        break
    else:
        resposta = 0
    print(resposta)
    return render_template('resultado.html', resposta=resposta)






app.run(debug=True)
