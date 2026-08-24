class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = dict(paths)
        c = paths[0][0]
        while c in d:
            c = d[c]
        return c