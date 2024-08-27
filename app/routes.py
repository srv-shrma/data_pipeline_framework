from . import app

@app.route('/test', methods=['GET'])
def test_route():
    return "Test route is working!"
