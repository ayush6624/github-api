from flask import Flask, jsonify
import requests
from flasgger import Swagger


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SWAGGER'] = {
    'title': 'Github API Wrapper'
}
Swagger(app)


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found'}), 404


@app.route('/popular')
def popular():
    '''
    Shows the Top 3 Starred Repository of the given Languages
    I've Taken Kotlin, Go & Ruby as languages here
    ---
    swagger: "2.0"
    tags:
      - Popular Repositories
    responses:
      200:
        description: Request Successfully Executed
      400:
        description: Invalid Request
      404:
        description: Not Found
    '''

    top_repo_list = []
    languages = ['kotlin', 'go', 'ruby']
    for language in languages:
        response = requests.get(
            'https://api.github.com/search/repositories',
            params={'q': 'language:' + language,
                    'sort': 'stars', 'order': 'desc'},
        )

        repositories = response.json()
        repositories = repositories['items']
        repositories = repositories[:3]

        keys = ['full_name', 'language',
                'stargazers_count', 'html_url', 'description']

        language_list = [dict((k, repo[k]) for k in keys)
                         for repo in repositories]
        top_repo_list.extend(language_list)
    return jsonify(top_repo_list)


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
        description: Invalid Request
      404:
        description: Not Found
    '''

    req_top_contributor = requests.get(
        'https://api.github.com/repos/' + owner + '/' + repo + '/contributors')

    # To avoid a situation wherein Github API does not deliver a correct \
    # response eg- owner= torvalds, repo= linux, or wrong info is entered

    if req_top_contributor.status_code != 200:
        return jsonify({'error': 'Invalid Request'}), 400

    repositories = req_top_contributor.json()
    repositories = repositories[:5]

    keys = ['login', 'contributions', 'html_url']
    top_repo_list = [dict((k, repo[k]) for k in keys) for repo in repositories]
    # make a list of dictionaries containing the key-value pairs required.

    return jsonify(top_repo_list)


if __name__ == "__main__":
    app.run(debug="false", host='0.0.0.0', threaded="true")
