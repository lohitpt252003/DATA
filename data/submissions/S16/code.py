curl -X POST http://<your-server-ip>:5000/api/execute \
  -H "Content-Type: application/json" \
  -d '{
        "language": "python",
        "code": "print(\"Hello World from curl!\")",
        "stdin": "",
        "timelimit": 2,
        "memorylimit": 128
      }'
