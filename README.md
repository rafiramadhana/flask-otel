# flask-otel

## Getting Started

0. Install dependency `pip install -r requirements.txt`
1. Run infra `make infra`
2. Run server `make server`
3. Do stress test `make stress`
4. See Jaeger (http://localhost:16686/search) for traces

```
(env) ➜  flask-otel git:(main) ✗ make server
python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8080
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 719-749-963
127.0.0.1 - - [14/Oct/2023 23:18:31] "POST /books/purchase HTTP/1.1" 200 -
127.0.0.1 - - [14/Oct/2023 23:18:31] "POST /books/purchase HTTP/1.1" 200 -
127.0.0.1 - - [14/Oct/2023 23:18:31] "POST /books/purchase HTTP/1.1" 408 -
```

TODO:

- [x] Add tracing for high latency
- [x] Add tracing for error
- [x] Write blog
- [ ] Convert blog to slides
