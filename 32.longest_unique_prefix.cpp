class TrieNode {
    private TrieNode[] links;
    private final int R = 26;
    private boolean isEnd;
    private int countChar;
    
    public TrieNode() {
        links = new TrieNode[R];
    }
    
    public boolean containsKey(char ch) {
        return links[ch - 'a'] != null;
    }
    
    public TrieNode get(char ch) {
        return links[ch - 'a'];
    }
    
    public void put(char ch, TrieNode node) {
        links[ch - 'a'] = node;
    }
    
    public void setCounter() {
        countChar++;
    }
    
    public int getCounter() {
        return countChar;
    }
    
    public void setEnd() {
        isEnd = true;
    }
    
    public boolean isEnd() {
        return isEnd;
    }
}

class Solution {
    private static TrieNode root;
    
    static String[] findPrefixes(String[] arr, int N) {
        // code here
        root = new TrieNode();
        
        for (String word: arr) {
            addWord(word);
        }
        
        for (int i = 0 ; i < arr.length ; i++) {
            TrieNode node = root;
            
            int n = arr[i].length();
            for (int j = 0 ; j < n ; j++) {
                char currentChar = arr[i].charAt(j);
                node = node.get(currentChar);
                if (node.getCounter() == 1) {
                    arr[i] = arr[i].substring(0, j+1);
                    break;
                }
            }
        }
        
        return arr;
    }
    
    private static void addWord(String word) {
        TrieNode node = root;
        int n = word.length();
        
        for (int i = 0 ; i < n ; i++) {
            char currentChar = word.charAt(i);
            if (!node.containsKey(currentChar)) {
                node.put(currentChar, new TrieNode());
            }
            node = node.get(currentChar);
            node.setCounter();
        }
        
        node.setEnd();
        return;
    } 
};