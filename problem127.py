class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        looked_up = []
        l = len(beginWord)
        # trying to find all possible one word edit distance
        d = {}
        for word in wordList:
            for i in range(l):
                extra_word = word[:i] + "*" + word[i + 1:]
                if extra_word in d:
                    d[extra_word].append(word)
                else:
                    d[extra_word] = [word]
        # print(d)
        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while len(queue) > 0:
            curr_word, level = queue.pop(0)

            for i in range(l):
                inter = curr_word[:i] + "*" + curr_word[i + 1:]
                if inter in d:
                    for all_pos_word in d[inter]:
                        if all_pos_word == endWord:
                            return level + 1
                        if all_pos_word not in visited:
                            visited[all_pos_word] = True
                            queue.append((all_pos_word, level + 1))
        return 0