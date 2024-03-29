class MyQueue {
public:
    stack<int>st1;
    stack<int>st2;
    MyQueue() {
        
    }
    
    void push(int x) {
        st1.push(x);
    }
    
    int pop() {
        while(!st1.empty())
        {
            int val = st1.top();
            st1.pop();
            st2.push(val);
        }
        int res = st2.top();
        st2.pop();
        while(!st2.empty())
        {
            int val1 = st2.top();
            st2.pop();
            st1.push(val1);
        }
        return res;
    }
    
    int peek() {
        while(!st1.empty())
        {
            int val = st1.top();
            st1.pop();
            st2.push(val);
        }
        int res = st2.top();
        while(!st2.empty())
        {
            int val1 = st2.top();
            st2.pop();
            st1.push(val1);
        }
        return res;
    }
    
    bool empty() {
        return st1.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */