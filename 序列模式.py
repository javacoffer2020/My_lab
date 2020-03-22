#!/usr/bin/env python
# coding: utf-8

# In[1]:


import itertools
import pandas as pd


# In[2]:


def createC1(dataSet):  
    C1 = set(itertools.chain(*dataSet))  
    
    return [frozenset([i]) for i in C1]


# In[3]:


def scanD(dataSet, Ck, min_support):
    support = {}

    for i in dataSet:
        for j in Ck:
            if j.issubset(i):
                support[j] = support.get(j, 0) + 1

    n = len(dataSet)

    return {k: v/n for k, v in support.items() if v/n >= min_support}


# In[4]:


def aprioriGen(Lk):  
    lenLk = len(Lk)
    k = len(Lk[0])
    if lenLk > 1 and k > 0:
        return set([
                Lk[i].union(Lk[j])
                for i in range(lenLk - 1)
                for j in range(i + 1, lenLk)
                if len(Lk[i] | Lk[j]) == k +1
            ])  


# In[5]:


def apriori(dataSet, min_support=0.5): 
    C1 = createC1(dataSet)
    L1 = scanD(dataSet, C1, min_support)
    L = [L1, ]       # Large-itemsets
    k = 2
    while len(L[k-2]) > 1:
        Ck = aprioriGen(list(L[k-2].keys()))
        Lk = scanD(dataSet, Ck, min_support)
        if len(Lk) > 0:
            L.append(Lk)
            k += 1
        else:
             break
                
    d = {}
    for Lk in L:  
        d.update(Lk)
    return d


# In[6]:


def rulesGen(iterable):  
    subSet = []
    for i in range(1, len(iterable)):
        subSet.extend(itertools.combinations(iterable, i))
        
    return [(frozenset(lhs), frozenset(iterable.difference(lhs))) for lhs in subSet] 


# In[7]:


def arules(dataSet, min_support=0.5):
    L = apriori(dataSet, min_support) 
    rules = []
    for Lk in L.keys():
        if len(Lk) > 1:
            rules.extend(rulesGen(Lk))
    
    scl = []
    for rule in rules:
        lhs = rule[0]; rhs = rule[1]
        support = L[lhs | rhs]
        confidence = support / L[lhs]
        lift = confidence / L[rhs]
        scl.append({'LHS':lhs, 'RHS':rhs, 'support':support, 'confidence':confidence, 'lift':lift})
        
    return pd.DataFrame(scl)


# In[8]:


def createLs1(dataSet, min_support):
    n = len(dataSet)
    flattenSet = list(itertools.chain(*dataSet))
    flatten_n = len(flattenSet)
    
    min_support_new = min_support * n / flatten_n
    litemsets = apriori(flattenSet, min_support=min_support_new)
    mapping = {v:k for k,v in enumerate(litemsets)}
    
    supportLs1 = {(mapping[k],):v * flatten_n / n
                 for k,v in litemsets.items()}
    
    return mapping, supportLs1


# In[9]:


def seqMapping(seq, mapping):
    newSeq = []
    for iSet in seq:
        newSet = [v for k,v in mapping.items() if k <= set(iSet)]
        if newSet != []:
            newSeq.append(newSet)
    return newSeq

def transform(dataSet, mapping):
    transformDS = []
    for seq in dataSet:
        newSeq = seqMapping(seq, mapping)
        if newSeq !=[]:
            transformDS.append(newSeq)
    return transformDS


# In[10]:


def seqGen(seqA, seqB):
    newA, newB = seqA.copy(), seqB.copy()
    if seqA[:-1] == seqB[:-1]:
        newA.append(seqB[-1])
        newB.append(seqA[-1])
        return [newA, newB]
    
def CsGen(Ls):
    Cs = []
    for seqA, seqB in itertools.combinations(Ls, 2):
        newSeqs = seqGen(seqA, seqB)
        if newSeqs != None:
            Cs.extend(newSeqs)
    return [seq for seq in Cs if seq[1:] in Ls]


# In[11]:


def isSubSeq(seq,cusSeq):
    nSeq, nCusSeq = len(seq), len(cusSeq)
    if nSeq > nCusSeq:
        return False
    if nSeq == 1:
        return any([seq[0] in i for i in cusSeq])
    if nSeq > 1:
        head = [seq[0] in i for i in cusSeq]
        if any(head):
            split = head.index(True)
            return isSubSeq(seq[1:], cusSeq[split + 1:])
        else:
            return False


# In[12]:


def calcSupport (transformDS, Cs, min_support):
    supportLsk = {}; n = len(transformDS)
    if len(Cs) >= 1:
        for seq in Cs:
            support = sum([isSubSeq(seq, cusSeq) for cusSeq in transformDS]) / n
            if support >= min_support:
                supportLsk.update({tuple(seq):support})
    return [list(k) for k in supportLsk], supportLsk


# In[13]:


def isSubSeq2(seq, cusSeq):
    nSeq, nCusSeq = len(seq), len(cusSeq)
    
    if nSeq > nCusSeq:
        return False
    if nSeq == 1:
        return any([seq[0].issubset(i) for i in cusSeq])
    if nSeq > 1:
        head = [seq[0].issubset(i) for i in cusSeq]
        if any(head):
            split = head.index(True)
            return isSubSeq2(seq[1:], cusSeq[split:])
        else:
            return False


# In[14]:


def notProperSubSeq(seq, cusSeq):
    if seq == cusSeq:
        return True
    else:
        return not isSubSeq2(seq, cusSeq)


# In[15]:


def maxLs(Ls, supportLs):
    LsCopy = Ls.copy()
    lenL, lenC = len(Ls), len(LsCopy)
    while lenC > 1 and lenL > 1:
        if LsCopy[lenC - 1] in Ls:
            mask = [notProperSubSeq(seq, LsCopy[lenC-1]) for seq in Ls]
            Ls = list(itertools.compress(Ls, mask))
            lenL = len(Ls)
            
        lenC -= 1

    supportLs = {tuple(seq):supportLs[tuple(seq)] for seq in Ls}

    return Ls, supportLs


# In[16]:


def aprioriAll(dataSet, min_support=0.4):
    mapping, supportLs1 = createLs1(dataSet, min_support)
    Ls1 = [list(k) for k in supportLs1]
    transformDS = transform(dataSet, mapping)
    
    LsList = [Ls1]; supportLs = supportLs1.copy()
    k =1
    while k >= 1 and len(LsList[-1]) > 1:
        Csk = CsGen(LsList[-1])
        Lsk, supportLsk = calcSupport(transformDS, Csk, min_support)
        if len(Lsk) > 0:
            LsList.append(Lsk); supportLs.update(supportLsk)
            k += 1
        else:
            break
        
    Ls = list(itertools.chain(*LsList))
    tr_mapping = {v:k for k,v in mapping.items()}
    Ls = [[tr_mapping[k] for k in seq] for seq in Ls]
    supportLs = {tuple([tr_mapping[i] for i in k]):v for k,v in supportLs.items()}
    
    Ls, supportLs = maxLs(Ls, supportLs)
    return pd.DataFrame(list(supportLs.items()), columns=['sequence', 'support'])


# In[17]:


def aggFunc(*args):
    agg = itertools.chain(*args)
    return list(agg)


# In[18]:


Transactions = pd.read_csv('Transactions.csv')
baskets = Transactions['Model'].groupby([Transactions['OrderNumber'], Transactions['LineNumber']]).apply(aggFunc)
dataSet = list(baskets.groupby(level=0).apply(list))
aprioriAll(dataSet, min_support=0.05).head()

