from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    p = request.args.get('params', 'none')

    with open('memo.txt', 'r') as f:
        memo = f.readlines()

        if p != 'none':
            memo.append(p)

    with open('memo.txt', 'w') as f:
        memo_str = ""
        for m in memo:
            memo_str += m + '\n'
        f.write(memo_str)

    return render_template('index.html', memo = memo_str)

if __name__ == '__main__':
    app.run()