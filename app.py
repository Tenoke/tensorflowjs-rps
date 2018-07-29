from flask import Flask, render_template, request, Response


app = Flask(__name__)


@app.route('/rps')
def rps():
    return render_template('rps.html')


@app.route('/save', methods=['POST'])
def save():
    """
    Optional endpoint for saving user games
    """
    data = request.get_data().decode("utf-8")
    with open("collected-data-others.txt", "a") as file:
        file.write(data + '\n')
    return Response(status=200)


if __name__ == '__main__':
    app.run()
