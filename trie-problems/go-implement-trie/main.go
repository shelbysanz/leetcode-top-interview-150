package main

import "fmt"

type Trie struct {
	children map[byte]*Trie
	isLeaf   bool
}

func Constructor() Trie {
	return Trie{children: make(map[byte]*Trie)}
}

func (this *Trie) Insert(word string) {
	curr := this
	for i := 0; i < len(word); i++ {
		b := word[i]
		val, ok := curr.children[b]
		if !ok {
			val = &Trie{children: make(map[byte]*Trie)}
			curr.children[b] = val
		}
		curr = val
	}
	curr.isLeaf = true
}

func (this *Trie) find(word string) (*Trie, bool) {
	curr := this
	for i := 0; i < len(word); i++ {
		b := word[i]
		val, ok := curr.children[b]
		if !ok {
			return nil, false
		}
		curr = val
	}
	return curr, true
}

func (this *Trie) Search(word string) bool {
	curr, found := this.find(word)
	return curr != nil && curr.isLeaf && found
}

func (this *Trie) StartsWith(prefix string) bool {
	_, found := this.find(prefix)
	return found
}

func main() {
	trie := Constructor()
	trie.Insert("apple")
	fmt.Println("search apple:", trie.Search("apple"))
	fmt.Println("search app:", trie.Search("app"))
	fmt.Println("starts with app:", trie.StartsWith("app"))
	trie.Insert("app")
	fmt.Println("search app:", trie.Search("app"))
}
