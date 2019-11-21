from flask import Flask, jsonify
import requests


app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Invalid Request'}), 404


@app.route('/contributor/<string:owner>/<string:repo>')
def top_contributor(owner, repo):
    '''
    Lists the top 5 contributors of a repository

    :param owner name
    :param repository name
    '''
    req_top_contributor = requests.get(
        'https://api.github.com/repos/' + owner + '/' + repo + '/contributors')

    top_c = req_top_contributor.json()
    top_c = top_c[:5]

    for user in top_c:
        name = user['login']
        number_of_contrib = user['contributions']
        url = 'https://github.com/'+name
        user.clear()
        user['login'] = name
        user['contributions'] = number_of_contrib
        user['url'] = url
    return jsonify(top_c)


if __name__ == "__main__":
    app.run(debug="true", host='0.0.0.0', threaded="true")
