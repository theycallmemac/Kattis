package main

import (
        "fmt"
)

func main() {
        var n int
        var i int = 0
        fmt.Scan(&n)
        for i < n {
                fmt.Println(i+1, "Abracadabra")
                i++
        }
}
