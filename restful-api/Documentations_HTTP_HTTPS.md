# Basics of HTTP/HTTPS

## Objective
At the end of this exercise, students should be able to:
- Differentiate between HTTP and HTTPS.
- Understand the basic working and structure of HTTP requests and responses.
- Recognize and explain the common HTTP methods and status codes.

## Resources
1. [Mozilla Developer Network (MDN) - An Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
2. [Difference between HTTP and HTTPS](https://www.cloudflare.com/fr-fr/learning/ssl/why-is-http-not-secure/)
3. [List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes)


## Glossary
| Word | Definition | 
|----------|-------------|
| HTTP | HyperText Transfer Protocol |
| TLS | Transport Layer Security |
| HTTP**S** | HyperText Transfer Protocol **Secure** |

---

## Differences between HTTP and HTTPS

**HTTP** is the basic communication protocol for the web
It transmits data in plain text: anyone capable of intercepting network traffic can read the content being exchanged (logins, passwords, personal data, etc.)

**HTTPS** is the secure version
It adds a layer of encryption using the TLS protocol
Even if an attacker intercepts the data, they will only see an unreadable, encrypted stream


### Comparison

| Critère | HTTP | HTTPS |
|---|---|---|
| Encryption | ❌ None | ✅ TLS/SSL |
| Default port | 80 | 443 |
| Data readable by third parties | Yes (plain text) | No (encrypted) |
| Certificate required | No | Yes |
| Recommended use | Never for sensitive data | Always |
| Example URL | `http://exemple.com` | `https://exemple.com` |


### Why it's important

- With HTTP, an attacker on the same Wi-Fi network can see your password in plain text (known as a man-in-the-middle attack)
- HTTPS guarantees three things:
  - **confidentiality** - no one else can read it
  - **integrity** - the data is not modified en route
  - **authenticity** - you are talking to the right server
- All sites that handle sensitive data (banks, email, social networks) use HTTPS

> 💡 **Note Wireshark** :
> if you capture HTTP traffic with Wireshark, you will see the content in plain text in the “Follow TCP Stream” tab
> With HTTPS, you will only see incomprehensible encrypted bytes

---

## Structure of an HTTP Request and Response

### HTTP Request Structure

```
GET /users/42 HTTP/1.1
Host: api.example.com
Accept: application/json
Authorization: Bearer my-token
User-Agent: Mozilla/5.0

(empty body for a GET request)
```

| Element | Example | Description |
|---|---|---|
| **Method** | `GET` | The action to perform |
| **Path** | `/users/42` | The requested resource |
| **Version** | `HTTP/1.1` | Protocol version |
| **Headers** | `Host: …` | Metadata (format, language, auth…) |
| **Body** | `{"name": "Sofiane"}` | Data sent (POST, PUT…) |

### HTTP Response Structure

```
HTTP/1.1 200 OK
Date: Tue, 17 Feb 2026 10:00:00 GMT
Content-Type: application/json
Content-Length: 85

{
  "id": 42,
  "name": "Sofiane Messaoui",
  "email": "soso@example.com"
}
```

| Element | Example | Description |
|---|---|---|
| **Version** | `HTTP/1.1` | Protocol version |
| **Status code** | `200` | Result of the request |
| **Status message** | `OK` | Short description of the result |
| **Headers** | `Content-Type: …` | Response metadata |
| **Body** | `{"id": 42, …}` | Returned data |

> 💡 **How to observe it yourself**: in Chrome or Firefox or your favorite navigator, right-click → *Inspect* → *Network* tab
> Reload the page and click on the first request
> You will see the exact request and response headers

---

## Common HTTP Methods

| Method | Description | Use Case |
|---|---|---|
| **GET** | Retrieves a resource without modifying it | Loading a web page, reading a user's data from an API (`GET /users/1`) |
| **POST** | Creates a new resource | Submitting a sign-up form, publishing a new post (`POST /posts`) |
| **PUT** | Fully replaces an existing resource | Updating a user's complete profile (`PUT /users/1`) |
| **PATCH** | Partially modifies an existing resource | Changing only a user's email without touching the rest (`PATCH /users/1`) |
| **DELETE** | Deletes a resource | Removing an account or an article (`DELETE /posts/42`) |

---

## Common HTTP Status Codes

| Code | Name | Description | Concrete Scenario |
|---|---|---|---|
| **200 OK** | Success | The request succeeded and the resource is returned | A `GET /users/1` returns the user's data |
| **201 Created** | Created | The resource was successfully created | A `POST /posts` with a new title returns the created article |
| **400 Bad Request** | Bad Request | The request is malformed or the data is invalid | A form submitted with an incorrectly formatted email address |
| **401 Unauthorized** | Unauthorized | The user is not authenticated | Accessing `/profile` without providing a JWT token |
| **403 Forbidden** | Forbidden | The user is authenticated but lacks the required permissions | A regular user tries to access an admin-only route |
| **404 Not Found** | Not Found | The requested resource does not exist | A `GET /users/999` for a user that does not exist in the database |
| **500 Internal Server Error** | Server Error | The server encountered an unexpected error | A bug in the server-side code causes a crash |

> 💡 **Quick memo**: `2xx` = success · `4xx` = **your** mistake (client-side) · `5xx` = **server's** mistake
