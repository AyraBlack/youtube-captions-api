from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/captions', methods=['GET'])
def get_captions():
    video_id = request.args.get('videoId')
    if not video_id:
        return jsonify({"error": "Missing videoId"}), 400
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        combined = " ".join([entry['text'] for entry in transcript])
        return jsonify({ "videoId": video_id, "captions": combined })
    except Exception as e:
        return jsonify({ "error": str(e) }), 400

if __name__ == '__main__':
    app.run()
