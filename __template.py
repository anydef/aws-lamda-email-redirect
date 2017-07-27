def render_template(**kwargs):
    return '''
        <html>
            <body>
                <h1>Hi, you received a message from {name}</h1>
                <h2>Subject: {subject}</h2>
                <h2>Message:</h2>
                <p>{message}</p>
            </body>
        </html>
    '''.format(**kwargs)
