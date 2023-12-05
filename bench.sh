#!/bin/bash
set -Eeuo pipefail

N=10

for s in $(find . -name '*py' | sort); do
    echo -n "$s: "
    totals=()
    for _ in $(seq 1 $N); do
        d=$(dirname "$s")
        start=$(date +%s%N)
        python3 "$s" < "$d/input" >/dev/null
        total_ms="$((($(date +%s%N) - "$start")/1000000))"
        totals+=("$total_ms")
        echo -n "$total_ms "
    done
    echo -n "ms | avg: "

    sum=0
    for e in "${totals[@]}"; do
        sum=$(("$sum" + "$e"))
    done
    echo "$(("$sum" / "$N")) ms"

done
