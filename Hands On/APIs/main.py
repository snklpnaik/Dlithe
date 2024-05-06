import requests

#url="https://jsonplaceholder.typicode.com/todos/1"
# result=requests.get(url)
# data=result.json()
# print(result)
# #<Response [200]>
# print(data)
# #{'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
# print(result.status_code)
# #200
# print(result.headers)
# #{'Date': 'Thu, 02 May 2024 13:05:50 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Report-To': '{"group":"heroku-nel","max_age":3600,"endpoints":[{"url":"https://nel.heroku.com/reports?ts=1712094370&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=gF1qH1e1LtNN9tUnIPeGWmDZMZ38me0RTEPGnWhrzY4%3D"}]}', 'Reporting-Endpoints': 'heroku-nel=https://nel.heroku.com/reports?ts=1712094370&sid=e11707d5-02a7-43ef-b45e-2cf4d2036f7d&s=gF1qH1e1LtNN9tUnIPeGWmDZMZ38me0RTEPGnWhrzY4%3D', 'Nel': '{"report_to":"heroku-nel","max_age":3600,"success_fraction":0.005,"failure_fraction":0.05,"response_headers":["Via"]}', 'X-Powered-By': 'Express', 'X-Ratelimit-Limit': '1000', 'X-Ratelimit-Remaining': '999', 'X-Ratelimit-Reset': '1712094375', 'Vary': 'Origin, Accept-Encoding', 'Access-Control-Allow-Credentials': 'true', 'Cache-Control': 'max-age=43200', 'Pragma': 'no-cache', 'Expires': '-1', 'X-Content-Type-Options': 'nosniff', 'Etag': 'W/"53-hfEnumeNh6YirfjyjaujcOPPT+s"', 'Via': '1.1 vegur', 'CF-Cache-Status': 'HIT', 'Age': '23949', 'Server': 'cloudflare', 'CF-RAY': '87d839a5ac8c096e-HKG', 'Content-Encoding': 'gzip', 'alt-svc': 'h3=":443"; ma=86400'}
# print(result.headers["Date"])
# #Thu, 02 May 2024 13:07:25 GMT


# url="https://jsonplaceholder.typicode.com/todos/"
# data={
#     "userId":1,
#     "title":"Change Change blabla",
#     "completed":False
# }
# result=requests.post(url,json=data)
# print(result.json())

#PUT-to overwrite
# url="https://jsonplaceholder.typicode.com/todos/"
# data={
#     "userId":1,
#     "title":"Wowowww",
#     "completed":False
# }
# result=requests.put(url,json=data)
# print(result.json())
# print(result.status_code)

#PATCH
url="https://jsonplaceholder.typicode.com/todos/15"
data={
    "title":"nono"
}
result=requests.patch(url,json=data)
print(result.json())
print(result.status_code)
