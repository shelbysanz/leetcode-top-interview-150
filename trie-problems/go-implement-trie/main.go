package leetcode

type Trie struct {
	children map[byte]*Trie
	isLeaf   bool
}

func Constructor() Trie {
	return Trie{children: make(map[byte]*Trie)}
}

func (this *Trie) Insert(word string) {
	curr := this
	for _, b := range word {
		val, ok := curr.children[byte(b)]
		if !ok {
			val = &Trie{children: make(map[byte]*Trie)}
			curr.children[byte(b)] = val
		}
		curr = val
	}
	curr.isLeaf = true
}

func (this *Trie) Search(word string) bool {
	return false
}

func (this *Trie) StartsWith(prefix string) bool {
	return false
}
