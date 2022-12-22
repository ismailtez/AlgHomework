class Solution(object):
    def getMinimumDifference(self, root):
        dif = 2 ** 16
        val = []
        q = [root]
        while q:
            ptr = q.pop(0)
            for i in val:
                if abs(i - ptr.val) < dif:
                    dif = abs(i - ptr.val)

            val.append(ptr.val)

            if ptr.left != None:
                q.append(ptr.left)

            if ptr.right != None:
                q.append(ptr.right)

        return dif
