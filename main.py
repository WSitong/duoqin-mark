from quart import Quart, render_template

app = Quart(__name__)


@app.route('/', methods=['GET'])
async def home_page():
    return await render_template('home.html')


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, True)
