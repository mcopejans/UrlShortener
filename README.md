# URL shortener
This is a basic URL shortener written by Marieke Copejans.

## Example usage
After initializing the venv python environment, you can run the backend with REST API as follows:

```
venv/bin/python/api.py
```

To test this API without frontend, you can enter the following URLs in your browser:

- Shorten the queried long URL in the query. Replace `<url>` with your long URL.
```
http://0.0.0.0:3001/shorten?long_url=<url>

```
- Enlarge a previously shortened URL. Replace `<url>` with your short URL.
```
http://0.0.0.0:3001/enlarge?short_url=<url>

```
- Optionally, it's possible to provide a custom_url query argument to create a custom short URL.
This is a special case of the shorten URL option and works as follows:
```
http://0.0.0.0:3001/shorten?long_url=<url>&custom_url="test"
```

As an example, consider the following long URL:
http://www.google.com/my/search/keyword

Default shortened URL: `http://www.goog.le/abcdef` or ìf a custom URL was specified to be 'test', the short URL will be:
`http://www.goog.le/test`.

## Frontent
Start the react frontent app as:
```
npm start
```