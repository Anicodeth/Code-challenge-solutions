function countTriples(n: number): number {
    let count = 0;

    for (let a = 1; a <= n; a++) {
        const start = a * a;

        for (let b = 1; b <= n; b++) {
            const c = Math.sqrt(start + b * b);

            if (Number.isInteger(c) && c <= n) {
                count++;
            }
        }
    }

    return count;
}
