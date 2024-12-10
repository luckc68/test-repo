// main.go
package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Hello, World! Welcome to the Go HTTP server.")
}

func main() {
    http.HandleFunc("/", handler)
    fmt.Println("Starting server at http://localhost:8080")
    http.ListenAndServe(":8080", nil)
}
