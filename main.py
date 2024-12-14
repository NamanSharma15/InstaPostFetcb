from post.get_post import InstagramPost
from flask import Flask,request
app = Flask(__name__)
@app.route("/getPost",methods=["POST"])
def getPost():
    body= request.get_json()
    print() 
    url:str = body["url"]
    post:InstagramPost = InstagramPost(url)
    return post.getData()
if __name__ == "__main__":
    app.run(port=5000)