package main

import (
        "fmt"
        "strconv"
        "strings"
)

var pieces = [6]int{1, 1, 2, 2, 2, 8}
var result = []string{}

func main() {
        var k, q, r, b, n, p int
        fmt.Scan(&k, &q, &r, &b, &n, &p)
        var curr = [6]int{k, q, r, b, n, p}
        var calc [6]int
        for i := 0; i < len(pieces); i++ {
                calc[i] = pieces[i] - curr[i]
                result = append(result, strconv.Itoa(calc[i]))
        }
        answer := strings.Join(result, " ")
        fmt.Println(answer)
}
