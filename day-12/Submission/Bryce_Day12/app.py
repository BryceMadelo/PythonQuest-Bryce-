from flask import Flask, jsonify

app = Flask(__name__)

user_data = {
    "name": "Bryce",
    "course_and_section": "BSCOE 3-4",
    "favorite_programming language": "JavaScript",
    "aws_service": "Amazon s3"
}

@app.route('/api/data', methods=['GET'])
def get_user_data():
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(debug=True)