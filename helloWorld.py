from bottle import route, run
import tracemalloc

tracemalloc.start()

@route('/hello')
def hello():
    return "Hello World"

run(host="localhost", port=8080, debug=True)

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)