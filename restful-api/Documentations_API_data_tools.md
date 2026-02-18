# Basics of HTTP/HTTPS

## Objective
At the end of this exercise, students should be able to:
- Install and use `curl` from the command line.
- Construct and execute basic API requests using `curl`, including setting headers and inspecting the output.
- Interpret the results of common API requests.

## Resources
1. [curl - Everything curl](https://ec.haxx.se/)
2. [Using cURL to interact with HTTP APIs](https://thevalleyofcode.com/lesson/http/http-curl/)
3. Public API to play with: [JSONPlaceholder](https://jsonplaceholder.typicode.com/)


## Glossary
| Word | Definition | 
|----------|-------------|
| curl | Abbreviation for client URL  |
| TLS | Transport Layer Security |
| HTTP**S** | HyperText Transfer Protocol **Secure** |


## Key `curl` Flags

| Flag | Purpose | Example |
|---|---|---|
| `--version` | Check the installed version | `curl --version` |
| `-I` | Fetch headers only (HEAD request) | `curl -I https://example.com` |
| `-X` | Specify the HTTP method | `curl -X POST https://...` |
| `-d` | Send data in the request body | `curl -d '{"key":"value"}'` |
| `-H` | Add a custom request header | `curl -H "Content-Type: application/json"` |
| `-v` | Verbose mode (see full request + response) | `curl -v https://example.com` |
| `-o` | Save the response to a file | `curl -o result.json https://...` |

> **Quick reminder**: `-X` sets the method · `-d` sends data · `-H` adds a header · `-I` shows headers only · `-v` is the best for debugging.

---

# Exercise — Using `curl` to Interact with HTTP APIs

## 1. Installing and Basic Interaction with `curl`

### Installation

`curl` comes pre-installed on most macOS and Linux systems. 
For Windows, you can use WSL (Windows Subsystem for Linux) or download it from [curl.se](https://curl.se/download.html).

### Verifying the installation

```bash
curl --version
```

**Expected output:**

```
curl 8.4.0 (x86_64-apple-darwin23.0) libcurl/8.4.0 ...
Protocols: dict file ftp ftps gopher http https imap ...
Features: alt-svc AsynchDNS GSS-API HSTS HTTP2 HTTPS-proxy ...
```

The output confirms that `curl` is installed and lists all the supported protocols and features.
The most important ones to notice are `http` and `https` in the Protocols section

### Fetching a webpage

```bash
curl http://example.com
```

**Expected output:**

```html
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
    ...
</head>
<body>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples...</p>
</body>
</html>
```

`curl` retrieves the raw HTML content of the page and prints it directly to the terminal, just like a browser would receive it (except without rendering it visually)

---

## 2. Fetching Data from an API

### Retrieving all posts

```bash
curl https://jsonplaceholder.typicode.com/posts
```

**Expected output (truncated):**

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor..."
  },
  ...
]
```

The response is a **JSON array** containing 100 posts.
Each post object has four attributes:

| Attribute | Type | Description |
|---|---|---|
| `userId` | integer | ID of the user who created the post |
| `id` | integer | Unique identifier of the post |
| `title` | string | Title of the post |
| `body` | string | Content of the post |

### Fetching a single post

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

**Expected output:**

```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita..."
}
```

> **Tip**: pipe the output to `jq` for cleaner, color-highlighted JSON formatting:
> ```bash
> curl https://jsonplaceholder.typicode.com/posts/1 | jq
> ```

---

## 3. Using Headers and Other Options with `curl`

### Fetching only the response headers (`-I`)

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

**Expected output:**

```
HTTP/2 200
date: Tue, 17 Feb 2026 10:00:00 GMT
content-type: application/json; charset=utf-8
x-powered-by: Express
cache-control: max-age=43200
expires: Tue, 17 Feb 2026 22:00:00 GMT
vary: Origin, Accept-Encoding
access-control-allow-credentials: true
```

The `-I` flag sends a `HEAD` request, which retrieves **only the headers** without downloading the response body. This is useful for:
- Checking the **status code** (`200 OK`) without downloading all the data.
- Inspecting the **Content-Type** to confirm the API returns JSON.
- Reviewing **cache settings** (`cache-control`, `expires`).
- Checking **CORS headers** (`access-control-allow-credentials`).

### Making a POST request (`-X POST` and `-d`)

```bash
curl -X POST \
  -d "title=foo&body=bar&userId=1" \
  https://jsonplaceholder.typicode.com/posts
```

**Expected output:**

```json
{
  "title": "foo",
  "body": "bar",
  "userId": "1",
  "id": 101
}
```

The server responds with the simulated newly created post, including a generated `id` of `101`. 
Since JSONPlaceholder is a mock API, the post is not actually saved — but the response mimics what a real REST API would return.

### Making a POST request with JSON (better practice)

When working with real APIs, it is better to send data as JSON rather than form-encoded data. Use the `-H` flag to set the `Content-Type` header and `-d` to send a JSON body:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"title": "foo", "body": "bar", "userId": 1}' \
  https://jsonplaceholder.typicode.com/posts
```

**Expected output:**

```json
{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}
```

---


