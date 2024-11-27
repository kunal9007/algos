class Stack {
    constructor() {
        this.stack = []
        this.size = 0
        this.top = 0
    }
    push(value) {
        this.stack[this.top] = value;
        this.top++;
    }
    pop() {
        this.stack[this.top] = null;
    }
    length() {
        return this.stack.length;
    }
    print() {
        for (let i = 0; i < this.stack.length; i++) {
            console.log(this.stack[i]);
        }
    }
    peek() {
        return this.stack[this.top - 1];
    }
}

const s = new Stack();
s.push(10);
s.push(20);
s.push(30);

s.print();
let peeked = s.peek();
console.log(peeked);

