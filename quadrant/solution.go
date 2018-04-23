package main

import (
        "fmt"
)

func main() {
        var x, y int
        fmt.Scan(&x, &y)
        switch {
        case x > 0 && y > 0:
                fmt.Println(1)
        case x < 0 && y > 0:
                fmt.Println(2)
        case x < 0 && y < 0:
                fmt.Println(3)
        case x > 0 && y < 0:
                fmt.Println(4)
        }
}
