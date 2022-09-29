from rss_feed_reader import create_app

app = create_app()
app.secret_key = "dfhue834729hg462v"

if __name__ == '__main__':
    app.run(debug=True)