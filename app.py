from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    barramento_a_var = 'R0'
    barramento_b_var = 'R0'
    barramento_c_var = 'R0'

    if request.method == 'POST':
        barramento_a_var = request.form['barramento_a']
        barramento_b_var = request.form['barramento_b']
        barramento_c_var = request.form['barramento_c']
        valor = request.form['valor_input']
        update_interface(valor)

    return render_template('index.html', 
                           barramento_a_var=barramento_a_var,
                           barramento_b_var=barramento_b_var,
                           barramento_c_var=barramento_c_var)

if __name__ == '__main__':
    app.run(debug=True)
