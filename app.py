from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Contact us')
def contactus():
    return render_template('contactus.html')

@app.route('/About us')
def aboutus():
    return render_template('aboutus.html')

@app.route('/Bestapp')
def bestapp():
    return render_template('bestapp.html')

@app.route('/bestapp.html', methods=['POST', 'GET'])
def bestapp_page():
    if request.method == 'POST':
        # Process the form data from bestapp.html
        category = request.form.get('category')
        # You can process category data here and fetch features related to the category
        features = get_features_for_category(category)
        return render_template('bestapp.html', category=category, features=features)
    else:
        return redirect(url_for('bestapp'))
    
@app.route('/result', methods=['GET'])   
def result():
    category = request.args.get('category')
    feature = request.args.get('feature')

    # You can perform any processing or calculations here based on category and feature
    best_app = recommend_best_app(category, feature)

    return render_template('result.html', category=category, feature=feature, best_app=best_app)

def recommend_best_app(category, feature):
    # Replace this with your logic to recommend the best app
    # For example, you can use a database query or predefined logic
    # Dummy data for illustration purposes
    if category == 'Social':
        if feature == 'messaging':
            return 'WhatsApp'
        elif feature == 'Secure Messaging':
            return 'Telegram Desktop'
        elif feature == 'Social Photo Sharing':
            return 'Instagram'
        elif feature == 'Social Networking':
            return 'Facebook'
        elif feature == 'Visual Discovery and Inspiration':
            return 'Pinterest'
        elif feature == 'Instant Messaging':
            return 'Messenger'
        elif feature == 'Social News Aggregation and Discussion':
            return 'Reddit'
        elif feature == 'Unofficial Telegram Client':
            return 'Unigram - Telegram for Windows 10'
        elif feature == 'Desktop Version of imo for Video Calls and Chat':
            return 'imo desktop free video calls and chat'
        elif feature == 'Professional Networking Analytics':
            return 'lnkd.in'
        elif feature == 'Universal Cloud Dashboard':
            return 'Cloud Drive! : OneDrive, Dropbox, Google Drive and more'
        elif feature == 'Integrated website analytics and insights':
            return 'WordPress.com'
        elif feature == 'seamless integration with Windows notifications':
            return 'WeChat For Windows'
    elif category == 'Entertainment':
        if feature == 'Streaming Entertainment':
            return  'Amazon Prime Video for Windows'
        elif feature == 'On-Demand Video Streaming':
            return 'Netflix'
        elif feature == 'Audio Enhancement':
            return 'Dolby Access'
        elif feature == 'Gaming Console Integration':
            return 'Xbox'
        elif feature == 'Immersive Audio Experience':
            return 'DTS Sound Unbound'
        elif feature == 'Enhanced YouTube Viewing':
            return 'YouPlay - YouTube Player'
        elif feature == '3D Painting and Art Creation':
            return 'Paint 3D'
        elif feature == 'Streaming Anime and Manga':
            return 'Crunchyroll'
        elif feature == 'Relaxing Coloring Book Experience':
            return 'Zen: Coloring book for adults'
        elif feature == 'DVD Playback Support':
            return 'DVD Player'
        elif feature == 'youTube Video Download and Conversion':
            return 'GoTube - Video Downloader for YouTube 4K. MP4 & MP3 Music Converter'
        elif feature == 'Personalized Video Recommendations':
            return 'Videoder'
        elif feature == 'Smart Photo Organization':
            return 'Xbox Insider Hub'
    elif category == 'Music':
         if feature == 'Music Streaming':
             return 'Spotify Music'
         elif feature == 'Media Library Management':
             return 'iTunes'
         elif feature == 'Music Streaming & Discovery':
             return 'Gaana'
         elif feature == 'Extensive Music Library and Radio':
             return 'JioSaavn Music & Radio'
         elif feature == 'YouTube Video Download and Conversion':
             return 'TubeMate - YouTube Video Downloader.'
         elif feature == 'Bluetooth Audio Connectivity':
             return 'Bluetooth Audio Receiver'
         elif feature == 'Collaborative Music Creation':
             return 'Music Maker Jam'
         elif feature == 'Personalized Radio Station Recommendations':
             return 'TuneIn Radio'
         elif feature == 'Real-time Pitch Correction in Karaoke':
             return 'Karaoke One'
         elif feature == 'Download and convert YouTube videos to various formats':
             return 'SnapTube Converter'
         elif feature == 'Virtual piano with customizable key layouts':
             return 'Piano 10'
         elif feature == 'AI-assisted automatic beatmatching':
             return 'Transitions DJ'
         elif feature == 'Automatic beatmatching and BPM synchronization for seamless mixing':
             return 'edjing 5: DJ turntable to mix and record music'
         elif feature == 'AI-generated dynamic playlists based on user mood and preferences.':
             return 'MP3 Player - Music Player & Equalizer'
    elif category == 'Photo and Videos':
         if feature == 'Media Player':
             return 'VLC UWP'
         elif feature == 'Photo Editing':
             return 'Adobe Lightroom'
         elif feature == 'Photo Editing Mastery':
             return 'Adobe Photos+A21:A43hop Express'
         elif feature == 'Creative Photo Collages':
             return 'Picsart Photo Studio: Collage Maker and Picture Editor'
         elif feature == 'Cinematic Video Editing':
             return 'Movie Maker - Video Editor'
         elif feature == 'Comprehensive PDF Toolkit':
             return 'Reader For Adobe Acrobat PDF Editor '
         elif feature == 'AI-Powered Photo Editing':
             return 'Luminar AI'
         elif feature == 'Versatile Video Editing':
             return 'FilmForth: video editor,'
         elif feature == 'High-Definition Video Playback':
             return 'All Video Player HD'
         elif feature == 'User-Friendly Video Editing':
             return 'Animotica - Movie Maker'
         elif feature == 'Multi-functional Screen Recording Suite':
             return 'RecForth - Free Screen Recorder'
         elif feature == 'HEIC Image Format Support and Conversion':
             return 'HEIC Image Viewer, '
         elif feature == 'Advanced Photo Editing Suite':
             return 'PhotoScape X'
         elif feature == 'Advanced photo Editing Tools':
             return 'Photo Editor | Polar'
         elif feature == 'Video and Music Conversion':
             return 'VidMate Converter'
         elif feature == 'Epson Printer Management':
             return 'Epson Print and Scan'
         elif feature == 'Customizable Web Browser':
             return 'YouTuBrowser'
         elif feature == 'High-Quality Media Playback with 4K UHD and HDR':
             return 'CnX Media Player - 4K UHD & HDR Video Player'
         elif feature == 'Free and Easy Video Editing':
             return 'Movie Maker : Free Video Editor'
         elif feature == 'Open-Source Media Center and Entertainment Hub':
             return 'Kodi'
         elif feature == 'Samsung Device Photo Gallery':
             return 'Samsung Gallery'
         elif feature == 'Universal Video Playback':
             return 'Video Player - Play All Videos'
         elif feature == 'Comprehensive Video Editing Studio':
             return 'Video Editor Studio : Movie Maker, Flim Editor, Audio Mixer and More'
    return 'No recommendation'


def get_features_for_category(category):
    # Replace this with your logic to fetch features based on the selected category
    # For example, you can use a database query
    # Dummy data for illustration purposes
    if category == 'Social':
        return ['messaging', 'Secure Messaging', 'Social Photo Sharing','Social Networking','Visual Discovery and Inspiration', 'Instant Messaging', 'Social News Aggregation and Discussion', 'Unofficial Telegram Client', 'Desktop Version of imo for Video Calls and Chat', 'Professional Networking Analytics', 'Universal Cloud Dashboard', 'Integrated website analytics and insights.', 'Augmented reality constellation identification', 'seamless integration with Windows notifications', 'AI-powered smart replies and suggested stickers in LINE messages', 'Tumblr for browsing and posting on the social media platform']
    elif category == 'Entertainment':
        return ['On-Demand Video Streaming','Streaming Entertainment', 'Audio Enhancement','Gaming Console Integration', 'Immersive Audio Experience', '3D Painting and Art Creation', 'Streaming Anime and Manga', ' DVD Playback Support', 'youTube Video Download and Conversion', 'Sketching and Drawing Application', 'Personalized Video Recommendations', 'Smart Photo Organization', 'Dynamic Crosshair Customization', 'AI-Enhanced Coloring Suggestions', '4K Video Downloads and MP3 Conversion', ' Frame-by-Frame Animation Creation', ' Floating Video Player for Multitasking', ' Live TV Streaming and Media Conversion', 'Multiscreen TV Streaming', 'Advanced audio enhancements for immersive gaming and media experiences']
    elif category == 'Music':
        return['Music Streaming', 'Media Library Management', ' Music Streaming', 'Music Streaming & Discovery', 'Extensive Music Library and Radio', 'YouTube Video Download and Conversion', 'Bluetooth Audio Connectivity', 'YouTube Video and Music Download and Conversion', ' Collaborative Music Creation', 'Personalized Radio Station Recommendations', 'Real-time Pitch Correction in Karaoke', 'Download and convert YouTube videos to various formats..', 'Virtual piano with customizable key layouts.', 'AI-assisted automatic beatmatching.', 'Automatic beatmatching and BPM synchronization for seamless mixing.', 'AI-generated dynamic playlists based on user mood and preferences.']
    elif category == 'Photo and Videos':
        return['Media Player', ' Photo Editing', 'Photo Editing Mastery', ' Creative Photo Collages', 'Cinematic Video Editing', 'Comprehensive PDF Toolkit', 'AI-Powered Photo Editing', 'Versatile Video Editing', 'High-Definition Video Playback', 'User-Friendly Video Editing', ' Multi-functional Screen Recording Suite', 'HEIC Image Format Support and Conversion', 'Advanced Photo Editing Suite', 'Video and Music Conversion', ' Advanced Photo Editing Tools', 'Epson Printer Management', 'Customizable Web Browser', ' High-Quality Media Playback with 4K UHD and HDR', 'Free and Easy Video Editing', ' Open-Source Media Center and Entertainment Hub', 'Samsung Device Photo Gallery', 'Universal Video Playback', 'Comprehensive Video Editing Studio']
    elif category == 'Productivity' :
        return['Device Integration',]
    
    else:
        return []

if __name__ == '__main__':
    app.run(debug=True)
