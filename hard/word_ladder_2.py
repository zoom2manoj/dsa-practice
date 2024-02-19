from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    wordList = set(wordList)
    if endWord not in wordList:
        return []

    graph = defaultdict(list)
    distance = {word: float('inf') for word in wordList}
    distance[beginWord] = 0

    queue = deque([(beginWord, [beginWord])])

    while queue:
        current_word, path = queue.popleft()

        if current_word == endWord:
            return [path]

        for i in range(len(current_word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + char + current_word[i + 1:]
                if next_word in wordList and distance[next_word] >= distance[current_word] + 1:
                    distance[next_word] = distance[current_word] + 1
                    graph[current_word].append(next_word)
                    queue.append((next_word, path + [next_word]))

    result = []
    dfs(beginWord, endWord, graph, [beginWord], result)
    return result

def dfs(word, endWord, graph, path, result):
    print('3434', graph, path, result)
    if word == endWord:
        result.append(path[:])
        return

    if word not in graph:
        return

    for next_word in graph[word]:
        dfs(next_word, endWord, graph, path + [next_word], result)

# Example usage:
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(findLadders(beginWord, endWord, wordList))
