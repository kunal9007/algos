class Queue {
    constructor() {
        this.data = [];
        this.rear = 0;
        this.size = 20;
    }

    enqueue(ele) {
        if (this.rear < this.size) {
            this.data[this.rear] = ele;
            this.rear = this.rear + 1;
        }
    }

    length() {
        return this.rear;
    }

    isEmpty() {
        return this.rear === 0;
    }

    getFront() {
        if (this.isEmpty() === false) {
            return this.data[0];
        }
    }

    getLast() {
        if (this.isEmpty() === false) {
            return this.data[this.rear - 1];
        }
    }

    dequeue() {
        if (this.isEmpty() === false) {
            this.rear = this.rear - 1;
            return this.data.shift();
        }
    }

    print() {
        for (let i = 0; i < this.rear; i++) {
            console.log(this.data[i]);
        }
    }

    clear() {
        this.data.length = 0;
        this.rear = 0;
    }
}

const q = new Queue();
q.enqueue(1);
q.enqueue(23);
let l = q.length();
console.log(l)