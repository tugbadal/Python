# -*- coding: cp1254 -*-

class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.left = None
        self.right = None

    def __str__(self):
        return "[%s, %s, %s]" % (self.key, str(self.left), self.right)

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t

    def getRootVal(self):
        return self.key

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    # en b�y�k eleman
    def maxValue(self, root):
        while root.right != None:
            root = root.right
        return root.key

    # en k���k eleman
    def minValue(self, root):
        while(root.left != None):
            root = root.left
        return root.key

    # d���m say�s�
    def size(self, root):
        if root == None:
            return 0
        else:
            return self.size(root.left) + 1 + self.size(root.right)

    # k�kten b�y�k eleman say�s�
    def koktenBuyukSayisi(self, root):
        return self.size(root.right)

    # bst den s�ral� liste elde et k���kten b�y��e, ��kabilir.
    def siraliListe(self, root):
        if root == None:
            return []
        else:
            return self.siraliListe(root.left) + [root.key] + self.siraliListe(root.right)

    # b�y�kten k����e liste elde et
    def buyuktenKucugeSiraliListe(self, root):
        if root == None:
            return []
        else:
            return self.buyuktenKucugeSiraliListe(root.right) + [root.key] + self.buyuktenKucugeSiraliListe(root.left)

    # bu son 2 metodu ben ekledim, belki ��kar
    # aranan eleman var m�?
    def ara(self, root, eleman):
        if root == None:
            return 0
        else:
            if eleman == root.key:
                return 1
            else:
                if eleman < root.key:
                    return self.ara(root.left, eleman)
                else:
                    return self.ara(root.right, eleman)

    # en derindeki eleman
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            return max(ldepth, rdepth) + 1

def main():  
    t = BinaryTree(6)

    t.insertLeft(2)
    t.left.insertLeft(1)
    t.left.insertRight(4)

    t2 = t.left.getRightChild()
    t2.insertLeft(3)

    t.insertRight(8)
    t.right.insertLeft(7)
    t.right.insertRight(12)
    
    print "A�a�:\n", t
    print ""
    print "k�k: \n", t.getRootVal()

    print ""
    solAltAgac = t.left
    print "Sol Alt A�a�:\n", solAltAgac

    print ""
    print "Sol Alt A�ac�n K�k�:\n", solAltAgac.getRootVal()

    print ""
    print "En B�y�k Eleman:\n", t.maxValue(t)

    print ""
    print "En K���k Eleman:\n", t.minValue(t)

    print ""
    print "d���m say�s�: \n", t.size(t)

    print ""
    print "BST nin k�kten b�y�k eleman say�s�: \n", t.koktenBuyukSayisi(t)

    print ""
    print "S�ral� Liste elde et: \n", t.siraliListe(t)

    print ""
    print "B�y�kten K����e S�ral� liste: \n", t.buyuktenKucugeSiraliListe(t)

    print ""
    print "5 Eleman�n� var m�? (1 evet var, 0 hay�r yok): \n", t.ara(t, 4)

    print ""
    print "Max Depth(en derindeki eleman):\n", t.maxDepth(t)

if __name__ == '__main__':
    main()
