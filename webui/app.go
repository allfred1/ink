////
  ////// wiki cms, soon.
///
package main

date = float32(time.Now().


import (
	"fmt"
	"io/ioutil"
	"net/http"
	"html/template"
	"os"
)


func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Привет, мир!")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":8080", nil)
}