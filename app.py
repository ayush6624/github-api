from flask import Flask, jsonify
import requests
from flasgger import Swagger


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
Swagger(app)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Invalid Request'}), 404


@app.route('/popular')
def popular():
    '''
    Shows the Top 3 Starred Repository of the given Languages
    I've Taken Kotlin, Go & Ruby as languages here
    ---
    tags:
      - Popular Repositories
    responses:
      200: 
        description: Request Successfully Executed
      400:
        description: Backend Error 
      404:
        description: Not Found
    '''
    top_c = []
    language = ['kotlin', 'go', 'ruby']
    for lang in language:
        response = requests.get(
            'https://api.github.com/search/repositories',
            params={'q': 'language:' + lang, 'sort': 'stars', 'order': 'desc'},

        )
        repository = response.json()
        repository_list = repository['items']
        repository_list = repository_list[:3]

        for repo in repository_list:
            ok = {}
            ok['full_name'] = repo['full_name']
            ok['language'] = lang
            ok['stars'] = repo['stargazers_count']
            ok['url'] = 'https://github.com/'+repo['full_name']
            ok['desciption'] = repo['description']
            top_c.append(ok)
    return jsonify(top_c)


@app.route('/contributor/<string:owner>/<string:repo>')
def top_contributor(owner, repo):
    '''
    Lists the top 5 contributors of a repository
    ---
    tags:
      - Top Contributors
    parameters:
      - name: owner
        in: path
        type: string
        required: true
      - name: repo
        in: path
        type: string
        required: true
    responses:
      200: 
        description: Request Successfully Executed
      400:
        description: Backend Error 
      404:
        description: Not Found
    '''
    top_c = []
    req_top_contributor = requests.get(
        'https://api.github.com/repos/' + owner + '/' + repo + '/contributors')

    repositories = req_top_contributor.json()
    repositories = repositories[:5]

    for repo in repositories:
        ok = {}
        ok['login'] = repo['login']
        ok['contributions'] = repo['contributions']
        ok['url'] = 'https://github.com/'+repo['login']
        top_c.append(ok)
    return jsonify(top_c)


if __name__ == "__main__":
    app.run(debug="false", host='0.0.0.0', threaded="true")
