import os.path
from quart import Quart, render_template, abort, send_file, request
import config
import utils

app = Quart(__name__)


@app.route('/', methods=['GET', 'POST'])
async def home_page():
    return await list_file_path()


@app.route('/<path:file_path>', methods=['GET', 'POST'])
async def list_file_path(file_path: str | None = None):
    full_path = config.full_path_share if file_path is None else os.path.join(config.full_path_share, file_path)
    if not os.path.exists(os.path.join('root', full_path)):
        return abort(404)
    if os.path.isfile(full_path):
        return await send_file(full_path, conditional=True)
    else:
        short_name = '/' if file_path is None else os.path.basename(file_path)
        path_name = '/' if file_path is None else file_path
        files = []
        for file_name in os.listdir(full_path):
            full_file_path = os.path.join(full_path, file_name)
            files.append({
                'name': file_name,
                'isfile': os.path.isfile(full_file_path),
                'date': utils.format_time(os.path.getmtime(full_file_path)),
                'size': utils.format_size(os.path.getsize(full_file_path)),
            })
        return await render_template('list-dir.html', path_name=path_name, short_name=short_name, files=files)


if __name__ == '__main__':
    app.run('0.0.0.0', 8000, debug=True)
