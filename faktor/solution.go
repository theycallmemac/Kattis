package main

import (
        "fmt"
)

func main() {
        var a, i int
        fmt.Scan(&a, &i)
        var mult int = a * (i - 1)
        fmt.Println(mult + 1)
}
