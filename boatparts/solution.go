package main

import (
        "fmt"
)

var p, n, d int = 0, 0, 0
var w string

func strInArr(str string, a []string) bool {
        for j := 0; j < len(a); j++ {
                if a[j] == str {
                        return true
                }
        }
        return false
}

func main() {
        fmt.Scan(&p, &n)
        var seen = make([]string, 0)
        for i := 0; i < n; i++ {
                fmt.Scan(&w)
                if !(strInArr(w, seen)) {
                        seen = append(seen, w)
                        d = i + 1
                }
        }
        if len(seen) == p {
                fmt.Println(d)
        } else {
                fmt.Println("paradox avoided")
        }
}
