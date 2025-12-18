package leetcode

type Node struct {
	Val, Key   int
	Prev, Next *Node
}

type LRUCache struct {
	Capacity   int
	Head, Tail *Node
	CacheMap   map[int]*Node
}

func Constructor(capacity int) LRUCache {
	this := LRUCache{
		Capacity: capacity,
		CacheMap: make(map[int]*Node, capacity),
		Head:     &Node{},
		Tail:     &Node{},
	}
	this.Head.Next = this.Tail
	this.Tail.Prev = this.Head
	return this
}

func (this *LRUCache) Get(key int) int {
	node, ok := this.CacheMap[key]
	if ok {
		this.moveToFront(node)
		return node.Val
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	node, ok := this.CacheMap[key]
	if ok {
		node.Val = value
		this.moveToFront(node)
	} else {
		node = &Node{Val: value, Key: key}
		this.addToFront(node)
	}
	if len(this.CacheMap) > this.Capacity {
		this.removeLeastRecentlyUsed()
	}
}

func (this *LRUCache) addToFront(node *Node) {
	second := this.Head.Next
	second.Prev = node
	node.Next = second
	node.Prev = this.Head
	this.Head.Next = node
	this.CacheMap[node.Key] = node
}

func (this *LRUCache) removeNode(node *Node) {
	node.Prev.Next = node.Next
	node.Next.Prev = node.Prev
	node.Prev = nil
	node.Next = nil
	delete(this.CacheMap, node.Key)
}

func (this *LRUCache) moveToFront(node *Node) {
	this.removeNode(node)
	this.addToFront(node)
}

func (this *LRUCache) removeLeastRecentlyUsed() {
	node := this.Tail.Prev
	this.removeNode(node)
}
