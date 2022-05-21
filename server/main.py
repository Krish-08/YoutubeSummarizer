

from flask import render_template, request ,Flask
import getTranscript as getTranscript



app=Flask(__name__)

@app.route("/")

def main():
    return render_template("getLink.html")



@app.route('/api/summarize', methods=['GET'])
def getSummary():
    link = request.args.get("youtube_url"," ")
    obj=getTranscript.gettranscript()
    print(link)
    Transcript=obj.transcript(link)
    return Transcript


if(__name__=="__main__"):
    app.run(debug=True)
    