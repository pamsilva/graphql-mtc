from flask import Flask
from flask_graphql import GraphQLView

from model import session
from schema import schema

app = Flask(__name__)
app.debug = True


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True,  # For having the GraphiQL interface
        context={'session': session}
    )
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()
    print 'POTATO'


if __name__ == '__main__':
    print 'Hello World'
    app.run()
