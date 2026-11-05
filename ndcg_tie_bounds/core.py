import math,itertools
from .common import number,integer,identifier,unique_ids
def run(d):
 rows=d['documents'];unique_ids(rows);k=integer(d.get('k',len(rows)),1,10000)
 if not 1<=len(rows)<=10000:raise ValueError('documents')
 for r in rows:number(r['score']);integer(r['relevance'],0,10)
 groups={}
 for r in rows:groups.setdefault(r['score'],[]).append(2**r['relevance']-1)
 ordered=sorted(groups,reverse=True);min_gains=[];max_gains=[];expected=0;position=0
 for score in ordered:
  gains=groups[score];min_gains+=sorted(gains);max_gains+=sorted(gains,reverse=True)
  mean=sum(gains)/len(gains)
  expected+=sum(mean/math.log2(i+2)for i in range(position,min(position+len(gains),k)));position+=len(gains)
 def dcg(gains):return sum(v/math.log2(i+2)for i,v in enumerate(gains[:k]))
 ideal=dcg(sorted((2**r['relevance']-1 for r in rows),reverse=True));return dict(k=k,ideal_dcg=ideal,ndcg_min=dcg(min_gains)/ideal if ideal else None,ndcg_max=dcg(max_gains)/ideal if ideal else None,ndcg_expected_uniform_ties=expected/ideal if ideal else None,tied_groups=sum(len(v)>1 for v in groups.values()))
