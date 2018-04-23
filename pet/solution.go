package main

import (
        "fmt"
)

const size int = 5

var arr [size]int

func main() {
        var i, j, k, l int
        var itr, n int = 0, 1
        for itr < size {
                var total int = 0
                fmt.Scan(&i, &j, &k, &l)
                total = i + j + k + l
                arr[itr] = total
                itr++
        }
        var max int = arr[0]
        var pos int = 0
        for n < len(arr) {
                if arr[n] >= max {
                        max = arr[n]
                        pos = n
                } else {
                        max = max
                        pos = pos
                }
                n++
        }
        fmt.Println(pos+1, max)

}
