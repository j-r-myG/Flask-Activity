from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    words:list[str] = [
            request.form.get('txt1'),
            request.form.get('txt2'),
            request.form.get('txt3'),
            request.form.get('txt4'),
            request.form.get('txt5')
    ]

    if request.method == 'GET':
        return render_template('index.html')
    else:
        words_str = ','.join(words) # convert to string
        return redirect(url_for('display_words', words = words_str))


@app.route("/display-words/<words>")
def display_words(words:str):
    words_list:list[str] = words.split(',')
    missing_index:list = [i for i, j in enumerate(words_list) if not j]

    if missing_index:
        missing_index_str = ','.join(map(str, missing_index)) # convert to string
        return redirect(url_for('display_error', missing_index = missing_index_str))
    else:
        return render_template('display-words.html', words = words_list)


@app.route("/display-error/<missing_index>")
def display_error(missing_index:str):
    if missing_index: 
        missing_index_list = list(map(int, missing_index.split(',')))  
        return render_template('display-error.html', indexes = missing_index_list)
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(host='127.0.0.1',port='5000',debug=True)