class Solution(object):
    def averageOfLevels(self, root):
        sums, counts = [], []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(sums):
                sums.append(0)
                counts.append(0)
            sums[depth] += node.val
            counts[depth] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return [s / float(c) for s, c in zip(sums, counts)]
