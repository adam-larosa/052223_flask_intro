
from flask import Flask, make_response, request

app = Flask( __name__ ) 



@app.route( '/cats', methods = [ 'GET', 'POST' ] )
def cats():
    if request.method == 'GET':
        #
        # !!!!!!!!!!!!!!!!!!!!!!!!
        #
        return make_response( 'this could be all the cats!', 200 )

    if request.method == 'POST':
        data = request.get_json()
        return make_response( str( f'the body was: {data}' ), 201 )


@app.route( '/cats/<id>', methods = [ 'GET', 'PATCH', 'DELETE' ] )
def cats_by_id( id ):
    return f'our route was /cats/{id}'






# If we want to start the application with "flask run" we need to first set
# two environment variables from the command line:
#
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
#
# after setting those two we can run "flask run" from the command line.

# if we don't use "flask run" we need to run python directly on the app.py file
# so the following line hits.
if __name__ == '__main__':
    app.run( port = 5555, debug = True )