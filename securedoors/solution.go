package main

import (
        "fmt"
)

func check(n string, m map[string]int) bool {
        val, ok := m[n]
        if val == 0 && ok {
                return true
        }
        return false
}

func main() {
        n, a, p := 0, "", ""
        log := make(map[string]int)
        fmt.Scan(&n)
        for i := 0; i < n; i++ {
                fmt.Scan(&a, &p)
                switch a {
                case "entry":
                        switch check(p, log) {
                        case true:
                                fmt.Printf("%s entered (ANOMALY)\n", p)
                        case false:
                                log[p] = 0
                                fmt.Printf("%s entered\n", p)
                        }
                case "exit":
                        switch check(p, log) {
                        case true:
                                log[p] = 1
                                fmt.Printf("%s exited\n", p)
                        case false:
                                fmt.Printf("%s exited (ANOMALY)\n", p)
                        }
                }
        }
}
