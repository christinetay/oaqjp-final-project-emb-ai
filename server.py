''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/")
def render_index_page():
    ''' Render index page
    '''
    return render_template('index.html')


@app.route("/emotionDetector")
def sent_analyzer():
    ''' The function for emotion detector
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    system_response_text = ""

    if response['dominant_emotion'] is None:
        system_response_text = "Invalid text! Please try again!."
        return system_response_text

    system_response_text = "For the given statement, the system response is "
    system_response_text += "'anger' : "+ str(response['anger']) +", "
    system_response_text += "'disgust':  "+ str(response['disgust']) +", "
    system_response_text += "'fear': "+ str(response['fear']) +", "
    system_response_text += "'joy': "+ str(response['joy']) + " and "
    system_response_text += "'sadness': "+ str(response['sadness']) + "."
    system_response_text += "The dominant emotion is "+ response['dominant_emotion'] + "."

    return system_response_text


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
